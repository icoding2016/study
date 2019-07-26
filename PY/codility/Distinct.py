'''
Distinct
Compute number of distinct values in an array.


Write a function

def solution(A)

that, given an array A consisting of N integers, returns the number of distinct values in array A.

For example, given array A consisting of six elements such that:

 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1
the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''


'''
NOTE:
  Python's set() is the simplest tool that solve the problem quickly.  (See S1())
  
  Write another solution to practice the logic by myself without set().

'''


from utils import Debug


def S(A):
    N = len(A)
    S = sorted(A)
    if N < 2:
        return N
    count = 1
    for i in range(1, N):
        if S[i] != S[i-1]:
            count += 1

    return count


# time complexity:  O(N*log(N)) or O(N)
def S1(A):
    N = len(A)
    S = set(A)
    return len(S)


def solution(A):
    return S(A)

if __name__ == "__main__":

    sample = [ 
        [4,1,-3,2],       # 4
        [3,1,2,4,2],      # 4
        [1,2,2,1,5],      # 3
        [1],              # 1
        [],               # 0
        [1,1,1,1,1],      # 1
    ]

    for A in sample:
        print('-'*60)
        r = solution(A)
        print("{} -> {}".format(A, r))

