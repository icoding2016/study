# The producer–consumer problem (also known as the bounded-buffer problem) is a classic example of a multi-process synchronization problem 
# The problem describes two processes, the producer and the consumer, who share a common, fixed-size buffer used as a queue. 
# The producer's job is to generate data, put it into the buffer, and start again. 
# At the same time, the consumer is consuming the data (i.e., removing it from the buffer), one piece at a time. 
# The problem is to make sure that the producer won't try to add data into the buffer if it's full and that the consumer won't try to remove data from an empty buffer.
# We can solve this problem by using semaphores.

# Python通过两个标准库thread和threading提供对线程的支持。
# thread提供了低级别的、原始的线程以及一个简单的锁。
# threading 模块提供的其他方法

import threading
import time
import random


BUF_SIZE = 10
buf_counter = 0                 # current filled count in buf
sem_access = threading.Semaphore(1)

sem_buf_free = threading.Semaphore(BUF_SIZE)
sem_buf_used = threading.Semaphore(0)


def produce():
    # produce_onelock()
    produce_3locks()

def produce_onelock():
    global BUF_SIZE
    global buf_counter
    global sem_access

    # sem_access.acquire(blocking=True)        # use 'with statement'
    with sem_access:
        if buf_counter < BUF_SIZE:
            buf_counter += 1
            print("produce +1, now {}".format(buf_counter))
        else:
            print("product: too many.. skip")
    # sem_access.release()

def produce_3locks():
    global sem_access
    global sem_buf_free
    global sem_buf_used

    with sem_access:
        if sem_buf_free.acquire(blocking=False):
            sem_buf_used.release()
            print("produce +1, now {}".format(sem_buf_used._value))
        else:
            print('produce skip, (queue full).')

def consume():
    # consume_onelock()
    consume_3locks()

def consume_onelock():
    global buf_counter
    global sem_access

    # sem_access.acquire(blocking=True)
    with sem_access:
        if buf_counter > 0:
            buf_counter -= 1
            print("consume -1, now {}".format(buf_counter))
        else:
            print("consume: no product.. give up")
    # sem_access.release()

def consume_3locks():
    global sem_access
    global sem_buf_free
    global sem_buf_used

    with sem_access:
        if sem_buf_used.acquire(blocking=False):
            sem_buf_free.release()
            print("consume -1, now {}".format(sem_buf_used._value))
        else:
            print('consume skip, (empty queue).')


class Producer(threading.Thread):
    def __init__(self, name=None, efficiency=5):
        threading.Thread.__init__(self)
        self.name = name if name else 'Producer'
        self.cr_section = threading.Lock()     # the Lock has no use (it's per object)
        self._active = True
        if efficiency >= 9:
            self.efficiency = 9
        elif efficiency < 1:
            self.efficiency = 1
        else:
            self.efficiency = efficiency
        print(f"Producer {self.name} is available")

    def run(self):
        global produce
        while(self._active):
            self.cr_section.acquire()
            produce()
            self.cr_section.release()
            time.sleep(random.random()*(10-self.efficiency))
        print(f'Producer {self.name} stopped.')

    def stop(self):
        self._active = False


class Consumer(threading.Thread):
    def __init__(self, name=None, efficiency=5):
        threading.Thread.__init__(self)
        self.name = name if name else 'Consumer'
        self.cr_section = threading.Lock()
        self._active = True
        if efficiency >= 9:
            self.efficiency = 9
        elif efficiency < 1:
            self.efficiency = 1
        else:
            self.efficiency = efficiency
        print(f"Consumer {self.name} is available")

    def run(self):
        global consume
        while(self._active):
            self.cr_section.acquire()
            consume()
            self.cr_section.release()
            time.sleep(random.random()*(10-self.efficiency))
        print(f'Consumer {self.name} stopped.')

    def stop(self):
        self._active = False


if __name__ == "__main__":
    _ = input('Press Enter to start the producer-consumer. (Press Enter again to stop).')

    P1 = Producer('P1', efficiency=5)
    P2 = Producer('P2', efficiency=3)
    C1 = Consumer('C1', efficiency=3)
    C2 = Consumer('C2', efficiency=4)
    C3 = Consumer('C3', efficiency=2)
    P1.start()
    P2.start()
    C1.start()
    C2.start()
    C3.start()

    _ = input('')
    P1.stop()
    P2.stop()
    C1.stop()
    C2.stop()
    C3.stop()

