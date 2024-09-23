"""
1404. Number of Steps to Reduce a Number in Binary Representation to One
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/
Medium


Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
    If the current number is even, you have to divide it by 2.
    If the current number is odd, you have to add 1 to it.
It is guaranteed that you can always reach one for all test cases.


Example 1:
Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  

Example 2:
Input: s = "10"
Output: 1
Explanation: "10" corresponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  

Example 3:
Input: s = "1"
Output: 0


Constraints:
    1 <= s.length <= 500
    s consists of characters '0' or '1'
    s[0] == '1'


"""


from collections import deque
from utils.testtools import test_fixture


class Solution:
    def numSteps(self, s: str) -> int:
        return self.ns_bit(s)

    # T(N*N)  N=len(s)
    def ns_bit(self, s: str) -> int:
        count = 0
        dq = deque(s)
        while len(dq) > 1:
            n = dq[-1]
            if n == '0':
                count += 1
                dq.pop()
            else:
                count += 1
                for i in range(len(dq)):    # +1 operation
                    if dq[-1-i] == '0':
                        dq[-1-i] = '1'
                        break
                    else:
                        dq[-1-i] = '0'
                        if i == len(dq)-1:
                            dq.appendleft('1')
        return count

    # cannot handle long string
    def ns1(self, s: str) -> int:
        num = int(s, 2) 
        steps = 0
        while num > 1:
            if num % 2 == 0:
                num = int(num/2)
                steps += 1
            else:
                num += 1
                steps += 1
        return steps
        

def test():
    data = [
        (("1101",), 6),
        (("10",), 1),
        (("1",), 0),
        (("1111011110000011100000110001011011110010111001010111110001",), 85),
    ]
    s = Solution()
    test_fixture(s.numSteps, data)


test()
