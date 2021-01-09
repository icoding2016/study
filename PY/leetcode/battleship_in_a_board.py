# Battleships in a Board
# Medium
# https://leetcode.com/problems/battleships-in-a-board/
#  
# Given an 2D board, count how many battleships are in it. 
# The battleships are represented with 'X's, empty slots are represented with '.'s. 
# You may assume the following rules:
#   You receive a valid board, made of only battleships or empty slots.
#   Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
#   At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
#   Example:
#     X..X
#     ...X
#     ...X
#     In the above board there are 2 battleships.
#   Invalid Example:
#     ...X
#     XXXX
#     ...X
#     This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
# 
# Follow up:
#   Could you do it in one-pass, using only O(1) extra memory and without modifying the value of the board?


from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        return self.countBattleships2(board)

    # T(M*N*max(M,N))
    def countBattleships1(self, board: List[List[str]]) -> int:
        self.M = len(board)
        self.N = len(board[0])
        checked = {}
        count = 0
        for y in range(self.M):
            for x in range(self.N):
                if board[y][x] == '.':
                    continue
                if (x,y) in checked:
                    continue
                if self.markShip(board, (x,y), checked):
                    count += 1
        return count

    def markShip(self, board:List[List[str]], p:tuple, checked:dict)->bool:
        x=p[0]
        y=p[1]
        if x < 0 or x >= self.N or y < 0 or y >= self.M:
            return False
        if board[y][x] != 'X' or (x,y) in checked:
            return False
        checked[(x,y)] = True
        for n in [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]:
            self.markShip(board, n, checked)
        return True        

    # go through the matrix, if the left or up of current is 'X', do not count, otherwise count+1
    # T(N*M)
    def countBattleships2(self, board: List[List[str]]) -> int:
        self.M = len(board)
        self.N = len(board[0])
        count = 0
        for y in range(self.M):
            for x in range(self.N):
                if board[y][x] == 'X':
                    if (x-1 < 0 or (x-1 >= 0 and board[y][x-1] != 'X')) and \
                       (y-1 < 0 or (y-1 >=0 and board[y-1][x] != 'X')):
                       count += 1
        return count                        
        


def test_fixture(solution):
    testdata = [  # (input, expect),
        # N,ks,ke,b,
        (([ [".",".",".",".",".","."],
            [".",".",".",".",".","."],
            [".",".",".",".",".","."],
            [".",".",".",".",".","."],
            [".",".",".",".",".","."],
            [".",".",".",".",".","."],], ), 0),
        (([ [".","X",".",".","X","."],
            [".",".",".",".","X","."],
            [".","X",".","X",".","."],
            [".","X",".",".",".","X"],
            [".",".","X","X",".","."],
            ["X","X",".",".",".","."],], ), 7),
        (([ ["X","X",".","X","X","X"],
            [".",".",".",".",".","."],
            [".","X",".",".",".","."],
            [".","X",".",".","X","X"],
            [".","X",".","X",".","."],
            [".","X",".","X",".","."],], ), 5),
        (([ ["X",".","X",".","X","."],
            [".","X",".","X",".","X"],
            [".","",".",".",".","."],
            ["X","X","X","X","X","X"],
            [".",".",".",".",".","."],
            [".","X","X","X","X","."],], ), 8),
    ]

    for i in range(len(testdata)):
        ret = solution.countBattleships(*testdata[i][0])
        exp = testdata[i][1]
        #print("{} -> \t{} \t expect {}".format(testdata[i][0], ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))


def test():
    s = Solution()
    test_fixture(s)


test()    



