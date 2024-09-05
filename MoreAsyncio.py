import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1, "This is task 1 not hello"))
    task2 = asyncio.create_task(
        say_after(2, "This is task 2 not hello"))

    print(f"Task 1: started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"Task 2: finished at {time.strftime('%X')}")

asyncio.run(main())