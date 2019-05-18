# Python Stream Networking
# Streams are high-level async/await-ready primitives to work with 
# network connections. 
# Streams allow sending and receiving data without using callbacks 
# or low-level protocols and transports.
# asyncio — Asynchronous I/O
# asyncio is a library to write concurrent code using the async/await syntax.
# asyncio is used as a foundation for multiple Python asynchronous frameworks 
# that provide high-performance network and web-servers, database connection 
# libraries, distributed task queues, etc.
# asyncio is often a perfect fit for IO-bound and high-level structured network 
# code.

import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+

asyncio.run(main())
 