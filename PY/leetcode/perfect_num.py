# # Perfect Number
# Easy
# https://leetcode.com/problems/perfect-number/
#
# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. 
# A divisor of an integer x is an integer that can divide x evenly.
# Given an integer n, return true if n is a perfect number, otherwise return false.
#
# Example 1:
# Input: num = 28
# Output: true
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 1, 2, 4, 7, and 14 are all divisors of 28.
#  
# Example 2:
# Input: num = 6
# Output: true
#  
# Example 3:
# Input: num = 496
# Output: true
#  
# Example 4:
# Input: num = 8128
# Output: true
#  
# Example 5:
# Input: num = 2
# Output: false
#
# Constraints:
# 1 <= num <= 108

from math import sqrt

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return self._checkPerfectNumber2(num)

    def _checkPerfectNumber1(self, num: int) -> bool:
        if num <= 2:
            return False
        divisors = dict()
        S = 0
        for i in range(2, num//2):
            if i in divisors:
                break
            if num%i == 0:
                divisors[i] = True
                S += i
                j = num//i
                if j not in divisors:
                    divisors[j] = True
                    S += j
        S += 1
        return S == num

    def _checkPerfectNumber2(self, num: int) -> bool:
        if num <= 2:
            return False
        divisors = dict()
        S = 0
        for i in range(2, int(sqrt(num)+1)):
            if i in divisors:
                break
            if num%i == 0:
                divisors[i] = True
                S += i
                j = num//i
                if j not in divisors:
                    divisors[j] = True
                    S += j
        S += 1
        return S == num

def test_fixture(s):
    testdata = [  # (input, expect),
        ((28,),  True),
        ((6,),  True),
        ((496,),  True),
        ((8128,),  True),
        ((2,),  False),
        ((12,),  False),        
        ((25,),  False),

    ]

    for i in range(len(testdata)):
        ret = s.checkPerfectNumber(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t expect {}".format(testdata[i][0], ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))


import timeit
def test():
    s = Solution()
    test_fixture(s)

test()

