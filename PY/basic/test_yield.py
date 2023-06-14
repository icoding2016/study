"""

[yield]
yield expression returns control to the whatever is using the generator. 
The generator pauses at this point, which means that the @contextmanager decorator knows that the code is done with the setup part.
In other words, everything you want to do in the context manager __enter__ phase has to take place before the yield.

Once your context exits (so the block under the with statement is done),
the @contextmanager decorator is called for the __exit__ part of the context manager protocol and will do one of two things:
- If there was no exception, it'll resume your generator. 
  So your generator unpauses at the yield line, and you enter the cleanup phase, the part
- If there was an exception, the decorator uses generator.throw() to raise that exception in the generator. 
  It'll be as if the yield line caused that exception. 
  If you have a finally clause, it'll be executed before your generator exits because of the exception.

e.g.
    import contextlib
    import time
    @contextlib.contextmanager
    def time_print(task_name):
        t = time.time()
        try:
            yield
        finally:
            print task_name, "took", time.time() - t, "seconds."

    def doproc():
        x=1+1

    with time_print("processes"):
        [doproc() for _ in range(500)]
    # processes took 15.236166954 seconds.

So, in above example the sequence is as follows:

- with time_print("processes"):
  This creates the context manager and calls __enter__ on that.
- The generator starts execution, t = time.time() is run.
- The yield expression pauses the generator, control goes back to the decorator.
  This takes whatever was yielded and returns that to the with statement, in case there is an as target part. 
  Here None is yielded (there is only a plain yield expression).
- [doproc() for _ in range(500)] is run and completes.
- The context manager __exit__ method is run, no exception is passed in.
- The decorator resumes the generator, it continues where it left off.
- The finally: block is entered and print task_name, "took", time.time() - t, "seconds." is executed.
- The generator exits, the decorator __exit__ method exits, all is done.


Q: When does the code after yield been executed? 
A: You can think of it as if the function which yields simply "pauses" when it comes across the yield.
   The next time you call it, it will resume after the yield keeping the state that it was in when it left.


[async generator]
https://www.python.org/dev/peps/pep-0525/




"""

import contextlib


num = 0

def gen_num():
    global num
    while num < 10:
        num += 1
        yield num
        print(f'after yield {num}')
    print(f'get out of loop from {num}.')

def test1():
    """the code after yield is executed when the generator is called the next round,
       which was paused at the first yield
    """
    try:
        for n in gen_num():
            print(n)
    except StopIteration:
        print('Done')



@contextlib.contextmanager
def gen1():
    try:
        print(f"gen1: setup 0.")
        yield "gen1 generated content"
    finally:
        print("gen1: cleanup")


def test_gen1():
    with gen1() as g1:
        print(g1)


# iterator
class NumGen1():
    def __init__(self, count:int = 1, start:int=None) -> None:
        self.start = start if start else 0
        self.count = count
        self.num = start
    
    def __iter__(self):
        return self

    #__next__ using return
    def __next__(self) -> int:
        if self.num < self.start + self.count - 1:
            self.num += 1
            return self.num
        else:
            raise StopIteration


# generator
def gen_num2(self, count:int = 1, start:int=None) -> None:
    start = start if start else 0
    for i in range(start, start+count):
        yield i



def test_num_gen():
    print([i for i in NumGen1(10, 0)])
    print([i for i in gen_num2(10, 10)])



print("=====test1=====")
test1()
print("=====test_gen1=====")
test_gen1()
print("=====test_num_gen=====")
test_num_gen()


######################
# async
import asyncio

class NumIter():
    seed: int = 0

    def __init__(self, count:int = 1, start:int=None) -> None:
        self.start = start if start else 0
        self.count = count
        self.num = self.start

    def __aiter__(self):
        return self

    # Note:  iterator does not use yield.. which is creating a generator.
    #   So below is a wrong way to do iterator
    async def wrong__anext__(self) -> None:
        while self.num < self.num + self.count:
            yield self.num
            self.num += 1
        raise StopAsyncIteration

    async def __anext__(self) -> int:
        if self.num < self.start + self.count:
            num = self.num
            self.num += 1
            return num
        raise StopAsyncIteration


async def test_a_NumIter():
    print("test NumIter")
    async for i in NumIter(count=10, start=30):
        print(i)


def anum_gen(count:int=1, start:int=0) -> None:
    num = start
    for i in range(count):
        #print(f"NumGen.__next__: before generate {num}")
        yield num
        num += 1
        #print(f"NumGen.__next__: after generate {num}")

async def test_a_gen():
    print("test_a_gen:  async generator")
    for i in anum_gen(10,100):
        print(i)
    print([i for i in anum_gen(10,200)])


async def main():
    await test_a_NumIter()
    await test_a_gen()

asyncio.run(main())



