'''
MissingInteger
Find the smallest positive integer that does not occur in a given sequence.


This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer 
(greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''


'''
NOTE:
  1. Read and understand question. (e.g. wrong understanding in S1())
  2. Take care of boundary situation
  3. Use sort to simplify logic
'''


from utils import Debug


def S(A):
    S = sorted(A)

    nextMissingMax = 1
    for i in range(len(S)):
        if S[i] < 1 or S[i] < nextMissingMax:
            continue
        elif S[i] == nextMissingMax:
            nextMissingMax += 1
        else:  # S[i] > nextMissingMax:
            break
    return nextMissingMax
    


def S1(A):
    S = sorted(A)

    curContinousMax = S[0]
    nextMissingMax = 1 if S[0] < 1 else S[0]+1
    for i in range(len(S)):
        if S[i] < 1 or S[i] <= curContinousMax:
            continue
        elif S[i] == nextMissingMax:
            curContinousMax = S[i]
            nextMissingMax += 1
        elif S[i] > curContinousMax:
            break
    return nextMissingMax
    


def solution(A):
    return S(A)

if __name__ == "__main__":

    sample = [ 
        [1, 3, 6, 4, 1, 2],        # 5
        [1, 2, 3],      # 4
        [-1, -3],       # 1
        [1],            # 2
        [0],            # 1
        [-1],           # 1
        [1,1,1,1],      # 2
        [2,2,2],        # 1
        [2,4,5],        # 1
    ]

    for A in sample:
        print('-'*60)
        r = solution(A)
        print("{} -> {}".format(A, r))

