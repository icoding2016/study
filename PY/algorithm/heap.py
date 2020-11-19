# Heap is a 'tree' based data structure
# Max Heap -- A complete binary tree that each node >= its descendants
# Min Heap -- A complete binary tree that each node <= its descendants
# Heap data structure is mainly used to represent a priority queue.
# 
# The implementation is by a 'queue'
# In Python, it is available using “heapq” module. (methods: 'heapify', 'heappop', 'heappush', 'merge', 'nlargest', 'nsmallest'...) 
#
# For a zero-based Array, the parent is located at position (n-1)/2 (floored)
# - Arr[(i -1) / 2] returns its parent node.
# - Arr[(2 * i) + 1] returns its left child node.
# - Arr[(2 * i) + 2] returns its right child node.

import heapq
import copy
from typing import TypeVar


T = TypeVar('T')


class MaxHeapQueue(object):
    def __init__(self, data:list[T]=None) -> None:
        self._queue = []
        if None != data:
            self.heapify(data)

    def create(self, data:list[T]) -> list[T]:
        '''Create Heap (from Top root to bottom). 
           Internal heap queue will be generated and returned.
           O(NlogN)
        '''
        self._queue = copy.deepcopy(data)
        i = 1
        while i < len(self._queue):
            loc = i
            pi = int((loc-1)/2)  # parent index
            while loc > 0:
                if self._queue[loc] <= self._queue[pi]:
                    break
                self._queue[loc], self._queue[pi] = self._queue[pi], self._queue[loc]
                #print('swap {},{}'.format(self._queue[loc], self._queue[pi]))
                loc = pi
                pi = int((loc-1)/2)
            i += 1
        return self._queue

    # Heapify
    # Heapify process the element backwards from bottom to top, for each element, swap down if needed.
    # O(N)
    def heapify(self, data:list[T]) -> list[T]:
        '''Heapify. 
           Modify the input list in place.
           Also create new internal heap queue.
           O(N)
        '''
        L = len(data)
        cur = int((L -2)/2)
        # process backwards one by one, from L/2
        while cur >= 0:
            pi = cur
            while pi < L - 1:
                li = 2 * pi + 1 if (2 * pi + 1) < L else None
                ri = 2 * pi + 2 if (2 * pi + 2) < L else None
                if not li:
                    break
                if not ri:
                    i = li
                else:
                    i = li if data[li] >= data[ri] else ri
                if data[i] > data[pi]:
                    data[i], data[pi] = data[pi], data[i]
                pi = i
            cur -= 1
        self._queue = copy.deepcopy(data)


    def push(self, data:T) -> None:
        self._queue.append(data)
        loc = len(self._queue) - 1
        if loc < 1:     # 1 element
            return
        pi = int((loc-1)/2)
        while loc > 0 and self._queue[loc] > self._queue[pi]:
            self._queue[loc], self._queue[pi] = self._queue[pi], self._queue[loc]
            loc = pi
            pi = int((loc-1)/2)

    # Heap Pop:
    #   1) Pop the root, 
    #   2) Fill root with tail element. 
    #   3) Swap root down
    def pop(self) -> T:
        if not self._queue:
            return None
        L = len(self._queue)
        data = self._queue[0]
        self._queue[0] = self._queue[-1]
        pi = 0
        while pi <= L - 1:
            li = pi*2+1
            ri = pi*2+2
            if li > L-1:
                return data
            if ri > L - 1:
                self._queue[pi] = self._queue[li]
                return data
            i = li if self._queue[li] >= self._queue[ri] else ri
            self._queue[pi] = self._queue[i]
            pi = i
        self._queue = self._queue[:-1]
        return data

    def __len__(self):
        return len(self._queue)

    def __str__(self):
        return self._queue.__str__()

    def show(self):
        lvl = 0
        count = 0
        for i in range(len(self._queue)):
            print(self._queue[i], end=', ')
            count += 1
            if count == 2**lvl:
                print('')
                lvl += 1
                count = 0
        print('')


class MinHeapQueue(object):
    def __init__(self, data:list[T]=None) -> None:
        self._queue = []
        if None != data:
            self.heapify(data)

    # Create Heap (from Top root to bottom)
    # O(NlogN)    for each in the N loop, log(N) swap in worst case. 
    def create(self, data:list[T]) -> list[T]:
        '''Create Heap (from Top root to bottom). O(NlogN)'''
        self._queue = data.copy()
        i = 1
        for i in range(1, len(self._queue)):
            loc = i
            pi = int((loc-1)/2)
            while loc > 0 and self._queue[loc] < self._queue[pi]:
                self._queue[loc], self._queue[pi] = self._queue[pi], self._queue[loc]
                loc = pi
                pi = int((loc - 1)/2)
        return self._queue

    # Heapify
    # O(N)
    def heapify(self, data:list[T]) -> list[T]:
        if not data:
            self._queue = data
            return data
        L = len(data)
        cur = int((L-2)/2)
        while cur >= 0:
            pi = cur
            while pi < L - 1:
                li = pi * 2 + 1 if (pi * 2 + 1)<L else None
                ri = pi * 2 + 2 if (pi * 2 + 2)<L else None
                if not li:
                    break
                if not ri:
                    i = li
                else:
                    i = li if data[li] < data[ri] else ri
                if data[i] < data[pi]:
                    data[i], data[pi] = data[pi], data[i]
                    pi = i
                else:
                    break
            cur -= 1
        self._queue = copy.deepcopy(data)
        return data

    def push(self, data:T) -> list[T]:
        self._queue.append(data)
        cur = len(self._queue) - 1
        while cur > 0:
            pi = int((cur-1)/2)
            if self._queue[cur] < self._queue[pi]:
                self._queue[cur], self._queue[pi] = self._queue[pi], self._queue[cur]
                cur = pi
            else:
                break
        return self._queue

    def pop(self) -> T:
        if not self._queue:
            return None
        data = self._queue[0]
        L = len(self._queue)
        self._queue[0] = self._queue[L-1]
        pi = 0
        while pi < L - 1:
            li = pi * 2 + 1 if (pi * 2 + 1)<L else None
            ri = pi * 2 + 2 if (pi * 2 + 2)<L else None
            if not li:
                break
            if not ri:
                i = li
            else:
                i = li if self._queue[li] < self._queue[ri] else ri
            if self._queue[pi] > self._queue[i]:
                self._queue[pi], self._queue[i] = self._queue[i], self._queue[pi]
                pi = i
            else:
                break
        self._queue.pop()
        #self.show()  ##
        return data

    def __len__(self):
        return len(self._queue)

    def __str__(self):
        return self._queue.__str__()


    def show(self):
        lvl = 0
        count = 0
        for i in range(len(self._queue)):
            print(self._queue[i], end=', ')
            count += 1
            if count == 2**lvl:
                print('')
                lvl += 1
                count = 0
        print('')


# T(NlogN)  - CreatHeap use heapiify - O(N), pop all the N elements:  N * O(logN)
def heap_sort(data:list[T]) -> list[T]:
    if len(data) <= 1:
        return data
    hp = MinHeapQueue(data)
    print(hp)
    hp.show()
    i = 0
    while len(hp) > 0:
        data[i] = hp.pop()
        i += 1
    return data





def test():
    # python build-in heapq
    ll = [3,5,7,1,9,2,4,8,0,6]
    heapq.heapify(ll)
    print(ll)

    # MaxHeapQueue
    print('MaxHeapQueue')
    maxhq = MaxHeapQueue()
    maxhq.create(ll)
    print(maxhq)
    maxhq1 = MaxHeapQueue()
    maxhq1.heapify(ll)
    print(maxhq1)
    maxhq1.show()
    print('- push 8')
    maxhq.push(8)
    print(maxhq)
    print('- push 15')
    maxhq.push(15)
    print(maxhq)
    print('pop: {}'.format(maxhq.pop()))
    print(maxhq)
    print('pop: {}'.format(maxhq.pop()))
    print(maxhq)
    print('pop: {}'.format(maxhq.pop()))
    print(maxhq)


    # MinHeapQueue
    print('MinHeapQueue')
    ll = [3,5,7,1,9,2,4,8,0,6]
    minhq = MinHeapQueue(ll)
    print(minhq)
    print(minhq.show())
    minhq1 = MinHeapQueue()
    minhq1.create(ll)
    print(minhq1)
    minhq1.show()
    
    print('- push 15')
    minhq.push(15)
    print(minhq)
    minhq.push(3)
    print(minhq)
    minhq.show()
    while len(minhq):
        print(minhq.pop(), end=', ')
    print('')
    
    # heap_sort
    print('heap sort')
    ll = [7,3,5,7,1,9,2,4,8,10,0,6]
    print(ll, ' ->')
    print(heap_sort(ll))

test()    