# A battleship question
#  
# Given list of battleship positions and hits, find how many ships have been sunk and how many ships have been hit, but not sunk
# Sink criteria: >=3 hit
# 
# The battleships are represented with 'X's, empty slots are represented with '.'s.
# You may assume the following rules:
#   You receive a valid board, made of only battleships or empty slots.
#   Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
#   At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
#  e.g.  
#  board = 
#  [["X","X",".","X","X","X"],
#   [".",".",".",".",".","."],
#   [".","X",".",".",".","."],
#   [".","X",".",".","X","X"],
#   [".","X",".","X",".","."],
#   [".","X",".","X",".","."]]
#  hits=[[1,3,4,0,0,0],
#        [0,1,0,7,0,3],
#        [0,0,4,2,0,0],
#        [2,1,0,0,0,3],
#        [1,0,3,2,0,3],
#        [0,0,0,0,0,3],]
#  ] 
#  => 5 battleships, hit 4, sunk 2
#  # 

class Solution(object):
    def __init__(self):
        self.sunk_threshold = 3    # sunk when hit >= threshold

    def battle_report(self, board:list[list[str]], hits:list[list[int]]) -> dict:  # (battleship#, hit#, sunk#)
        self.board = board
        self.hits = hits
        self.M = len(board)
        self.N = len(board[0])
        r = self.gen_report(board, hits)
        return (r["ship"], r["hit"], r["sunk"])

    def gen_report(self, board:list[list[str]], hits:list[list[int]])->dict:
        report = {"ship":0, 'hit':0, 'sunk':0}
        marked = {} # {(x,y):True}
        for y in range(self.M):
            for x in range(self.N):
                b,h = self.mark_ship((x,y), marked, 0)
                if b:
                    report["ship"] += 1
                    report["hit"] += 1 if h > 0 else 0
                    report["sunk"] += 1 if h >= self.sunk_threshold else 0
        return report

    def mark_ship(self, p:tuple, marked:dict, hit_counter:int=0)->(bool,int):
        x = p[0]
        y = p[1]
        if y < 0 or y >= self.M or x < 0 or x >= self.N:
            return False, hit_counter
        if self.board[y][x] == "." or (x, y) in marked:
            return False, hit_counter
        elif self.board[y][x] == "X":
            marked[(x,y)] = True
            hit_counter += self.hits[y][x]
            for n in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                _, hit_counter = self.mark_ship(n, marked, hit_counter)
            return True, hit_counter
        return False, hit_counter

def test_fixture(solution):
    testdata = [  # (input, expect),
        # N,ks,ke,b,
        (([ [".",".",".",".",".","."],    # board
            [".",".",".",".",".","."],
            [".",".",".",".",".","."],
            [".",".",".",".",".","."],
            [".",".",".",".",".","."],
            [".",".",".",".",".","."],], 
           [[1,3,4,0,0,0],                # hits
            [0,1,0,7,0,3],
            [0,0,4,2,0,0],
            [2,1,0,0,0,3],
            [1,0,3,2,0,3],
            [0,0,0,0,0,3],]), (0,0,0)),

        (([ [".","X",".",".","X","."],
            [".",".",".",".","X","."],
            [".","X",".","X",".","."],
            [".","X",".",".",".","X"],
            [".",".","X","X",".","."],
            ["X","X",".",".",".","."],],
           [[1,3,4,0,0,0],                # hits
            [0,1,0,7,0,3],
            [0,0,4,2,0,0],
            [2,1,0,0,0,3],
            [1,0,3,2,0,3],
            [0,0,0,0,0,3],]), (7,5,3)),

        (([ ["X","X",".","X","X","X"],
            [".",".",".",".",".","."],
            [".","X",".",".",".","."],
            [".","X",".",".","X","X"],
            [".","X",".","X",".","."],
            [".","X",".","X",".","."],], 
           [[1,3,4,0,0,0],                # hits
            [0,1,0,7,0,3],
            [0,0,4,2,0,0],
            [2,1,0,0,0,3],
            [1,0,3,2,0,3],
            [0,0,0,0,0,3],]), (5,4,2)),

        (([ ["X","X",".","X","X","X"],
            [".",".",".",".",".","."],
            [".","X",".",".",".","."],
            [".","X",".",".","X","X"],
            [".","X",".","X",".","."],
            [".","X",".","X",".","."],], 
           [[0,0,4,0,0,0],                # hits
            [0,1,0,7,0,3],
            [0,0,4,2,0,0],
            [2,0,0,1,0,0],
            [1,0,3,0,0,3],
            [0,0,0,0,0,3],]), (5,0,0)),

        (([ ["X",".","X",".","X","."],
            [".","X",".","X",".","X"],
            [".","",".",".",".","."],
            ["X","X","X","X","X","X"],
            [".",".",".",".",".","."],
            [".","X","X","X","X","."],], 
           [[1,3,4,0,0,0],                # hits
            [0,1,0,0,0,3],
            [0,0,4,2,0,0],
            [2,1,0,0,0,3],
            [1,0,3,2,0,3],
            [0,0,0,0,0,3],]), (8,5,3)),
    ]

    for i in range(len(testdata)):
        ret = solution.battle_report(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t expect {}".format("testdata[i][0]", ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))


def test():
    s = Solution()
    test_fixture(s)


test()    

