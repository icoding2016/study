"""
New Year Chaos
https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

Problem
It is New Year's Day and people are in line for the Wonderland rollercoaster ride. 
Each person wears a sticker indicating their initial position in the queue from  to . 
Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. 
One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order. 
Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

Example
q = [1,2,3,4,5,6,7,8]
If person 5 bribes person 4, the queue will look like this: 1,2,3,5,4,6,7,8. Only 1 bribe is required. Print 1.

q = [4,1,2,3]
Person 4 had to bribe 3 people to get to the current position. Print Too chaotic.

Function Description
Complete the function minimumBribes in the editor below.
minimumBribes has the following parameter(s):
  int q[n]: the positions of the people after all bribes
Returns
  No value is returned. 
  Print the minimum number of bribes necessary or Too chaotic if someone has bribed more than 2 people.
Input Format
  The first line contains an integer , the number of test cases.
  Each of the next 2 pairs of lines are as follows:
    - The first line contains an integer , the number of people in the queue
    - The second line has  space-separated integers describing the final state of the queue.

Constraints
  1 <= t
  1 <= n

Subtasks


Sample Input

STDIN       Function
-----       --------
2           t = 2
5           n = 5
2 1 5 3 4   q = [2, 1, 5, 3, 4]
5           n = 5
2 5 1 3 4   q = [2, 5, 1, 3, 4]
Sample Output
3
Too chaotic


"""


import math
import os
import random
import re
import sys

from utils.testtools import hackrank_test, hackrank_test_data

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    ret = minimumBribes1(q)
    print(ret)

    

def minimumBribes1(q):
    # Write your code here
    N = len(q)
    cur = 1
    moved = {}
    seq = {}
    for i, v in enumerate(q):
        if v != cur:
            moved[v]=i+1
        else:
            seq[cur]=i+1
            cur += 1
    total_move = 0
    for v,moved_to in moved.items():
        gap = v-moved_to
        if gap <=0:
            continue
        if gap > 2:
            return 'Too chaotic'
        else:
            total_move += abs(gap)
    #print(moved)
    return total_move



test_data = """
2
5
2 1 5 3 4
5
2 5 1 3 4
"""

test_exp = """3
'Too chaotic'"""

hackrank_test_data(test_data, test_exp)

#if __name__ == '__main__':
@hackrank_test
def main():
    _ = input()
    i = input()
    t = int(i.strip())

    for t_itr in range(t):
        n = int(input().strip())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)


main()
