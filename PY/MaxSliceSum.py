'''
MaxSliceSum
Find a maximum sum of a compact subsequence of array elements.


A non-empty array A consisting of N integers is given. 
A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. 
The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].

'''


'''
Note:
  - Kadane's Algorithm.
  - Pay attention to the initialization for both curMax and globalMax.
'''



# Connectness 75%, Performance 80%
# time complexity: 
def S(A):
    N = len(A)
    
    if N == 1:
        return A[0]

    gMax = A[0]
    curMax = A[0]

    for i in range(1, N):
        curMax = max(curMax+A[i], A[i])
        if not gMax or (gMax and gMax < curMax):
            gMax = curMax

    return gMax


# Connectness 75%, Performance 80%
# time complexity: 
def S1(A):
    N = len(A)
    
    if N == 1:
        return A[0]

    gMax = None                    # <-- mistake here. gMax is not initialized with the 1st value in loop
    curMax = A[0]

    for i in range(1, N):
        curMax = max(curMax+A[i], A[i])
        if not gMax or (gMax and gMax < curMax):
            gMax = curMax

    return gMax



def solution(A):
    return S(A)

if __name__ == "__main__":

    sample = [ 
        [3,2,-6,4,0],     # 5
        [1],              # 1
        [1,2],            # 3
        [-2,1],           # 1
        [-1,2,-2],        # 2
        [-1,1,-1,1,-1],   # 1
        [1,0,-1,2,0,1],   # 3
        [2,0,-1,1,2,0],   # 4
        # Failed case
        [1,-2],           # 1
    ]

    for A in sample:
        print('-'*60)
        r = solution(A)
        print("{} -> {}".format(A, r))

