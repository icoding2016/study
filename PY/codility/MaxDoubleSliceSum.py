'''
MaxDoubleSliceSum
Find the maximal sum of any double slice.


A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of 
A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, 
returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
'''

'''
Notes:
  1. Thought: maxDoubleSlice = max(SingleSlice[x,z] - A[X] -A[Y] - A[Z])
                             = max(SingleSlice[x,z] - A[X] - A[Z]) - min(A[x+1,z-1])
     (z-x>2)
  2. N>=3, Boundery case [a,b,c] --> maxDoubleSlice = 0   ???
'''

# Connectness %, Performance %
# time complexity: 
def S(A):
    N = len(A)

    if N < 3:
        raise(ValueError)
        return
    if N == 3:
        return 0    # ???? 

    curMax = 0  #sum(A[0:3])           # for maxSingleSlice(A[x,z])
    globalMaxSS = curMax           # for maxSingleSlice(A[x,z])
    globalMaxDS = 0                # maxDoubleSlice
    minY = A[1]                    # min(A[x+1,z-1])
    x = 0
    z = 2
    for i in range(3,N):
        tmp = curMax + A[i-1]         # calculate within [x+1,z-1]
        
        if tmp > sum(A[i-2:i+1]):
            curMax = tmp
            z = i
        else:
            curMax = sum(A[i-2:i+1])
            x = i-2
            z = i
        minY = min(min(A[x+1:z]), minY)
        if curMax > globalMaxSS:
            globalMaxSS = curMax

        globalMaxDS = globalMaxSS - A[x] - A[z] - minY
        print("x={},z={},minY={},maxSS={},maxDS={}".format(x,z,minY,globalMaxSS, globalMaxDS))

    return globalMaxDS


def solution(A):
    return S(A)


if __name__ == "__main__":

    sample = [ 
        [3,2,-6,-1,4,5,-1,2],     # 17
        [1,1,1],                  # 0 (?)
        # Failed case
        
    ]
    sample_bakup = [
        [1,2,3,2,1],              # 5
        [5,1,-1,3],               # 1
        [-1,1,-1,1,-1,1],         # 2
        [1,0,-1,2,0,1],           # 2
        [2,0,-1,1,2,0],           # 3
    ]

    for A in sample:
        print('-'*60)
        r = solution(A)
        print("{} -> {}".format(A, r))

