# Python Stream Networking
# Streams are high-level async/await-ready primitives to work with 
# network connections. 
# Streams allow sending and receiving data without using callbacks 
# or low-level protocols and transports.
# Subprocesses
# This example describes high-level async/await asyncio APIs to create 
# and manage subprocesses.
# A demonstration of how asyncio can run a shell command and obtain its result:
 
import asyncio

async def run(cmd):

    proc = await asyncio.create_subprocess_shell(
        cmd,

        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')

    if stdout:
        print(f'[stdout]\n{stdout.decode()}')

    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

asyncio.run(run('ls /zzz'))
