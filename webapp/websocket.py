#!/usr/bin/env python3

import asyncio
import websockets
from threading import Thread


def send(message):
    asyncio.get_event_loop().run_until_complete(client(message))


async def client(message):
    uri = "ws://localhost:9000"
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)


async def server(websocket, path):
    # Register
    connected.add(websocket)

    try:
        async for message in websocket:
            for client in connected:
                if client != websocket:
                    await client.send(f'MESSAGE: {message}')
    finally:
        # Unregister
        connected.remove(websocket)

connected = set()


def start_server():
    websocket_thread = Thread(target=spawn)
    websocket_thread.start()


def spawn():
    websocket_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(websocket_loop)

    start_server = websockets.serve(server, "localhost", 9000)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
