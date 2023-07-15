"""
Multi-threading in 2 ways: 
- threading
- async/await

"""


##############
# Multi-threading with theading
##############
from time import sleep
from threading import Thread, Lock
from concurrent.futures import ThreadPoolExecutor


lock=Lock()
data=0
run_flag = True

def task1():
    global data
    while run_flag:
        lock.acquire()
        data += 1
        print(f"task1: data++ -> {data}")
        lock.release()
        sleep(1)

def task2():
    global data
    while run_flag:
        with lock:
            data -= 1
            print(f"task2: data-- -> {data}")
        sleep(1)

def test():
    global run_flag
    thread1 = Thread(target=task1)
    thread2 = Thread(target=task2)
    thread1.start()
    thread2.start()
    sleep(5)
    run_flag = False
    thread1.join()
    thread2.join()

def test2():
    global run_flag
    pool = ThreadPoolExecutor(max_workers=3)
    pool.submit(task1)
    pool.submit(task2)
    sleep(5)
    run_flag = False
    pool.shutdown(wait=True)

#test()
test2()

##############
# Multi-threading with async/await
#
# atest() and atest1() run the 2 tasks in parallel, using different method: asyncio.gather(), asyncio.create_task()
# atest2() doesn't run the 2 tasks in parallel. Why?
#   In the atest() function, await atask1() first starts. it encounters 'await asyncio.sleep(5)', which suspends atask1() for 5 seconds.
#   During this waiting period, the event loop is free to switch to other tasks.
#   But since 'await atask2()' is not reached until atask1() completes, the execution of atask2() is delayed until atask1() finishes waiting.
# 
##############

import asyncio

async def atask1():
    print("start a-task1")
    await asyncio.sleep(5)
    print("stop a-task1")

async def atask2():
    print("start a-task2")
    await asyncio.sleep(6)
    print("stop a-task2")


###
async def atest():
    """
    run atask1/2 in parallel, 
    output:
        start a-task1
        start a-task2
        stop a-task1
        stop a-task2
    """
    await asyncio.gather(atask1(), atask2())

async def atest1():
    """
    run atask1/2 in parallel, 
    output:
        start a-task1
        start a-task2
        stop a-task1
        stop a-task2
    """
    t1 = asyncio.create_task(atask1())
    t2 = asyncio.create_task(atask2())
    await t1
    await t2
    #

async def atest2():
    """
    run atask1/2 NOT in parallel, 
    output:
        start a-task1
        stop a-task1
        start a-task2
        stop a-task2
    """
    await atask1()
    await atask2()

asyncio.run(atest())

