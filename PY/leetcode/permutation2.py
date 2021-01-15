#  Permutations II
# Medium
# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
#
# Example 1:
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# 
# Example 2:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 
# Constraints:
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
#
# The key is how to deal with the duplicate
# Solution 1: BF recursive, skip duplicate
#
# Solution 2:  N positions,  M numbers  e.g. [1,1,2,3]   {1:2, 2:1, 3:1}, N=4, M=3
#   for each position, pick a number out of M, 
# # 

from typing import List
from collections import Counter
from call_counter import call_counter, show_call_counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nc = Counter(nums)
        #return self.permute_bf(nums)
        return self.permute1(nc, len(nums))

    # brutal force
    # T(N!)
    # S(N)
    @call_counter
    def permute_bf(self, nums: List[int], cur: List[int]=None, output:List[List]=None) -> List[List[int]]:
        if None == output:
            output = []
        if None == cur:
            cur = []
        if not nums:
            if cur not in output:
                output.append(cur)
            return output
        for i,n in enumerate(nums):
            self.permute_bf(nums[:i]+nums[i+1:], cur+[n], output)
        return output

    # T(M^N)
    @call_counter
    def permute1(self, nc:dict[int,int], remain_len:int, cur: List[int]=None, output:List[List]=None) -> List[List[int]]:
        if None == output:
            output = []
        if None == cur:
            cur = []
        if not remain_len:
            output.append(cur)
            return output
        for n in nc:
            newnc = nc.copy()
            if newnc[n] > 1:
                newnc[n] -= 1
            else:
                del newnc[n]
            self.permute1(newnc, remain_len-1, cur+[n], output)
        return output


def test_fixture(solution):
    testdata = [  # (input, expect),
        (([1]), [[1]]),
        (([1,1,2]), [[1,1,2],[1,2,1],[2,1,1]]),
        (([1,2,3]), [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
        (([1,1,1]),[1,1,1]),
    ]

    for i in range(len(testdata)):
        ret = solution.permuteUnique(testdata[i][0])
        show_call_counter()
        exp = sorted(testdata[i][1])
        print("{} -> \t{} \t\t{} expect {}".format(testdata[i][0], ret, 'pass' if sorted(ret)==exp else 'fail', exp))


def test():
    s = Solution()
    test_fixture(s)


test()    

