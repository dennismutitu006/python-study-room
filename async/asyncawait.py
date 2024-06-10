async def g():#a func that u introduce with async def is a coroutine-func
    '''
    this function may use await, return,or yield but all are optional.
    declaring async def noop(): pass is valis:
    using await and/ or return creates a coroutine function. to call a such a func 
    you must await it to get its results.
    you can only use yield in an async def block only in python.This creates an asynchronouse generetor,
    which you iterator over with async for.
    anything defined with async def may not use yield from, which will raise a syntax error.
    just like its a syntaxerr to use yield outside def func, it is a syntaxerr to use await 
    outside of an async def coroutine.
    '''
    # Pause here and come back to g() when f() is ready
    r = await f()
    return r
'''
The syntax async def introduces either a native coroutine or an asynchronous generator. The expressions async with and async for are also valid, and you’ll see them later on.

The keyword await passes function control back to the event loop. (It suspends the execution of the surrounding coroutine.) If Python encounters an await f() expression in the scope of g(), this is how await tells the event loop, “Suspend execution of g() until whatever I’m waiting on—the result of f()—is returned. In the meantime, go let something else run.”
'''

