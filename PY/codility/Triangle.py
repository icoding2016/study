'''
Triangle
Determine whether a triangle can be built from a given set of edges


An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

'''


'''

  Consideration:
    Triangle:  for either a,b,c: a+b>c;  so a,b,c should be close to each other.
    Sort the numbers and only pick the adjacent 3.
'''


# time complexity:  O(N*log(N))
def S(A):
    N = len(A)
    if N < 3:
        return 0

    S = sorted(A)
    for i in range(2,N):
        if S[i-2] + S[i-1] > S[i]:
            return 1
    return 0

def solution(A):
    return S(A)

if __name__ == "__main__":

    sample = [ 
        [4,1,3,2],        # 1
        [3,2,4,6],        # 1
        [1,2,3],          # 0
        [1,2],            # 0
        [2],              # 0
        [],               # 0
    ]

    for A in sample:
        print('-'*60)
        r = solution(A)
        print("{} -> {}".format(A, r))
