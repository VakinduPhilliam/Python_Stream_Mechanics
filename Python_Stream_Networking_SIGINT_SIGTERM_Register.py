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
# Set signal handlers for SIGINT and SIGTERM
# (This signals example only works on Unix.)
# Register handlers for signals SIGINT and SIGTERM using the 
# loop.add_signal_handler() method:
 
import asyncio
import functools
import os
import signal

def ask_exit(signame):

    print("got signal %s: exit" % signame)

    loop.stop()

async def main():

    loop = asyncio.get_running_loop()

    for signame in {'SIGINT', 'SIGTERM'}:

        loop.add_signal_handler(
            getattr(signal, signame),

            functools.partial(ask_exit, signame))

    await asyncio.sleep(3600)

print("Event loop running for 1 hour, press Ctrl+C to interrupt.")
print(f"pid {os.getpid()}: send SIGINT or SIGTERM to exit.")

asyncio.run(main())
