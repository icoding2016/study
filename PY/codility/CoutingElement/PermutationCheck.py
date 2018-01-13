
'''
A non-empty zero-indexed array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

int solution(int A[], int N);
that, given a zero-indexed array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.

'''

def PermCheck(A):
    N = len(A)
    CheckA = [-1]*N   # initalize all elements to -1
    for x in A:
        if x > N:
            return 0
        if CheckA[x-1] != -1:    # already have the value, appeared more than once
            print("%s appeared more than once." % x)
            return 0
        CheckA[x-1] = x

    return 1

def Verify():
    A1 = [1,2,3,4]
    A2 = [1,3,4,5]
    A3 = [1,2,3,2]
    A4 = [2,5,3,4,1]
    A5 = [3,4,1,5]
    A6 = [1]

    AA = [A1, A2, A3, A4, A5, A6]
    for a in AA:
        r = PermCheck(a)
        print("%s, result:%d" % (a, r))

Verify()
