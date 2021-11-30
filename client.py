import asyncio


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    print('Send: %r' % message)
    writer.write(message.encode())

    data = await reader.read()
    print('Received: %r' % data.decode())
    print('Close the socket')
    writer.close()

while True:
    # message = input('>>> ')
    message = '{"request_id":"01","data":"First&&name&&Tim&&old&&23&&name1&&Yel&&old1&&19&&old2&&1%%Second&&name&&Bob&&old3&&11&&name1&&Tim&&old1&&23&&name2&&Yel&&old2&&19"}'
    if message:
        break

loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(message))
loop.close()
