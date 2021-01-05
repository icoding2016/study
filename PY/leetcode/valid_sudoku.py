# Valid Sudoku
# Medium
# https://leetcode.com/problems/valid-sudoku/
#  
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
#
# Example 1:
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# 
# Example 2:
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
# 
# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.


from typing import List

class Solution:
    def __init__(self):
        self.vals = set([str(x) for x in range(1,10)])

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidSudoku1(board)

    # bf2:
    # T(N^2)    # row: N*(N+N+N)=3N^2 -> O(N^2),  col: 3N^2, 
    def isValidSudoku1(self, board: List[List[str]]) -> bool:
        C = len(board[0])
        R = len(board)
        for row in board:
            lr = []
            for v in row:
                if v == ".":
                    continue
                if v in lr or v not in self.vals:
                    return False
                lr.append(v)
        for c in range(C):
            lc = []
            for r in range(R):
                v = board[r][c]
                if v == ".":
                    continue
                if v in lc or v not in self.vals:
                    return False
                lc.append(v)
        for j in range(R//3):
            for i in range(C//3):
                lb = []
                for y in range(3):
                    for x in range(3):
                        v = board[j*3+y][i*3+x]
                        if v == ".":
                            continue
                        if v in lb or v not in self.vals:
                            return False
                        lb.append(v)
        return True

    # bf2:
    # T(N^2)    # row: N*(N+N+N)=3N^2 -> O(N^2),  col: 3N^2, 
    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        C = len(board[0])
        R = len(board)
        for r in range(R):   # row
            lr = [x for x in board[r] if x != "."]
            sr = set(lr)
            if len(lr) != len(sr):
                return False
            if not set.issubset(sr, self.vals):
                return False
        # check col
        for c in range(C):
            lc = [board[r][c] for r in range(R) if board[r][c] != "."]
            sc = set(lc)
            if len(lc) != len(sc):
                return False
            if not set.issubset(sc, self.vals):
                return False
        # check subblock
        for r in range(R//3):
            for c in range(C//3):
                lb = []
                for i in range(3):
                    for j in range(3):
                        v = board[r*3+j][c*3+i]
                        if v == ".":
                            continue
                        if v in lb or v not in self.vals:
                            return False
                        lb.append(v)
        return True




def test_fixture(solution):
    testdata = [  # (input, expect),
        ((  [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]], ), True),   # True
        ((  [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","0"]], ), False),   # 0 not in [(]1-9]
        ((  [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","5",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]], ), False),   # violate block rule
        ((  [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]], ), False),   # violate column rule
        ((  [["2",".",".","4",".",".",".",".","2"]
            ,[".",".",".",".",".",".",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,["1",".",".",".",".",".",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,["3",".",".",".",".",".",".",".","."]], ), False),   # violate row rule
        ((  [[".",".",".",".",".",".",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]
            ,[".",".",".",".",".",".",".",".","."]], ), True),   # empty -- true
    ]

    for i in range(len(testdata)):
        ret = solution.isValidSudoku(*testdata[i][0])
        exp = testdata[i][1]
        #print("{} -> \t{} \t expect {}".format(testdata[i][0], ret, exp))
        print("{}".format('pass' if ret==exp else 'fail'))



def test():
    s = Solution()
    test_fixture(s)


test()    





