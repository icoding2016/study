"""
300. Longest Increasing Subsequence
Medium

Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?

"""

from typing import List, Optional
from utils.testtools import test_fixture


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # return self.lenOfLIS_r(nums)
        return self.lenOfLIS(nums)

    # recursive solution:
    # T(2^N) 
    def lenOfLIS_r(self,nums: List[int],  cur:Optional[int]=None, count:int=0) -> int:
        if len(nums) == 0:
            return count
        if cur == None:
            return max(self.lenOfLIS_r(nums[1:], nums[0], 1), self.lenOfLIS_r(nums[1:], None, 0))
        if nums[0] <= cur:
            return self.lenOfLIS_r(nums[1:], cur, count)
        c1 = self.lenOfLIS_r(nums[1:], nums[0], count+1)
        c2 = self.lenOfLIS_r(nums[1:], cur, count)
        return max(c1, c2)

    # DP solution
    # T(N*N)     T= (N-1)+(N-2)+..+1 = N(N-1)/2
    def lenOfLIS(self, nums: List[int]) -> int:
        lis = {i:0 for i in range(len(nums))}
        lis[len(nums)-1] = 1
        for i in range(len(nums)-1, 0, -1):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    lis[j] = max(lis[i]+1, lis[j])
                else:  # nums[j] >= nums[i]:
                    lis[j] = max(lis[j], 1)
        # print(lis)
        return max([v for v in lis.values()])

    # Wrong anwser, doesn't consider skip cur increasing number
    def lenOfLIS_wrong(self, nums: List[int]) -> int:
        lis = {i:1 for i in range(len(nums))}
        for i in range(len(nums)):
            count = 1
            cur = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] > cur:
                    count += 1
                    cur = nums[j]
            lis[i] = count
        return max([c for c in lis.values()])


def test():
    data = [
        (([10,9,2,5,3,7,101,18],),4),
        (([0,1,0,3,2,3],),4),
        (([7,7,7,7,7,7,7],),1),
        (([7,6,5,4,3,2,1],),1),
        (([3],),1),
        (([10,9,2,5,3,7,101,18,77,42,138,90,99,100],),8),
        (([1,3,6,7,9,4,10,5,6],),6)
    ]
    s = Solution()
    test_fixture(s.lengthOfLIS, data)

test()
