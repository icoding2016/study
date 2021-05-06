# Implement async producer/consumer
# -- Async/await solution


import asyncio
import random


_MAX_QUEUE_SIZE = 20


class Product(object):
    _serial_num = 0
    def __init__(self, name: str):
        self.name = name
        self._serial_num += 1
        self.serial_num = self._serial_num


async def produce(name: str, q: asyncio.Queue, efficiency: int) -> None:
    if efficiency > 10:
        efficiency = 10
    elif efficiency < 1:
        efficiency = 1
    while True:
        try:
            producing_time = random.randint(1,11-efficiency)
            p = Product('CoolProduct')
            print(f'{name}: Producing {p.name}{p.serial_num} ... ', end='')
            await asyncio.sleep(producing_time)
            print('done.')
            print('Moving to storage ... ', end=' ')
            await q.put(p)
            print(f'done. in store: {q.qsize()}')
        except asyncio.CancelledError:
            break


async def consume(name: str, q: asyncio.Queue, efficiency: int) -> None:
    if efficiency > 10:
        efficiency = 10
    elif efficiency < 1:
        efficiency = 1

    while True:
        consuming_time = random.randint(1,11-efficiency)       
        print(f'{name}: Retrieving product, current in store {q.qsize()}...')
        try:
            p = q.get_nowait()
            print(f'Consuming {p.name}{p.serial_num} ... ', end='')
            print('done.')
        except asyncio.QueueEmpty: 
            print('skip.')
        except asyncio.CancelledError:
            break
        await asyncio.sleep(consuming_time)


async def main():
    q = asyncio.Queue(maxsize=_MAX_QUEUE_SIZE)
    producers = [asyncio.create_task(produce(name=f'P{i}', q=q, efficiency=4*i)) for i in range(1,3)]
    consumers = [asyncio.create_task(consume(name=f'C{i}', q=q, efficiency=i)) for i in range(1,5)]
    await asyncio.gather(
        *producers, 
        *consumers
        )

    await asyncio.sleep(60)
    for p in producers:
        p.cancel()
    for c in consumers:
        c.cancel()


if __name__ == '__main__':
    asyncio.run(main())