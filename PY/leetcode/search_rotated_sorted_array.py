# Search in Rotated Sorted Array
# Medium
# You are given an integer array nums sorted in ascending order, and an integer target.
# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# If target is found in the array return its index, otherwise, return -1.
#  
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
#
# Constraints:
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is guranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4
#
# Ideas: (binary search + pivot check)
#    say lowest value at index k,
#       0                          k                 N
#       A[0],A[1] ...    A[k-1],  A[k], ...      A[N-1] 
#       Ak,  A(k+1)  ... A(N-1),  A(0), A(1)...  A(k-1)    (by value)
#    Pivot = A[0]  (a.k.a Ak), 
#         if target < pivot, search A[k~N] else search A[0,k]. 
#         but we don't know k, so we use the known left/right/mid.
#    mid = (left+right)//2
#     
#                           A[mid]<P                    A[mid]>P
#    if target < Pivot:  
#         search A[k~N] ->  [left,mid]                  [left,mid] if target<A[mid]
#                                                       [mid,k]    if target>A[mid] -> [mid,right]
#       target > Pivot:  
#         search A[0~k] ->  [k, mid] if target<A[mid]   [mid, right]
#                           -> [left, mid]
#                           [mid,right] if target>A[mid]
# 
# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/
# #

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.search2(nums, target)
    
    #bf
    # T(N)
    def search1(self, nums: List[int], target: int) -> int:
        for i, x in enumerate(nums):
            if x == target:
                return i
        return -1

    # T(logN)
    def search2(self, nums: List[int], target: int) -> int:    
        if target == nums[0]:
            return 0
        elif len(nums) == 1:
            return -1
        left = 0
        right = len(nums) -1
        P = nums[0]
        while left <= right:
            mid = (right+left)//2
            if nums[mid] == target:
                return mid
            if left == right:
                return -1
            if mid == left:
                if target in nums[left:right+1]:
                    return left if nums[left]==target else right
                else:
                    return -1

            if target < P:
                if nums[mid] < P:
                    if target < nums[mid]:
                        right = mid
                    else:
                        left = mid  # right = right
                else:  # num[mid] > P:
                    left = mid
            else:  # target > P
                if nums[mid] < P:
                    right = mid
                else:  # num[mid] >= P:
                    if target < nums[mid]:
                        right = mid
                    else:
                        left = mid  # right = right
        return -1


def test_fixture(solution):
    testdata = [  # (input, expect),
        (([4,5,6,7,0,1,2], 0), 4),
        (([4,5,6,7,0,1,2], 3), -1),
        (([1], 0), -1),
        (([i for i in range(10, 1000)]+[i for i in range(10)], 990), 980),
        (([i for i in range(10, 1000)]+[i for i in range(10)], 9), 999),
        (([i for i in range(10, 1000)]+[i for i in range(10)], 1001), -1),
        (([i for i in range(1000, 1100)]+[i for i in range(1000)], 990), 1090),
    ]

    for i in range(len(testdata)):
        ret = solution.search(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t\t{} expect {}".format("testdata[i][0]", ret, 'pass' if ret==exp else 'fail', exp))


def test():
    s = Solution()
    test_fixture(s)


test()    



