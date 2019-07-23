'''
MinAvgTwoSlice
Find the minimal average of any slice containing at least two elements


A non-empty array A consisting of N integers is given. 
A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A 
(notice that the slice contains at least two elements). 
The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. 
To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of 
the slice with the minimal average. If there is more than one slice with a minimal average, 
you should return the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].

'''

'''
NOTE:
  Need optimization for performance
  S1():  Basic logic, bad performance  -- O(N**3)
  S2():  Applies Prefix-Sum to sum(A[P:Q]), a bit improvement in perf  -- O(N**2)
  S():   TODO: More improvement
'''


from utils import Debug


# time complexity: 
# TODO: optimizing this to solve performance issue
def S(A):
    N = len(A)
    min_av = None
    min_pos = 0
    if N == 2:
        return 0
    S = [0]*N
    for i in range(N):
        S[i] = A[i] + S[i-1] if i > 0 else A[i]
    for p in range(N-1):
        for q in range(p+1,N):
            sm = S[q] - S[p-1] if p > 0 else S[q]
            avg = sm/(q-p+1) 
            if min_av is None or avg < min_av:
                min_av = avg
                min_pos = p
    return  min_pos


# time complexity: O(N**2)
# Applies Prefix-Sum to sum(A[P:Q]), gain a little improvement in performance, but not enough
#   Task Score 60%, Correctness 100%, Performance 20%
def S2(A):
    N = len(A)
    min_av = None
    min_pos = 0
    if N == 2:
        return 0
    S = [0]*N
    for i in range(N):
        S[i] = A[i] + S[i-1] if i > 0 else A[i]
    for p in range(N-1):
        for q in range(p+1,N):
            sm = S[q] - S[p-1] if p > 0 else S[q]
            avg = sm/(q-p+1) 
            if min_av is None or avg < min_av:
                min_av = avg
                min_pos = p
    return  min_pos


# Basic logic without performance optimization
# time complexity: O(N ** 3)
def S1(A):
    N = len(A)
    min_av = None
    min_pos = 0
    for p in range(N-1):
        for q in range(p+1,N):
            a = sum(A[p:q+1])/(q-p+1) 
            if min_av is None or a < min_av:
                min_av = a
                min_pos = p
    return  min_pos   


def solution(A):
    return S(A)

if __name__ == "__main__":

    sample = [ 
        [4,2,2,5,1,5,8],  # 1
        [3,2,1,1,6],      # 2
        [3,2,1,1,2,1,2],  # 2
        [1,2,3,4,5],      # 0
        [5,1],            # 0
        [1,2],            # 0
        [3,3,3,3,3]       # 0
    ]

    for A in sample:
        print('-'*60)
        r = solution(A)
        print("{} -> {}".format(A, r))



