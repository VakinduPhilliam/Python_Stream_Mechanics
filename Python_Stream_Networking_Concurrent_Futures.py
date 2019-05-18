# Python Stream Networking
# Streams are high-level async/await-ready primitives to work with 
# network connections. 
# Streams allow sending and receiving data without using callbacks 
# or low-level protocols and transports.
# Event Loop
# The event loop is the core of every asyncio application. 
# Event loops run asynchronous tasks and callbacks, perform network 
# IO operations, and run subprocesses.
# Application developers should typically use the high-level asyncio 
# functions, such as asyncio.run(), and should rarely need to reference 
# the loop object or call its methods. This section is intended mostly 
# for authors of lower-level code, libraries, and frameworks, who need 
# finer control over the event loop behavior.
# Executing code in thread or process pools

import asyncio
import concurrent.futures

def blocking_io():

    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.

    with open('/dev/urandom', 'rb') as f:
        return f.read(100)

def cpu_bound():

    # CPU-bound operations will block the event loop:
    # in general it is preferable to run them in a
    # process pool.

    return sum(i * i for i in range(10 ** 7))

async def main():
    loop = asyncio.get_running_loop()

    ## Options:

    # 1. Run in the default loop's executor:

    result = await loop.run_in_executor(
        None, blocking_io)

    print('default thread pool', result)

    # 2. Run in a custom thread pool:

    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, blocking_io)

        print('custom thread pool', result)

    # 3. Run in a custom process pool:

    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool, cpu_bound)

        print('custom process pool', result)

asyncio.run(main())
