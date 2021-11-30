import asyncio
import json


async def load_data(url):
    try:
        REQ = json.loads(str(url))
    except:
        return "Json is not readable"

    data = REQ.get('data')

    if data:
        REQ['data'] = dict()
    else:
        return REQ

    for i in data.split('%%'):
        sp = i.split('&&')
        REQ['data'].update({sp.pop(0): {sp.pop(0): sp.pop(0) for _ in range(len(sp) // 2)}})
    return json.dumps(REQ)


async def handle_echo(reader, writer):
    data = await reader.read(500)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print("Received %r from %r" % (message, addr))

    message = await load_data(message)
    print("Send: %r" % str(message))

    writer.write(str(message).encode())
    await writer.drain()

    print("Close the client socket")
    writer.close()


loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, '127.0.0.1', 8888, loop=loop)

server = loop.run_until_complete(coro)
# Serve requests until Ctrl+C is pressed

print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
