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
sem_buf = threading.Semaphore(1)


def produce():
    global BUF_SIZE
    global buf_counter
    global sem_buf

    sem_buf.acquire(blocking=True)
    if buf_counter < BUF_SIZE:
        buf_counter += 1
        print("produce +1, now {}".format(buf_counter))
    else:
        print("product: too many.. skip")
    sem_buf.release()
    
def consume():
    global buf_counter
    global sem_buf

    sem_buf.acquire(blocking=True)
    if buf_counter > 0:
        buf_counter -= 1
        print("consume +1, now {}".format(buf_counter))
    else:
        print("consume: no product.. give up")
    sem_buf.release()


class Producer(threading.Thread):
    def __init__(self, efficiency=5):
        threading.Thread.__init__(self)
        self.name = 'Producer'
        self.cr_section = threading.Lock()
        if efficiency >= 9:
            self.efficiency = 9
        elif efficiency < 1:
            self.efficiency = 1
        else:
            self.efficiency = efficiency
        print("Producer is available")

    def run(self):
        global produce
        while(True):
            self.cr_section.acquire()
            produce()
            self.cr_section.release()
            time.sleep(random.random()*(10-self.efficiency))
    
class Consumer(threading.Thread):
    def __init__(self, efficiency=5):
        threading.Thread.__init__(self)
        self.name = 'Consumer'
        self.cr_section = threading.Lock()
        if efficiency >= 9:
            self.efficiency = 9
        elif efficiency < 1:
            self.efficiency = 1
        else:
            self.efficiency = efficiency
        print("Consumer is available")

    def run(self):
        global consume
        while(True):
            self.cr_section.acquire()
            consume()
            self.cr_section.release()
            time.sleep(random.random()*(10-self.efficiency))


if __name__ == "__main__":
    P = Producer(efficiency=5)
    C = Consumer(efficiency=5)
    P.start()
    C.start()



