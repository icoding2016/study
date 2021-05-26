"""
Move Zeroes
Easy
https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?



Ideas:
  - 2 pointers swap doesn't work since the question requires to 'maintain order'.
  - 



"""


from typing import List
from utils.testtools import test_fixture


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.buble_up2(nums)

    # T(N*N)
    def buble_up1(self, nums: List[int]) -> None:
        for i, v in enumerate(nums):
            if v == 0 and i < len(nums)-1:
                j =  i + 1
                while nums[j] ==  0 and j < len(nums)-1:
                    j += 1
                if j >= len(nums):
                    return
                nums[i], nums[j] = nums[j], nums[i]


    def buble_up2(self, nums: List[int]) -> None:
        last_non_zero = None
        for i, v in enumerate(nums):
            if v == 0 and i < len(nums)-1:
                j =  last_non_zero if last_non_zero else i + 1
                while nums[j] ==  0 and j < len(nums)-1:
                    j += 1
                if j >= len(nums):
                    return
                last_non_zero = j
                nums[i], nums[j] = nums[j], nums[i]



    # Wrong solution -- order not maintained
    def moveZeroes_1(self, nums: List[int]) -> None:
        p1 = 0
        p2 = len(nums) - 1
        while p2 > p1:
            while nums[p1] != 0 and p1 < p2:
                p1 += 1
            while nums[p2] == 0:
                p2 -= 1
            if p2 > p1:
                nums[p1], nums[p2] = nums[p2], nums[p1]

    def test_stub(self, nums:List[int]) -> List[int]:
        self.moveZeroes(nums)
        return nums


def test():
    data = [
        (([0,1,0,3,12],), [1,3,12,0,0]),
        (([0],), [0]),
        (([1],), [1]),
        (([1,0],), [1,0]),
        (([0,1],), [1,0]),
        (([1,0,2,0,3,0],), [1,2,3,0,0,0]),
        (([31,0,1,0,3,12,31,4,1,41,0,9,0,0,14,94,0,0,91,4,1,3,4,0,0,5],), [31,1,3,12,31,4,1,41,9,14,94,91,4,1,3,4,5,0,0,0,0,0,0,0,0,0]),
        (([0,0]+[i for i in range(1,1000)],), [i for i in range(1,1000)]+[0,0]),
    ]
    s = Solution()
    test_fixture(s.test_stub, data)


test()
