"""
https://www.hackerrank.com/contests/justcode/challenges/lru-implementtion

Given:
N: no of elements
S: max. capacity of cache
a[i]: N no. of integers

Output:
PF: No. of page faults.
State of LRU cache.

Page falut occures when the element is not found in the cache.
In LRU algo , the least recently elements is removed first when no free space is avalaible in cache.

Input Format

N: no of elements
S: max. capacity of cache
a[i]: N no. of integers
Constraints

N ,S & a[i] all are integers

Output Format
PF:page fault
elements in LRU cache.

Sample Input
10 4
1 2 3 2 5 3 4 5 8 9
Sample Output
7
9 8 5 4
Explanation
Initially cache will be empty.
1 _ _ _      1
2 1 _ _      2
3 2 1 _      3
2 3 1 _      3
5 2 3 1      4
3 5 2 1      4
4 3 5 2      5
5 4 3 2      5
8 5 4 3      6
9 8 5 4      7
therefore: pagefaults = 7. state : 9 8 5 4.

"""

from collections import OrderedDict


class LRU():
    def __init__(self, S:int) -> None:
        self.capacity = S
        self._cache = OrderedDict()  # {value:<whatever>}

    def process(self, N:int, data:list[int]) -> tuple[int,list[int]]:
        if N != len(data):
            raise ValueError(f"size of input data doesn't match {N}")
        pf = 0  # page-fault
        for d in data:
            if not self.cache(d):
                pf += 1
        state = [d for d in self._cache]
        state.reverse()
        return (pf, state)

    def cache(self, data:int) -> bool:
        if data in self._cache:  # hit
            self._cache.move_to_end(data, last=True)
            return True
        if len(self._cache) < self.capacity:
            self._cache[data] = True     # key=data, the value doesn't matter
        else:
            self._cache.popitem(last=False)
            self._cache[data] = True
        return False
            

def test():
    data = [
        ((10, 4, [1, 2, 3, 2, 5, 3, 4, 5, 8, 9]), (7,[9, 8, 5, 4])),
    ]
    result = ""
    for (N, S, d), (pf,state) in data:
        s = LRU(S)
        r1, r2 = s.process(N, d)
        if r1 != pf or r2 != state:
            result = "FAIL"
        else:
            result = "PASS"
        print(f"{result}, ({r1},{r2}), exp ({pf},{state})")


test()


