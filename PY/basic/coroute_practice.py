import asyncio

async def beeper(interval:int=3):
    count = 0
    while True:
        try:
            await asyncio.sleep(interval)
            print('beep~')
            count += 1
        except asyncio.CancelledError:
            print('cancelling...')
            break
    return count

async def test():
    task = asyncio.create_task(beeper())
    group = asyncio.gather(task)
    await asyncio.sleep(11)
    # task.cancel()
    group.cancel()
    # print(group.result)

    
if __name__ == '__main__':
    asyncio.run(test())