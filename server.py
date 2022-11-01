import asyncio
import asyncws
import ssl

async def echo(websocket):
    while True:
        frame = await websocket.recv()
        if frame is None:
            break
        await websocket.send(frame)


ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.check_hostname = False
ssl_context.load_cert_chain('example.crt', 'example.key')

loop = asyncio.get_event_loop()
loop.set_debug(True)
server = loop.run_until_complete(
    asyncws.start_server(echo, '127.0.0.1', 8000, ssl=ssl_context))
try:
    print("Server started!")
    loop.run_forever()
except KeyboardInterrupt as e:
    server.close()
    loop.run_until_complete(server.wait_closed())
finally:
    loop.close()