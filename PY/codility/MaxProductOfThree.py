'''
MaxProductOfThree
Maximize A[P] * A[Q] * A[R] for any triplet (P, Q, R).


A non-empty array A consisting of N integers is given. 
The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.

Write a function:

def solution(A)

that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].

'''


'''
Note:
  Key: use sort to simplify logic
  Considerations:
    - negative:    +++, --+ > 0 > -++, ---
    - 0*anything = 0
    - sort
    - N=3, N>3

    so for the sorted list S. the last 3 items' possibility:   [.,x,y,z]
    .+++,  
    .0++, 
    .-0+, 
    .--0, 
    .---,
    .-++, 
    .--+, 

'''




from utils import Debug

# time complexity:  O(N * log(N))
def S(A):
    N = len(A)
    if N == 3:    return A[0]*A[1]*A[2]
    
    S = sorted(A)

    def triplet(x,y,z):
        return S[x]*S[y]*S[z]

    # N > 3
    if S[N-3] > 0:           # .+++
        if N < 5:
            return triplet(N-1, N-2, N-3)
        else:
            return max(triplet(N-1, N-2, N-3), triplet(0,1,N-1))
    elif S[N-3] == 0:         # .0++ =>  either [.0++] or [--..+]
        if N < 5:
            return 0
        else:
            return triplet(0, 1, N-1)
    elif S[N-2] == 0:         # .-0+
        return triplet(0, 1, N-1)
    elif S[N-1] == 0:         # .--0
        return 0
    elif S[N-3] < 0 and S[N-2] > 0:   # -++
        return triplet(0,1,N-1)
    elif S[N-2] < 0 and S[N-1] > 0:   # --+
        return triplet(0, 1, N-1)
    else:                     # .---
        return triplet(N-1,N-2,N-3)



# time complexity: 
# Task Score 55%, Correctness 75%, Performance 40%
#   some logic wrong (missing one branch)
def S1(A):
    N = len(A)
    if N == 3:    return A[0]*A[1]*A[2]
    
    S = sorted(A)

    def triplet(x,y,z):
        return S[x]*S[y]*S[z]

    # N > 3
    if S[N-3] > 0:           # .+++
        return triplet(N-1, N-2, N-3)
    elif S[N-3] == 0:         # .0++ =>  either [.0++] or [--..+]
        if N < 5:
            return 0
        else:
            return triplet(0, 1, N-1)
    elif S[N-2] == 0:         # .-0+
        return triplet(0, 1, N-1)
    elif S[N-1] == 0:         # .--0
        return 0
    elif S[N-3] < 0 and S[N-2] > 0:   # -++
        return triplet(0,1,N-1)
    elif S[N-2] < 0 and S[N-1] > 0:   # --+
        return triplet(0, 1, N-1)
    else:                     # .---
        return triplet(N-1,N-2,N-3)
    



def solution(A):
    return S(A)

if __name__ == "__main__":

    sample = [ 
        [4,2,1,3],         # 24
        [1,0,2,3],         # 6 
        [4,1,3,-2],        # 12
        [3,0,-2,1],        # 0
        [-4,1,3,-2],       # 24
        [-2,0,1,2,-3],     # 12
        [-1,-3,0,-4],      # 0
        [-2,-5,-3,-1],     # -6
        # Failed testcase in codility
        [-4, -6, 3, 4, 5], # 120
    ]

    for A in sample:
        print('-'*60)
        r = solution(A)
        print("{} -> {}".format(A, r))

