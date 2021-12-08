"""
371. Sum of Two Integers
Medium

Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5

Constraints:
-1000 <= a, b <= 1000

"""


from utils.testtools import test_fixture

class Solution:
    def getSum(self, a: int, b: int) -> int:
        return self.getSum1(a, b)

    # T(max(N+M)+1)
    def getSum1(self, a: int, b: int) -> int:
        if a == 0:
            return b
        elif b == 0:
            return a
        bit_a = 0
        bit_b = 0
        bit = 0
        carry = 0
        bits = []
        while a > 0 or b > 0:
            bit_a = a & 1 if a > 0 else 0
            bit_b = b & 1 if b > 0 else 0
            a = a >> 1
            b = b >> 1
            if (bit_a and not bit_b) or (bit_b and not bit_a):
                bit = 0 if carry else 1
                carry = 1 if carry else 0
            elif (not bit_a and not bit_b):
                bit = carry
                carry = 0
            else:
                bit = carry
                carry = 1
            bits.append(bit)
        if carry:
            bits.append(carry)
        result = 0
        for i in bits[::-1]:
            result = result << 1
            result |= i
        return result

    def getSum2(self, a: int, b: int) -> int:
        if a == 0:
            return b
        elif b == 0:
            return a
        aa = self.int2bin(a)
        bb = self.int2bin(b)
        cc = []
        bit = 0
        carry = 0
        for i in range(max(len(aa), len(bb))):
            if i >= len(aa):
                bit, carry = self.bitadd(bb[i], 0, carry)
            elif i >= len(bb):
                bit, carry = self.bitadd(aa[i], 0, carry)
            else:
                bit, carry = self.bitadd(aa[i], bb[i], carry)
            cc.append(bit)
        if carry:
            cc.append(carry)
        #print(aa, bb, cc)
        result = 0
        for i in cc[::-1]:
            result = result << 1
            result |= i
        return result
        
    def int2bin(self, a:int) -> list[int]:
        aa = []
        while a//2 >= 0:
            if a==0:
                break
            aa.append(a%2)
            a = a//2
        return aa

    def bitadd(self, b1:int, b2:int, c:int) -> list[int, int]:
        if b1 == 0 and b2 == 0:
            return [c, 0]
        elif (b1 == 0 and b2 == 1) or (b1 == 1 and b2 == 0):
            b = 0 if c else 1
            carry = 1 if c else 0
            return [b, carry]
        elif b1 == 1 and b2 == 1:
            return [c, 1]
        raise Exception('only allow 0 or 1.')



def test():
    data = [
        ((10,5), 15),
        ((0,7), 7),
        ((4, 8), 12),
        ((11,35), 46),
        ((0,0), 0),
        ((15, 7), 22)
        ((-3, 4), 1)
    ]
    s = Solution()
    test_fixture(s.getSum, data)


test()
