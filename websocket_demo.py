import asyncio
import websockets
import random
import time

async def handle_client(websocket, path):
    while True:
        timestamp = time.time()
        message = random.randint(1, 100)
        timestamp = str(timestamp)
        message = str(message)
        await websocket.send('{"timestamp": ' + '"' + timestamp + '", "message": "' + message + '"}')
        await asyncio.sleep(1)
start_server = websockets.serve(handle_client, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
