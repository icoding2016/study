import asyncio
import aiohttp
from datetime import datetime
from functools import wraps


def atiming(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        print("-"*50)
        t1 = datetime.now()
        result = await func(*args, **kwargs)
        t = datetime.now() - t1
        print(f"execution time: {t} sec.")
        print("-"*50)
        return result
    return wrapper


async def sleep_and_print():
    print("[sleep_and_print] starting await..")
    await asyncio.sleep(1)
    print("[sleep_and_print] slept for 1 sec")
    await asyncio.sleep(1)
    print("[sleep_and_print] slept for 1 sec")
    await asyncio.sleep(5)
    print("[sleep_and_print] slept for 5 sec")
      

async def delayed_msg(n:int, msg:str):
    await asyncio.sleep(n)
    print(f"delay {n} sec before {msg}")


# asyncio.create_task() schedules the task in the event loop12.
# This means the task starts immediately
@atiming
async def test1():
    delays = [3, 5, 1, 4, 2, 7]
    tasks = []
    for d in delays:
        t = asyncio.create_task(delayed_msg(d, 'done'))
        tasks.append(t)
    print("starting tasks...")
    await asyncio.gather(*tasks)

# await <async func> means that the current function will not continue to the next line until t has completed.
# During this time, the event loop can run other tasks
@atiming
async def test2():
    delays = [3, 5, 1, 4, 2, 7]
    tasks = []
    await sleep_and_print()
    for d in delays:
        await delayed_msg(d, 'done')
    await sleep_and_print()

async def http_task(id:str, task_queue):
    async with aiohttp.ClientSession() as session:
        while task_queue:
            url = await task_queue.get()
            print(f"task {id}: get url {url}, ", end='')
            t1 = datetime.now()
            async with session.get(url) as rsp:
                await rsp.text()
            t = datetime.now() - t1
            print(f"spent {t} sec")

@atiming
async def test_http():
    urls = [
        "http://google.com",
        "http://linkedin.com",
        "https://github.com",
        "http://amazon.com.au",
        "https://leetcode.com",
    ]
    task_queue = asyncio.Queue()
    for url in urls:
        await task_queue.put(url)
    await asyncio.gather(
        asyncio.create_task(http_task("worker-1", task_queue)),
        asyncio.create_task(http_task("worker-2", task_queue)),
    )
    

async def main():
    print("### test1")
    await test1()
    print("### test2")
    await test2()
    print("### test_http")
    await test_http()


asyncio.run(main())