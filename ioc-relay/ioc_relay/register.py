import asyncio
from collections import defaultdict
import json

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
        self._get_pv(pvname)
        self._subscribers[pvname].add(websocket)

    def unsubscribe(self, websocket, pvname):
        self._subscribers[pvname].discard(websocket)
        if not self._subscribers[pvname]:
            self._remove_pv(pvname)

    def _get_pv(self, pvname):
        pv = self._pvs.get(pvname)
        if pv is None:
            pv = PV(pvname, callback=self._ca_callback)
            self._pvs[pvname] = pv
        return pv

    def _remove_pv(self, pvname):
        self._get_pv(pvname).disconnect()
        del self._pvs[pvname]

    def _ca_callback(self, **kwargs):
        coro = self._aio_callback(**kwargs)
        self._loop.call_soon_threadsafe(asyncio.ensure_future, coro)

    async def _aio_callback(self, pvname, value, **kwargs):
        payload = json.dumps({'name': pvname, 'value': value})
        subscribers = list(self._subscribers[pvname])
        for ws in subscribers:
            try:
                await ws.send(payload)
            except ConnectionClosed:
                self.unsubscribe(ws, pvname)
