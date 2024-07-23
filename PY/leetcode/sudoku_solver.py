"""
37. Sudoku Solver
https://leetcode.com/problems/sudoku-solver/submissions/1330060064/
Hard

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

    Each of the digits 1-9 must occur exactly once in each row.
    Each of the digits 1-9 must occur exactly once in each column.
    Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

Example 1:
Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

Constraints:
    board.length == 9
    board[i].length == 9
    board[i][j] is a digit or '.'.
    It is guaranteed that the input board has only one solution.


Solution:
  backtracking: for each empty cell to fill, try the possible numbers.

"""


from typing import List, Tuple


# T(9^E)    E: empty_cells#
# S(E)      E: empty_cells#
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.result = None
        to_fill = [(x,y) for x in range(9) for y in range(9) if board[y][x]=='.']
        print(len(to_fill))
        if self.solve(to_fill, board):
            return self.result
        assert False, f'no found'
        

    def solve(self, to_fill:List[Tuple[int]], board:List[List[str]]) -> bool:
        if not to_fill:
            self.result = board
            return True
        x,y = to_fill.pop()
        pn = self.possible_num(x,y, board)
        if not pn:
            to_fill.append((x,y))
            return False
        for v in pn:
            board[y][x] = v
            if self.solve(to_fill, board):
                self.result = board
                return True
        board[y][x] = '.'
        to_fill.append((x,y))
        return False

    # speed can be improved by loopings candidate instead of cells
    def possible_num(self, x:int, y:int, board:List[List[str]]) -> List[int]:
        candidate = [chr(ord('0')+i) for i in range(1, 10)]
        if not candidate:
            return []
        for n in board[y]:
            if n != '.' and n in candidate:
                candidate.remove(n)
        for n in [board[i][x] for i in range(9)]:
            if n != '.' and n in candidate:
                candidate.remove(n)
        for j in range(y//3*3, y//3*3+3):
            for i in range(x//3*3, x//3*3+3):
                n = board[j][i]
                if n != '.' and n in candidate:
                    candidate.remove(n)
        return candidate





