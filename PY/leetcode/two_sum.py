# Two Sum
# Easy
# https://leetcode.com/problems/two-sum/
#  
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
# Constraints:
# 2 <= nums.length <= 103
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.twoSum_1(nums, target)

    # T(N)
    # S(N)
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        index = dict()
        for i, x in enumerate(nums):
            y = target - x
            if y in index:
                return [i, index[y]]
            else:
                index[x] = i
        raise Exception('No answers')


def test_fixture(s:Solution):
    testdata = [  # (input, expect),
        (([2,7,11,15],9), [0,1]),
        (([3,2,4],6), [1,2]),
        (([3,3],6), [0,1]),
    ]
    def cmp_result(a,b):
        if (a[0]==b[0] and a[1]==b[1]) or (a[0]==b[1] and a[1]==b[0]):
            return True
        else:
            return False
    for i in range(len(testdata)):
        ret = s.twoSum(*testdata[i][0])
        exp = testdata[i][1]
        #exp = s.maxProfit_bf(*testdata[i][0])
        print("{} -> \t{} \t expect {}".format("testdata[i][0]", ret, exp), end='\t')
        print("{}".format('pass' if cmp_result(ret,exp) else 'fail'))
import timeit
def test():
    s = Solution()
    test_fixture(s)
test()

