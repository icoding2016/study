"""
Merge two sorted lists of intervals


Given A and B, which are two interval lists. 
A has no overlap inside A and B has no overlap inside B. 
In A, the intervals are sorted by their starting points. 
In B, the intervals are sorted by their starting points. 
How do you merge the two interval lists and output the result with no overlap?

Here is an example:
A: [1,5], [10,14], [16,18]
B: [2,6], [8,10], [11,20]
The output:
[1,6], [8, 20]


Ideas:
1. One method is to concatenate the two lists, sort by the starting point,
   and apply merge intervals as discussed at https://www.geeksforgeeks.org/merging-intervals/.
2. Since the 2 list are alredy sorted. We just to through the 2 list, pick the smaller-start each time,
   and check if the new interval (s1, e1) overlap current merged interval (s0, e0).
   if s1 <= e0  -- overlap, extend current merged interval to max(e0, e1)
   if s1 > e0   that means current interval is already a separate one, then log it to result, 
                and take (s1,e1) as (s0,e0) and continue.
Idea 2 is more efficent since it doesn't need sort  (make use of the sorted list)

"""

from collections import deque
from typing import List
from utils.testtools import test_fixture


# O(M+N)   M=len(l1), N=len(l2)
# better in efficient
def merge_sorted_interval(l1:List[List[int]], l2:List[List[int]]) -> List[List[int]]:
    result = []
    cur_open = cur_close = None
    p1 = p2 = 0
    while p1 < len(l1) or p2 < len(l2):
        if cur_open == None:
            if p1 >= len(l1):
                cur_open, cur_close = l1[p2][0], l1[p2][1]
            elif p2 >= len(l2):
                cur_open, cur_close = l1[p1][0], l1[p1][1]
            elif l1[p1][0] < l2[p2][0]:
                cur_open, cur_close = l1[p1][0], l1[p1][1]
            else:
                cur_open, cur_close = l2[p2][0], l2[p2][1]
        else:
            if p1 >= len(l1):
                closer = l2[p2]
                p2 += 1
            elif p2 >= len(l2):
                closer = l1[p1]
                p1 += 1
            elif l1[p1][0] < l2[p2][0]:
                closer = l1[p1]
                p1 += 1
            else:
                closer = l2[p2]
                p2 += 1

            if closer[0] <= cur_close:  #overlap
                cur_close = max(cur_close, closer[1])
            else:
                result.append([cur_open, cur_close])
                cur_open, cur_close = closer[0], closer[1]
    if cur_open:
        result.append([cur_open, cur_close])
    return result


# T((M+N)log(M+N))           T(M+N) + T((M+N)log(M+N)) + T(M+N)
def merge_sorted_interval2(l1:List[List[int]], l2:List[List[int]]) -> List[List[int]]:
    result = []
    time_points = {}
    p1 = p2 = 0
    cur = None
    while p1 < len(l1) or p2 < len(l2):
        if p1 >= len(l1):
            cur = l2[p2]
            p2 += 1
        elif p2 >= len(l2):
            cur = l1[p1]
            p1 += 1
        else:
            if l1[p1][0] < l2[p2][0]:
                cur = l1[p1]
                p1 += 1
            else:
                cur = l2[p2]
                p2 += 1
        o, c = cur[0], cur[1]
        if o not in time_points:
            time_points[o] = deque(['o'])
        else:
            time_points[o].appendleft('o')
        if c not in time_points:
            time_points[c] = deque(['c'])
        else:
            time_points[c].appendright('c')
    time_orders = sorted(time_points)
    counter = 0
    start = end = None
    for t in time_orders:
        oprs = time_points[t]
        while oprs:
            opr = oprs.popleft()
            if opr == 'o':
                if counter == 0:
                    start = t
                counter += 1
            else:
                counter -= 1
                if counter == 0:
                    end = t
                    result.append([start, end])
    return result                    

            



def test():
    data = [
        (([[1,5], [10,14], [16,18]], [[2,6], [8,10], [11,20]]), [[1,6], [8, 20]]),
        (([[1,3]], [[2,4]]), [[1,4]]),
        (([[1,3], [5,10]], [[3,8],[12,17], [18,20]]), [[1,10], [12,17], [18,20]]),
        (([[1,3], [4,8]], [[1,2], [4,9], [11,13]]), [[1,3],[4,9], [11,13]]),
        (([[1,10],[14,15]], [[2,3],[5,6],[8,9]]), [[1,10],[14,15]]),
        # ((, ), ),
    ]

    test_fixture(merge_sorted_interval, data)
    test_fixture(merge_sorted_interval2, data)


test()

