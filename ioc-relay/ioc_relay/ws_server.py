import asyncio
from functools import partial
import json

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
            message = await websocket.recv()
        except ConnectionClosed:
            break
        else:
            await process_message(message, websocket=websocket, register=register)


async def process_message(message, *, websocket, register):
    try:
        data = json.loads(message)
    except json.decoder.JSONDecodeError:
        return
    action = data.get('action')
    if action == 'subscribe':
        register.subscribe(pvname=data['name'], websocket=websocket)
    elif action == 'unsubscribe':
        register.unsubscribe(pvname=data['name'], websocket=websocket)
