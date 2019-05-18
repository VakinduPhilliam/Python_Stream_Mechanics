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
# An example of a callback displaying the current date every second. 
# The callback uses the loop.call_later() method to reschedule itself 
# after 5 seconds, and then stops the event loop:
 
import asyncio
import datetime

def display_date(end_time, loop):

    print(datetime.datetime.now())

    if (loop.time() + 1.0) < end_time:
        loop.call_later(1, display_date, end_time, loop)

    else:
        loop.stop()

loop = asyncio.get_event_loop()

# Schedule the first call to display_date()

end_time = loop.time() + 5.0
loop.call_soon(display_date, end_time, loop)

# Blocking call interrupted by loop.stop()

try:
    loop.run_forever()

finally:
    loop.close()
