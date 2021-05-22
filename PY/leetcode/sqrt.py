# Sqrt(x)
# Easy
# https://leetcode.com/problems/sqrtx/

# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

# Example 1:
# Input: x = 4
# Output: 2

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

# Constraints:
# 0 <= x <= 231 - 1


from utils.testtools import test_fixture


class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        return self.sqrt_binary(x)

    def sqrt_binary(self, x: int) -> int:
        low = 0
        high = x
        mid = None
        while low < high:
            mid = low + (high-low)/2
            sq = int(mid*mid)
            if sq == x:
                return int(mid)
            elif sq < x:
                low = mid
            else:
                high = mid
        return mid


def test():
    data = [
        ((4,), 2),
        ((8,), 2),
        ((10,), 3),
        ((1,), 1),
        ((0,), 0),
    ]
    s = Solution()
    test_fixture(s.mySqrt, data)


test()


