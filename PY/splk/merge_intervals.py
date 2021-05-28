# Merge Intervals
# Medium
# https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of the non-overlapping intervals 
# that cover all the intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Constraints:
# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104
# 


from typing import List
from collections import deque
from utils.testtools import test_fixture


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        idx = {}
        for o, c in intervals:
            if o in idx:
                idx[o].appendleft('o')
            else:
                idx[o] = deque(['o'])
            if c in idx:
                idx[c].append('c')
            else:
                idx[c] = deque(['c'])
        sidx = sorted(idx)
        result = []
        stack_i = []
        for i in sidx:
            while idx[i]:
                opr = idx[i].popleft()
                if opr == 'o':
                    stack_i.append(i)
                elif len(stack_i) == 1:
                    result.append([stack_i.pop(), i])
                else:   # 'c'
                    stack_i.pop()
        return result


def test():
    data = [
        (([[1,3],[2,6],[8,10],[15,18]], ), [[1,6],[8,10],[15,18]]),
        (([[1,4],[4,5]], ), [[1,5]]),
        (([[1,10]], ), [[1,10]]),
        (([[3,5], [4,5], [7,10], [2,4]], ), [[2,5],[7,10]]),
        (([[2,5], [3,3], [5,5], [4,9], [10,12],[14,18]], ),[[2,9],[10,12],[14,18]] ),
        (([[3,5], [6,9], [17,100], [2000,2004]], ), [[3,5], [6,9], [17,100], [2000,2004]]),
        (([[3,5], [4,5], [3,5], [2,4], [5,5],[2,3],[4,5]], ), [[2,5]]),
    ]
    s = Solution()
    test_fixture(s.merge, data)


test()




