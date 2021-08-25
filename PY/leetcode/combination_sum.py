# Combination Sum
# Medium
#
# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers sum to target. 
# You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
# 
# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# 
# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
# 
# Example 3:
# Input: candidates = [2], target = 1
# Output: []
# 
# Example 4:
# Input: candidates = [1], target = 1
# Output: [[1]]
# 
# Example 5:
# Input: candidates = [1], target = 2
# Output: [[1,1]]
#
# Constraints:
# 1 <= candidates.length <= 30
# 1 <= candidates[i] <= 200
# All elements of candidates are distinct.
# 1 <= target <= 500

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        smaller_set = [c for c in candidates if c <= target]
        return self.combSum1(smaller_set, target)

    def combSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 1 and candidates[0]>target:
            return []
        return [x for x in self.combSum_r(target, candidates)]

    # T(N^m)         N=len(candidates), m=min(candidates)
    def combSum_r(self, remain: int, candidates: List[int], cur: List[int]=None) -> None:
        if None == cur:
            cur = []
        if remain == 0:
            yield cur
            return
        if remain < 0 or not candidates:
            return
        c = candidates[0]
        for x in self.combSum_r(remain-c, candidates, cur+[c]):
            yield x
        for x in self.combSum_r(remain, candidates[1:], cur):
            yield x
        return


def test_fixture(s):
    testdata = [  # (input, expect),
        (([2,3,6,7], 7),  [[2,2,3],[7]]),
        (([2,3,5], 8),  [[2,2,2,2],[2,3,3],[3,5]]),
        (([2], 1),  []),
        (([1], 1), [[1]]),
    ]

    def compResult(r, e):
        if len(r) != len(e):
            return False
        rr = [sorted(x) for x in r]
        ee = [sorted(x) for x in e]
        while rr:
            if rr[0] in ee:
                ee.remove(rr[0])
                rr.remove(rr[0])
            else:
                return False
        return not bool(ee)

    for i in range(len(testdata)):
        ret = s.combinationSum(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t expect {}".format(testdata[i][0], ret, exp), end='\t')
        print("{}".format('pass' if compResult(ret, exp) else 'fail'))



import timeit
def test():
    s = Solution()
    test_fixture(s)

test()



