"""
1877. Minimize Maximum Pair Sum in Array
Medium
https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

The pair sum of a pair (a,b) is equal to a + b. 
The maximum pair sum is the largest pair sum in a list of pairs.

For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:
- Each element of nums is in exactly one pair, and
- The maximum pair sum is minimized.
- Return the minimized maximum pair sum after optimally pairing up the elements.


Example 1:
Input: nums = [3,5,2,3]
Output: 7
Explanation: The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.

Example 2:
Input: nums = [3,5,4,2,4,6]
Output: 8
Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.
 

Constraints:
n == nums.length
2 <= n <= 105
n is even.
1 <= nums[i] <= 105

"""


from typing import List
from utils.testtools import test_fixture


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        return min([x for x in self.minPairSum_r(nums)])

    # T(N*)     N*(N-1)
    def minPairSum_r(self, remain: List[int], cur_max=None):
        if len(remain) == 0:
            yield cur_max
            return
        a = remain[0]
        for i in range(1,len(remain)):
            mx = a+remain[i] if cur_max==None else max(cur_max, a+remain[i])
            for x in self.minPairSum_r(remain[1:i]+remain[i+1:], mx):
                yield x
            


    # wrong solution,
    def minPairSum1(self, nums: List[int]) -> int:
        snums = sorted(nums)
        mx = None
        for i in range(len(nums)//2):
            cur = nums[i] + nums[len(nums)-1-i]
            if mx == None:
                mx = cur
            elif mx < cur:
                mx = cur
        return mx


def test():
    data = [
        (([3,5,2,3],),7),
        (([3,5,4,2,4,6],),8),
        (([3,4],),7),
        (([3,5,2,3,4,7,2,6,11,9],),13),
        # ((,),),
    ]
    s = Solution()
    test_fixture(s.minPairSum, data)


test()
