import asyncio
import time
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main2():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    await say_after(3, 'This is')
    await say_after(4, 'the asyncio import')
    await say_after(5, 'i really dont know what it does')
    await say_after(6, 'I am a boss')
    await say_after(7, 'oh its written in C btw')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main2())


