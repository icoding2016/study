"""
688. Knight Probability in Chessboard
Medium
https://leetcode.com/problems/knight-probability-in-chessboard/

On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. 
The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).
A chess knight has eight possible moves it can make, as illustrated below. 
Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.
  - x - x -
  x - - - x
  - - k - -
  x - - - x
  - x - x -

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.
The knight continues moving until it has made exactly k moves or has moved off the chessboard.

Return the probability that the knight remains on the board after it has stopped moving.

Example 1:
Input: n = 3, k = 2, row = 0, column = 0
Output: 0.06250
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.

Example 2:
Input: n = 1, k = 0, row = 0, column = 0
Output: 1.00000

Constraints:
1 <= n <= 25
0 <= k <= 100
0 <= row, column <= n

"""

from utils.testtools import test_fixture


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k < 1:
            return 1.0
        if n < 2:
            return 0.0
        self.memo = {}
        # return self.knightProbability_bf(n, k, row, column)
        return self.knightProbability_memo(n, k, row, column)

    # T(8^k)
    # S(k)     stack max = 8
    def knightProbability_bf(self, n: int, k: int, row: int, column: int) -> float:
        """The probability of inside the board when moving from a position"""
        if k <= 0:
            return 1.0
        nexthops = [(row-1, column-2), (row-1, column+2), (row-2, column-1), (row-2, column+1),
                    (row+1, column-2), (row+1, column+2), (row+2, column-1), (row+2, column+1),]
        total = 0.0
        for r, c in nexthops:
            if 0 <= r < n and 0 <= c < n:
                p = self.knightProbability_bf(n, k-1, r, c)
                total += p / 8
        return total

    # T(n*n*k)
    # S(n*n*k)   3D-memo: n*n*k,  can reduce to n*n*2 -> O(n*n) by just keeping the recent 2 layers
    def knightProbability_memo(self, n: int, k: int, row: int, column: int) -> float:
        if k <= 0:
            return 1.0
        if (row, column, k) in self.memo:
            return self.memo[(row, column, k)]
        nexthops = [(row-1, column-2), (row-1, column+2), (row-2, column-1), (row-2, column+1),
                    (row+1, column-2), (row+1, column+2), (row+2, column-1), (row+2, column+1),]
        total = 0.0
        for r, c in nexthops:
            if 0 <= r < n and 0 <= c < n:
                p = self.knightProbability_memo(n, k-1, r, c)
                total += p * 0.125
        self.memo[(row, column, k)] = total
        return total



def test():
    data = [
        ((3,2,0,0), 0.0625),
        ((1,0,0,0), 1.0),
        ((8,4,1,3), 0.32349),
        ((8,1,5,2), 1.0),
        ((20,8,9,7), 0.90331),
        ((13,12,4,8), 0.31366),
    ]
    s = Solution()
    def cmp(a, b, precision=5):
        if abs(a-b) < pow(0.1, precision):
            return True
        return False
    test_fixture(s.knightProbability, data, comp=cmp)


test()


