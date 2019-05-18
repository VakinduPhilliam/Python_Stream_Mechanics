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
# Watch a file descriptor for read events
# Wait until a file descriptor received some data using the loop.add_reader() 
# method and then close the event loop:
 
import asyncio
from socket import socketpair

# Create a pair of connected file descriptors

rsock, wsock = socketpair()

loop = asyncio.get_event_loop()

def reader():
    data = rsock.recv(100)

    print("Received:", data.decode())

    # We are done: unregister the file descriptor

    loop.remove_reader(rsock)

    # Stop the event loop

    loop.stop()

# Register the file descriptor for read event

loop.add_reader(rsock, reader)

# Simulate the reception of data from the network

loop.call_soon(wsock.send, 'abc'.encode())

try:

    # Run the event loop

    loop.run_forever()

finally:

    # We are done. Close sockets and the event loop.

    rsock.close()
    wsock.close()
    loop.close()
