# Robot Return to Origin
# Easy
# https://leetcode.com/problems/robot-return-to-origin/
#
# There is a robot starting at position (0, 0), the origin, on a 2D plane.
# Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
# The move sequence is represented by a string, and the character moves[i] represents its ith move. 
# Valid moves are R (right), L (left), U (up), and D (down). 
# If the robot returns to the origin after it finishes all of its moves, return true. 
# Otherwise, return false.
#
# Note: The way that the robot is "facing" is irrelevant. 
# "R" will always make the robot move to the right once, "L" will always make it move left, 
# etc. Also, assume that the magnitude of the robot's movement is the same for each move.
#
# Example 1:
# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.
#
# Example 2:
# Input: moves = "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.

# Example 3:
# Input: moves = "RRDD"
# Output: false

# Example 4:
# Input: moves = "LDRRLRUULR"
# Output: false
 
# Constraints:
# 1 <= moves.length <= 2 * 104
# moves only contains the characters 'U', 'D', 'L' and 'R'.



# from collections import Counter

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        C = {'L':0, 'R':0, 'U':0, 'D':0}
        for m in moves:
            C[m] += 1
        return C['L'] == C['R'] and C['U'] == C['D']




def test_fixture(s:Solution):
    testdata = [  # (input, expect),
        (("UD",), True),
        (("LL",), False),
        (("RRDD",), False),
        (("LDRRLRUULR",),False),
        (("RDDLLURDUU",), True),
        (("L",), False),
    ]
    for i in range(len(testdata)):
        ret = s.judgeCircle(*testdata[i][0])
        exp = testdata[i][1]
        #exp = s.maxProfit_bf(*testdata[i][0])
        print("{} -> \t{} \t expect {}".format("testdata[i][0]", ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))

import timeit
def test():
    s = Solution()
    test_fixture(s)
test()
