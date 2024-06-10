async def g():
    # Pause here and come back to g() when f() is ready
    r = await f()
    return r
'''
The syntax async def introduces either a native coroutine or an asynchronous generator. The expressions async with and async for are also valid, and you’ll see them later on.

The keyword await passes function control back to the event loop. (It suspends the execution of the surrounding coroutine.) If Python encounters an await f() expression in the scope of g(), this is how await tells the event loop, “Suspend execution of g() until whatever I’m waiting on—the result of f()—is returned. In the meantime, go let something else run.”
'''

