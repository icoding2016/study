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
# 
# Ideas:
#   Use stack, push at Open and pop at Close, if stack is empty, that's a non-overlap interval
#   1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19...
#   o o c     c   o   c              o         c
# 
# 
#  


from typing import List
from collections import defaultdict, deque
from utils.testtools import test_fixture


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        return self.merge_stack(intervals)

    # T(E+Ilog(I)+Ilog(S))    E=len(intervals),  I=num of indexes with O/C flag,  S=max(num of stacking flag)
    def merge_stack(self, intervals: List[List[int]]) -> List[List[int]]:
        output = list()
        sequence = defaultdict(deque)   # { index:[0,1,..]}  0-open, 1-close
        for oi, ci in intervals:
            sequence[oi].appendleft(0)
            sequence[ci].append(1)
        sseq = sorted(sequence)

        stack = []
        start = end = None
        for i in sseq:
            oprs = sequence[i]
            for opr in oprs:
                if opr == 0:
                    if not stack:
                        start = i
                    stack.append(opr)
                else:
                    stack.pop()
                    if not stack:
                        end = i
                        output.append([start, end])
        return output


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
    test_fixture(s.merge_stack, data)


test()

