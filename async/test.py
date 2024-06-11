#!/usr/bin/env python3
'''
you cannot use pythons await in a comprehension because that keyword
can only be used inside of an async def function's body.
asychnronous comprehensions are only allowed inside an async def func.
Just for fun, I tried defining an async def function to see 
if I could make my idea work
'''

import asyncio


async def test():
    return [i async for i in range(100) if % 2]


loop = asyncio.get_event_loop()
loop.run_until_complete(test())

