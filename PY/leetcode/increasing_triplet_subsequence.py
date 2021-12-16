"""
334. Increasing Triplet Subsequence
Medium
https://leetcode.com/problems/increasing-triplet-subsequence/description/

Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 
Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 
Constraints:
1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1


Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

"""


from typing import List
from utils.testtools import test_fixture


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # return self.increasingTriplet2(nums)
        return self.increasingTriplet3(nums)

    # T(N*N)
    def increasingTriplet1(self, nums: List[int]) -> bool:
        options = []
        for i in range(len(nums)):
            if not options:
                options.append([nums[i]])
            for o in options:
                if o[-1] < nums[i]:
                    o.append(nums[i])
                    if len(o) >= 3:
                        return True
                elif o[-1] == nums[i]:
                    continue
                else:
                    options.append([nums[i]])
        return False

    # T(N)
    def increasingTriplet2(self, nums: List[int]) -> bool:
        first = second = None
        for n in nums:
            if first == None:
                first = n
            elif second == None:
                if n > first:
                    second = n
                else:
                    first = n
            else:
                if n > second:
                    return True
                elif n > first:
                    second = n
                else:
                    first = n
        return False

    # Greate solution from girikuncoro: https://leetcode.com/problems/increasing-triplet-subsequence/discuss/78995/Python-Easy-O(n)-Solution
    def increasingTriplet3(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


def test():
    data = [
        (([1,2,3,4,5],), True),
        (([5,4,3,2,1],), False),
        (([2,1,5,0,4,6],), True),
        (([3,1,3,1,3,1,3],), False),
        (([3,1,3,1,4,3,1],), True),
        (([1,3,3,2,1,2,1,2,1],), False),
        (([1,3,3,2,1,2,1,2,1,3],), True),
        (([4,5,1,6], ), True),
    ]
    s = Solution()
    test_fixture(s.increasingTriplet, data)


test()
