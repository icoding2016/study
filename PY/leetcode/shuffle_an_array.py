# Given an integer array nums, design an algorithm to randomly shuffle the array.
# Implement the Solution class:
# Solution(int[] nums) Initializes the object with the integer array nums.
# int[] reset() Resets the array to its original configuration and returns it.
# int[] shuffle() Returns a random shuffling of the array.
#
# Example 1:
# Input
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# Output
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
# Explanation
# Solution solution = new Solution([1, 2, 3]);
# solution.shuffle();    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must be equally likely to be returned. Example: return [3, 1, 2]
# solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
# solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]
#
# Constraints:
# 1 <= nums.length <= 200
# -106 <= nums[i] <= 106
# All the elements of nums are unique.
# At most 5 * 104 calls will be made to reset and shuffle.

import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.A = nums
        self.B = nums.copy()

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.A = self.B.copy()
        return self.A
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        remain_id = set([x for x in range(len(self.A))])

        while len(remain_id) > 0:
            i = random.choice([x for x in remain_id])
            remain_id -= { i }
            if len(remain_id) > 0:
                j = random.choice([x for x in remain_id])
                remain_id -= {j}
            else:
                j = int(random.random()*(len(self.A)-1))
                if j == i:
                    j = i + 1
            self.A[i], self.A[j] = self.A[j], self.A[i]







