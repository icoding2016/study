"""
150. Evaluate Reverse Polish Notation
Solved
Medium
Topics
Companies

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.

 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

 

Constraints:

    1 <= tokens.length <= 104
    tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].


"""


from typing import List
from collections import defaultdict


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        return self.evalRPN2(tokens)

    def evalRPN1(self, tokens: List[str]) -> int:
        stack = []
        oprs = ['+', '-', '*', '/']
        for x in tokens:
            if x not in oprs:
                stack.append(int(x))
            else:
                b = stack.pop()
                a = stack.pop()
                c = int(eval(f"{a}{x}{b}"))
                stack.append(c)
        return stack[0]
    
    def evalRPN2(self, tokens: List[str]) -> int:
        stack = []
        oprs = ['+', '-', '*', '/']
        for x in tokens:
            if x not in oprs:
                stack.append(int(x))
            else:
                b = stack.pop()
                a = stack.pop()
                c = None
                if x == '+':
                    c = a + b
                elif x == '-':
                    c = a - b
                elif x == '*':
                    c = a * b
                elif x == '/':
                    c = int(a / b)
                stack.append(c)
        return stack[0]


def test_fixture(solution):
    testdata = [  # (input, expect),
        ((["10","6","9","3","+","-11","*","/","*","17","+","5","+"],), 22),
        # ((),),
    ]

    for i in range(len(testdata)):
        ret = solution.evalRPN(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t\t{} expect {}".format(testdata[i][0], ret, 'pass' if ret==exp else 'fail', exp))


def test():
    s = Solution()
    test_fixture(s)


test()    