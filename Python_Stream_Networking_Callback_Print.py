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
# An example using the loop.call_soon() method to schedule a callback. 
# The callback displays "Hello World" and then stops the event loop:
 
import asyncio

def hello_world(loop):
    """A callback to print 'Hello World' and stop the event loop"""
    print('Hello World')

    loop.stop()

loop = asyncio.get_event_loop()

# Schedule a call to hello_world()

loop.call_soon(hello_world, loop)

# Blocking call interrupted by loop.stop()

try:
    loop.run_forever()

finally:
    loop.close()
