"""
multiprocessing
Using multiple processes instead of threads can avoid the GIL impact in the case of multi-core.
Each Python process gets its own Python interpreter and memory space so the GIL won’t be a problem


"""

from multiprocessing import Process, Lock, Pool
from itertools import product, permutations
from time import time, sleep

gcount = 10000000
gnum = 0
glock = Lock()
keep_running = True

def countdown(n):
    while n > 0:
        n -= 1

def numbering(name:str='', v:int=1, doze:int=1):
    global gnum, glock
    while keep_running:
        with glock:
            gnum += v
            print(f"{name}: {gnum}")
            sleep(doze)
    

def single_countdown():
    global gcount
    init_value = gcount

    start = time()
    countdown(gcount)
    stop = time()
    print(f"single_countdown {gcount} takes: {stop-start}")

def multi_countdown1(pal:int=4):
    global gcount
    procs = [Process(target=countdown, args=(gcount,)) for _ in range(pal)]
    print(procs)
    print(gcount)
    start = time()
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    # map(lambda x:x.start(), procs)
    # map(lambda x:x.join(), procs)
    stop = time()
    print(gcount)
    print(f"multi_countdown {gcount} takes: {stop-start}")

def multi_countdown(pal:int=2):
    global gcount
    start = time()
    with Pool(processes=2) as mp:
        mp.map(countdown, (gcount,))
    stop = time()
    print(gcount)
    print(f"multi_countdown {gcount} takes: {stop-start}")
        
def multi_numbering(pal:int=2):
    global keep_running
    with Pool(processes=pal) as mp:
        # result = mp.map(numbering, (1, 1))
        result = mp.map_async(numbering, ('worker', 1,1))
        result.wait(timeout=10)
        r = result.get() 
    sleep(5)
    # keep_running = False
    mp.join()
    # mp.close()    # or mp.terminate()

def test_mp():
    global gcount
    single_countdown()
    gcount = 10000000
    multi_countdown()
    #
    print('multi_numbering')
    multi_numbering()



def combine_words(w1, w2) -> str:
    return ' '.join([w1,w2])

def test_mp2():
    words = [''.join(x) for x in permutations([chr(x) for x in range(ord('a'), ord('z')+1)], 2)]
    print(len(words))
    with Pool(3) as mp:
        result = mp.starmap(combine_words, product(words, repeat=2))
        mp.close()
        mp.join()
    print(result)
    print(len(result))

# test()   
# Note: this will cause error "An attempt has been made to start a new process before the current process has finished its bootstrapping phase."
#       if not running it in if __name__ == '__main__'
#       You need to insert an if __name__ == '__main__': guard in the main module to avoid creating subprocesses recursively. 

if __name__ == "__main__":
    # test_mp()
    test_mp2()