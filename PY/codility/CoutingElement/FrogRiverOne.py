'''
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0)
  and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given a zero-indexed array A consisting of N integers representing the falling leaves.
  A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river.
The frog can cross only when leaves appear at every position across the river from 1 to X
(that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves).
You may assume that the speed of the current in the river is negligibly small,
i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

int solution(int X, int A[], int N);
that, given a non-empty zero-indexed array A consisting of N integers and integer X,
returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Assume that:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(X), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.

'''

def FrogRiverOne(X, A):

    N = len(A)
    xCounter = X
    leafMark=[-1]*X    #initalized to -1 which means leaf is not available at the position

    for i in range(N):
        K = A[i]
        if leafMark[K-1] == -1:      # newly appear on the position
            xCounter -= 1
            leafMark[K-1] = 1        # mark it
        if xCounter <= 0:               # all position ready
            return i
    return -1

def Verify():
    X=5
    A1 = [3,5,1,3,4,2,1,2]      #5
    A2 = [1,4,2,3,1]            #3
    A3 = [2,3,3,5,1]            #-1
    AA=[A1,A2,A3]
    for a in AA:
        r = FrogRiverOne(X, a)
        print("%s, result:%d" %(a, r))

Verify()
