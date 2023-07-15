"""
LCM (Least Common Multiple)

Find the LCM of a list of iont

1. math lib support lcm method
2. LCM can be derived from GCD (Greatest Common Denominator)
   e.g.  for 2 int x, y,    LCM = x * y / GCD(x, y)

"""

from math import lcm, gcd
from functools import reduce


def LCM_1(data:list) -> int:
    return reduce(lcm, data)

def LCM_2(data:list) -> int:
    return reduce(lambda x,y: int((x*y)/gcd(x,y)), data)


test_data = [
    ([2, 3, 4, 5, 6], 60),
    ([49, 23, 15, 20, 2, 42, 21, 34], 1149540),
]


def test():
    print("LCM_1")
    for data, expectation in test_data:
        ret = LCM_1(data)
        print(f"{data}, LCM={ret} \t{'pass' if ret==expectation else 'fail'}")

    print("LCM_2")
    for data, expectation in test_data:
        ret = LCM_2(data)
        print(f"{data}, LCM={ret} \t{'pass' if ret==expectation else 'fail'}")


test()