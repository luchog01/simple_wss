import asyncio
import asyncws
import ssl

msg = "Hello World"

async def echo(websocket):
    while True:
        print("Sent: ", msg)
        await websocket.send(msg)  # Send msg to server
        await asyncio.sleep(5)
        echo = await websocket.recv()  # Revice msg from server
        print("Recived: ", echo)
        if echo is None:
            break


ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
ssl_context.load_verify_locations('example.crt')

loop = asyncio.get_event_loop()
websocket = loop.run_until_complete(
    asyncws.connect('wss://localhost:8000', ssl=ssl_context))
try:
    loop.run_until_complete(echo(websocket))
except KeyboardInterrupt as e:
    loop.run_until_complete(websocket.close())
    loop.run_until_complete(websocket.wait_closed())
finally:
    loop.close()