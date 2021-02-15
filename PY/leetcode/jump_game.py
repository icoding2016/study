#  Jump Game
# Medium
# https://leetcode.com/problems/jump-game/ 
#
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
#
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
#
# Constraints:
# 1 <= nums.length <= 3 * 104
# 0 <= nums[i] <= 105

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self.canJump2(nums)

    # T(N*S)   S=max-step 
    def canJump1(self, nums: List[int]) -> bool:
        N = len(nums)
        canReach = [False for i in range(N)]
        canReach[0] = True
        for i in range(N-1):
            for s in range(nums[i]+1):  # step from current nums[i]
                if canReach[i]:
                    if i+s == N-1:
                        return True
                    elif i+s< N:
                        canReach[i+s] = True
                    else:
                        break
                else:
                    continue
        return canReach[N-1]

    # O(N)
    def canJump2(self, nums: List[int]) -> bool:
        N = len(nums)
        canReach = [False for i in range(N)]
        canReach[0] = True
        max_reach = 0
        for i, s in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i+s)
            if max_reach >= N-1:
                return True
        return True

    # backwards tracking  ?? not work
    def canJump3(self, nums: List[int]) -> bool:
        N = len(nums)
        canReach = [False for i in range(N)]
        canReach[0] = True
        for i in range(N-1,-1,-1):
            for s in range(nums[i]+1):  # step from current nums[i]
                if canReach[i]:
                    if i+s == N-1:
                        return True
                    elif i+s< N:
                        canReach[i+s] = True
                    else:
                        break
                else:
                    continue
        return canReach[N-1]



def test_fixture(solution):
    testdata = [  # (input, expect),
        (([2,3,1,1,4], ), True),
        (([3,2,1,0,4], ), False),
        (([1,1,0,1,4], ), False),
        (([0], ), True),
        (([n for n in range(1000,0,-1)]+[1],), True),
        (([n for n in range(1000,0,-1)]+[0,1],), False),
    ]

    for i in range(len(testdata)):
        ret = solution.canJump(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t expect {}".format(testdata[i][0] if len(testdata[i][0][0])<7 else 'testdata[i][0]', ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))



def test():
    s = Solution()
    test_fixture(s)


test()    


