import asyncio
from collections import defaultdict
import json

import numpy as np
from websockets.exceptions import ConnectionClosed

from epics import PV


class Register:
    def __init__(self, *, loop):
        self._loop = loop
        self._pvs = {}
        self._subscribers = defaultdict(set)

    def subscribe(self, websocket, pvname):
        if websocket in self._subscribers[pvname]:
            return
        self._subscribers[pvname].add(websocket)
        self._get_pv(pvname).run_callbacks()

    def unsubscribe(self, websocket, pvname):
        self._subscribers[pvname].discard(websocket)
        if not self._subscribers[pvname]:
            self._remove_pv(pvname)

    def _get_pv(self, pvname):
        pv = self._pvs.get(pvname)
        if pv is None:
            pv = PV(pvname, form='ctrl', callback=self._ca_callback)
            self._pvs[pvname] = pv
        return pv

    def _remove_pv(self, pvname):
        self._get_pv(pvname).disconnect()
        del self._pvs[pvname]

    def _ca_callback(self, **kwargs):
        coro = self._aio_callback(**kwargs)
        self._loop.call_soon_threadsafe(asyncio.ensure_future, coro)

    async def _aio_callback(self, pvname, value, **kwargs):
        payload = self._make_payload(pvname=pvname, value=value, **kwargs)
        subscribers = list(self._subscribers[pvname])
        for ws in subscribers:
            try:
                await ws.send(payload)
            except ConnectionClosed:
                self.unsubscribe(ws, pvname)

    def _make_payload(self, *, pvname, value, char_value, type, **data):
        if 'string' in type or 'char' in type:
            value = char_value
        elif isinstance(value, np.ndarray):
            value = value.tolist()
        return json.dumps({'name': pvname, 'value': value})
