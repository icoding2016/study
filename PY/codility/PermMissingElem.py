'''
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], 
which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].

'''

'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
NOTE:  Failed cases
1. Not checking boundary  (e.g. N=0 -- empty list).
   [i for i in range(1,1)] --> []
2. number of iteration of [1,..,(N+1)] is bigger than len(A). Will overflow if put A[i] in one loop
e.g. S1
'''


from utils import Debug


def S(A):
    N = len(A)
    if N == 0:
        return 1
    A.sort()
    for i in range(1, N+1):
        if i != A[i-1]:
            return i
    else:
        return N+1


def S1(A):
    A.sort()
    for i in range(1, N+1):
        if i != A[i-1]:
            return i


def solution(A):
    return S(A)

if __name__ == "__main__":

    sample = [ 
        [2,5,3,1],
        [],
        [1],
        [2],
    ]

    for A in sample:
        r = solution(A)
        print("{} -> {}".format(A, r))



