# Python Stream Networking
# Streams are high-level async/await-ready primitives to work with 
# network connections. 
# Streams allow sending and receiving data without using callbacks 
# or low-level protocols and transports.
# This example is of a TCP echo client written using asyncio streams:
 
import asyncio

async def tcp_echo_client(message):

    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')

    writer.write(message.encode())

    data = await reader.read(100)

    print(f'Received: {data.decode()!r}')

    print('Close the connection')

    writer.close()

    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello World!'))
