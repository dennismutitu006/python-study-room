#!/usr/bin/env python3
# countasync.py

import asyncio  #for async/await syntax

async def count():#an async function that prints one and waits for 1 sec then prints two.
    print("One")
    await asyncio.sleep(1)#makes the function pause for one sec without blocking async tasks.
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())#to run 3 instances of the count func concurrently
    '''
    asyncio.gather(...): This function is used to run multiple asynchronous operations concurrently and wait for all of them to finish.
    '''

if __name__ == "__main__":#Ensures that the script runs only when executed directly not when imported as a module.
    import time #module for working with time-related functions.
    s = time.perf_counter()#measures how long the script takes to exec
    asyncio.run(main())
    elapsed = time.perf_counter() - s#calculates the elapsed tim by subtracting the start time from the current time.
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

    """
    How It Works
When the script runs, it starts by recording the current time.
The main function is then executed, which in turn calls asyncio.gather(count(), count(), count()) to start three count tasks concurrently.
Each count task prints "One", sleeps for one second, and then prints "Two".
Since these tasks run concurrently, they all start at the same time and complete roughly after one second.
After all tasks are finished, the script calculates and prints the total elapsed time.
"""
