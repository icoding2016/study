# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Easy
#
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Example 2:
# Input: nums = [1]
# Output: 1
#
# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
#
# Constraints:
# 1 <= nums.length <= 3 * 104
# -105 <= nums[i] <= 105
#
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
# 
# 
# Ideas: 
#   Say m[i-1]=max_subarray at i-1, ([1:i],[2:i]...[i:i])
#         m[i]=max(A[i+1], m[i-1]+A[i])
#   Then max(m) find the max sub array sum value
#   That is called Kadane's Algorithm
# #

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #return self._maxSubArray_bf(nums)
        return self._maxSubArray1(nums)

    # Kadane's Algorighm.  O(N)
    def _maxSubArray1(self, nums: List[int]) -> int:
        M = [0]*len(nums)
        M[0] = nums[0]
        for i in range(1, len(nums)):
            M[i] = max([nums[i], M[i-1]+nums[i]])
        return max(M)

    # Brutal Force,  O(N^3)    (1+2+..N)+(2+..N)+..(1)
    def _maxSubArray_bf(self, nums: List[int]) -> int:
        m = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                s = sum(nums[i:j+1])
                m = s if s>m else m
        return m

def test_fixture(s:Solution):
    testdata = [  # (input, expect),
        (([-2,1,-3,4,-1,2,1,-5,4],), 6),
        (([1],), 1),
        (([5,4,-1,7,8],), 23),
        (([-4,-6,-2,-8,7],),7),
        (([-5,-2,0,-3,-6],), 0),
        (([4,0,0,0,-1,0,0,0,5],), 8),
        (([0,0,-3,0,-2,1,0,3,-4,2,1],), 4),
        #((3, [x for x in range(1,101)]), 35),
    ]
    for i in range(len(testdata)):
        ret = s.maxSubArray(*testdata[i][0])
        #exp = testdata[i][1]
        exp = s._maxSubArray_bf(*testdata[i][0])
        print("{} -> \t{} \t expect {}".format("testdata[i][0]", ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))
import timeit
def test():
    s = Solution()
    test_fixture(s)
test()
# timeit.timeit('test()', number=1)    
