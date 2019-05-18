# Python Stream Networking
# Streams are high-level async/await-ready primitives to work with 
# network connections. 
# Streams allow sending and receiving data without using callbacks 
# or low-level protocols and transports.
# An example using the Process class to control a subprocess and the 
# StreamReader class to read from its standard output.
# The subprocess is created by the create_subprocess_exec() function:
 
import asyncio
import sys

async def get_date():

    code = 'import datetime; print(datetime.datetime.now())'

    # Create the subprocess; redirect the standard output
    # into a pipe.

    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', code,
        stdout=asyncio.subprocess.PIPE)

    # Read one line of output.

    data = await proc.stdout.readline()
    line = data.decode('ascii').rstrip()

    # Wait for the subprocess exit.

    await proc.wait()
    return line

if sys.platform == "win32":

    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy())

date = asyncio.run(get_date())

print(f"Current date: {date}")
