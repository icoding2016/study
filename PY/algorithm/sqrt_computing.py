# method for computing square root
# Sqrt(x) Requires to output double -- need to handle decimal
#
# Constrain: 
#    0 <= x <= 2^31-1
# 
# Methods:
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots 
#   1) binary estimation
# 
# 
#   


from utils.testtools import test_fixture
from math import sqrt


class Solution():
    def __init__(self, precision=4) -> None:
        self.precision = precision
    
    @staticmethod
    def sqrt(num:int, precision=4) -> float:
        if num == 0 or num == 1:
            return num
        return Solution.sqrt_binary(num, precision)

    @staticmethod
    def sqrt_binary(num, precision=4) -> float:
        low = high = num
        if num >= 1:
            low = 0
        else:
            high = 1
        mid = None
        accept_margin = pow(0.1, precision)
        while abs(high-low) > accept_margin:
            mid = low + (high-low)/2
            sq = mid*mid
            if abs(sq - num) < accept_margin:
                return mid
            if sq < num:
                low = mid
            else:
                high = mid
        return mid

def test():
    data = [
        ((4,), 2),
        ((8,), sqrt(8)),
        ((10,), sqrt(10)),
        ((1,), 1),
        ((0,), 0),
        ((0.25,), 0.5),
    ]

    precision = 4
    
    def cmpr(r, e):
        if abs(r-e) < pow(0.1, precision):
            return True
        return False
    test_fixture(Solution.sqrt, data, cmpr)


test()

