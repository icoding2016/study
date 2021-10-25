"""
Minimax Algorithm

Minimax is a kind of backtracking algorithm that is used in decision making and game theory 
to find the optimal move for a player, assuming that your opponent also plays optimally. 

The Minimax algorithm helps find the best move, by working backwards from the end of the game. 
At each step it assumes that player A is trying to maximize the chances of A winning, 
while on the next turn player B is trying to minimize the chances of A winning (i.e., to maximize B's own chances of winning).


https://en.wikipedia.org/wiki/Minimax
https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/



In below example, given a list of values (data[]) in the bottom level of the tree,
2 players (minPlayer/maxPlayer) try to minimize/maximize.
e.g.
  data = [3, 5, 2, 9, 12, 5, 23, 23],   maxPlayer first

  max             ?
               /      \ 
  min       -            -       
           / \          /  \ 
  max    -     -      -      -
        / \   / \    / \    / \
  min  [3, 5, 2, 9, 12, 5, 23, 23]
 
"""

from math import log2, pow
from utils.testtools import test_fixture


def minmax(data:list, maxTurn:bool, index:int) -> int:
    # index = level*2-1
    level = int(log2(index))+1 if index > 0 else 0
    max_level = int(log2(len(data)))+1
    offset = int(pow(2, max_level))
    if level >= max_level:
        print(f"{'max' if maxTurn else 'min' } index {index}: {data[index-offset+1]}")
        return data[index-offset+1]
    if maxTurn:
        pick = max(minmax(data, False, 2*index+1), minmax(data, False, 2*index+2))
    else:
        pick = min(minmax(data, True, 2*index+1), minmax(data, True, 2*index+2))
    print(f"{'max' if maxTurn else 'min' } index {index}: {pick}")
    return pick


def test():
    data = [
        (([3, 5, 2, 9, 12, 5, 23, 23],True, 0), 12),
        # ((,),),
    ]
    test_fixture(minmax, data)


test()

