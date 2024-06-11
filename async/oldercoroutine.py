"""
an older way of marking a function as a coroutine is to decorate a normal def function with @asyncio.coroutine.
This construction has been outdated since the async/await syntax was put in place in Python 3.5.
These two coroutines are essentially equivalent (both are awaitable), 
 but the first is generator-based, while the second is a native coroutine:
"""
import asyncio

@asyncio.coroutine
def py34_coro():
    """Generator-based coroutine, older syntax"""
    yield from stuff()

async def py35_coro():
    """Native coroutine, modern syntax"""
    await stuff()
