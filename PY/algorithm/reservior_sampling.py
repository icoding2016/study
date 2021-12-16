"""
蓄水池采样算法（Reservoir Sampling）

Question:
“给出一个数据流，这个数据流的长度很大或者未知。并且对该数据流中数据只能访问一次。
请写出一个随机选择算法，使得数据流中所有数据被选中的概率相等。”

Algorithm:
假设需要采样的数量为 k 。
首先构建一个可容纳 k 个元素的数组，将序列的前 k 个元素放入数组中。
然后对于第 j （j>k）个元素开始，以 k/j 的概率来决定该元素是否被替换到数组中（从数组的k个元素中随机挑选一个进行替换 -- k 个元素被替换的概率是相同的1/k）。 
当遍历完所有元素之后，数组中剩下的元素即为所需采取的样本。

原文链接：https://blog.csdn.net/anshuai_aw1/article/details/88750673


Apply the algorithm at ReserviorSampling._sampling

"""


import asyncio
from asyncio.exceptions import CancelledError
import random
import threading
import time
from typing import Awaitable



class StreamRandNumError(Exception):
    pass

class StreamRandNum(object):
    def __init__(self, low:int, high:int) -> None:
        super().__init__()
        if high < low:
            raise StreamRandNumError('Input high boundary smaller than low boundary')
        self.low = low
        self.high = high

    def read(self) -> int:
        return random.randint(self.low, self.high)

    def __next__(self) -> int:
        return random.randint(self.low, self.high)

    def __iter__(self):
        return self

# thead implementation (sync mode)
class ReserviorSampling(threading.Thread):
    SAMPLE_INTERVAL = 1  # sec

    def __init__(self, K:int, stream:StreamRandNum) -> None:
        super().__init__()
        self.K = K
        self.stream = stream
        self.samples = []
        self.count = 0
        self.lock = threading.Semaphore()
        self.active = True

    def _sampling(self) -> None:
        data = self.stream.read()
        self.count += 1
        if len(self.samples) < self.K:
            self.samples.append(data)
        else:
            if random.randint(1, self.count) <= self.K:    # choose the new data
                i = random.randint(0, self.K-1)            # Randomly pick one of the K samples
                self.samples[i] = data

    def sampling(self) -> None:
        self.lock.acquire()
        self._sampling()
        self.lock.release()

    def get_sample(self) -> list[int]:
        self.lock.acquire()
        sample = self.samples[:]
        self.lock.release()
        return sample

    def run(self) -> None:
        while self.active:
            self.sampling()
            time.sleep(self.SAMPLE_INTERVAL)
        print('Sampling end.')

    def stop(self) -> None:
        self.active = False
        print('Stopping sampling.')


def reservior_sampling():
    stream = StreamRandNum(1, 100)
    rs = ReserviorSampling(10, stream)
    rs.start()
    for i in range(30):
        print(rs.get_sample())
        time.sleep(random.randint(1,10))
    rs.stop()

# async mode implementation
class AReserviorSampling(object):
    SAMPLE_INTERVAL = 1  # sec

    def __init__(self, K:int, stream:StreamRandNum) -> None:
        super().__init__()
        self.K = K
        self.stream = stream
        self.samples = []
        self.count = 0
        self.lock = asyncio.Lock()

    def _sampling(self) -> None:
        data = self.stream.read()
        self.count += 1
        if len(self.samples) < self.K:
            self.samples.append(data)
        else:
            if random.randint(1, self.count) <= self.K:    # choose the new data
                i = random.randint(0, self.K-1)            # Randomly pick one of the K samples
                self.samples[i] = data

    async def sampling(self) -> Awaitable:
        await self.lock.acquire()
        self._sampling()
        self.lock.release()

    async def get_sample(self) -> Awaitable[list[int]]:
        await self.lock.acquire()
        print(self.samples, end=' ,')
        sample = self.samples[:]
        print(sample)
        self.lock.release()
        return sample

    async def run(self) -> Awaitable:
        while True:
            try:
                await self.sampling()
                await asyncio.sleep(self.SAMPLE_INTERVAL)
            except asyncio.CancelledError:
                print('Sampling end.')
                break


async def areservior_sampling(ars:AReserviorSampling) -> Awaitable:
    stream = StreamRandNum(1, 200)
    ars = AReserviorSampling(10, stream)
    for i in range(20):
        sample = await ars.get_sample()
        print(sample)
        await asyncio.sleep(random.randint(1,5))
    


def test():
    reservior_sampling()

async def test_as():
    stream = StreamRandNum(1, 200)
    ars = AReserviorSampling(10, stream)
    arst = asyncio.create_task(ars.run())
    arsc = asyncio.create_task(areservior_sampling(ars))
    group = asyncio.gather(arst, arsc)
    await asyncio.sleep(30)
    group.cancel()        

# test()

asyncio.run(test_as())

