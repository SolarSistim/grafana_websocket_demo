import asyncio
import random
import websockets
from random import randrange

async def handle_websocket(websocket, path):
    while True:

        current_number = randrange(100)
        increment = random.choice([-1, 1])
        value = random.randint(1, 10) * 5
        new_number = max(1, min(100, current_number + (increment * value)))
        current_number = new_number
        await websocket.send(str(current_number))
        await asyncio.sleep(0.5)

start_server = websockets.serve(handle_websocket, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
