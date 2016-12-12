import asyncio
from functools import partial

import websockets
from websockets.exceptions import ConnectionClosed

from .register import Register


def main():
    register = Register(loop=asyncio.get_event_loop())
    handler = partial(client_handler, register=register)
    start_server = websockets.serve(handler, '0.0.0.0', 5678)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


async def client_handler(websocket, path, *, register):
    while True:
        try:
            pvname = await websocket.recv()
        except ConnectionClosed:
            break
        else:
            register.subscribe(pvname=pvname, websocket=websocket)
