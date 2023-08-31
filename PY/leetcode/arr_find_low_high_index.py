"""
Find Low/High Index
34. Find First and Last Position of Element in Sorted Array
Medium
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1]. See the example below.

e.g

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 5
Output: [0, 0]

Input: nums = [5,7,7,8,8,10], target = 18
Output: [-1,-1]

Input: nums = [], target = 0
Output: [-1,-1]

You must write an algorithm with O(log n) runtime complexity.

Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109

    

"""

from typing import List
from bisect import bisect, bisect_left


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # return self.search_range_bisect(nums, target)
        i = Solution.bsearch(nums, target, 0, len(nums) - 1)
        if i == -1:
            return [-1, -1]
        left, right = -1, -1
        l = r = i
        while True:
            if l == 0 or nums[l - 1] != target:
                left = l
                break
            else:
                l = Solution.bsearch(nums, target, 0, l - 1)
        while True:
            if r == len(nums) - 1 or nums[r + 1] != target:
                right = r
                break
            else:
                r = Solution.bsearch(nums, target, r + 1, len(nums) - 1)
        return [left, right]

    # use bisect
    def search_range_bisect(self, nums: List[int], target: int) -> List[int]:
        low = bisect_left(nums, target)
        high = bisect(nums, target)
        if low >= len(nums) or nums[low] != target:
            return [-1, -1]
        return [low, high - 1]

    @staticmethod
    def bsearch(nums: List[int], target: int, low: int, high: int) -> int:
        """search target and return index (-1 if not found),"""
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        assert low <= high, "low shold <= high"
        while low <= high:
            if low == high:
                return low if nums[low] == target else -1
            mid = low + (high - low + 1) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
                continue
            else:
                high = mid - 1
                continue
        return -1


test_data = [
    (([], 1), [-1, -1]),
    (([1], 1), [0, 0]),
    (([1], 2), [-1, -1]),
    (([2], 1), [-1, -1]),
    (([2, 4, 5, 5, 9], 1), [-1, -1]),
    (([2, 4, 5, 5, 9], 10), [-1, -1]),
    (([2, 4, 5, 5, 9], 6), [-1, -1]),
    (([2, 4, 5, 5, 9], 5), [2, 3]),
    (([2, 4, 5, 5, 5, 9], 5), [2, 4]),
    (([2, 4, 5, 5, 9], 4), [1, 1]),
    (([2, 4, 5, 5, 9], 2), [0, 0]),
    (([2, 4, 5, 5, 9], 9), [4, 4]),
    (([2, 4, 5, 5, 9, 9, 9], 9), [4, 6]),
    (([2, 2, 2, 2, 4, 5, 5, 9], 2), [0, 3]),
    # (([],), []),
]


def test():
    s = Solution()
    print("search_range_bisect.")
    for d, ep in test_data:
        ret = s.search_range_bisect(*d)
        print(f"{d} -> {ret} (expect {ep}): {'Pass' if ep==ret else 'Fail'}")

    print("searchRange.")
    for d, ep in test_data:
        ret = s.searchRange(*d)
        print(f"{d} -> {ret} (expect {ep}): {'Pass' if ep==ret else 'Fail'}")


test()
