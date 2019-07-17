"""
MaxCounters
Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.


You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
"""


'''
NOTE:
  Need taking care of performance
  e.g.   
  S1() only got 40% in performance score:
       Task Score:66%, Correctness 100%, Performance 40%
  S2() optimized performance by 
       1) recording cur-max value instead of max([]) each time
       2) skip counter 'initializing to max' when there is continuous 'max'
       But still failed performance (score 60% only)
  S()  1),2) and
       3) change the list initialization method from list comprehension to []*n, greatly improved performance
  to achieve performance score 100%, all the optimizations are required.


List initialization:
e.g.
>>> timeit.timeit('l=[1 for i in range(2000)]')
38.3013196529937
>>> timeit.timeit('l=[1]*2000')
3.1312345970072784
'''

from utils import Debug



def S(N, A):
    M = len(A)
    counter = [0] * N

    maxflag = False
    curMax = 0
    for a in A:
        if a  <= N:
            counter[a-1] += 1
            if curMax < counter[a-1]:
                curMax = counter[a-1]
            maxflag = False
        else:
            if not maxflag:
                counter = [curMax] * N
                maxflag = True
    return counter


def S2(N, A):
    M = len(A)
    counter = [ 0 for i in range(N)]

    maxflag = False
    curMax = 0
    for a in A:
        if a  <= N:
            counter[a-1] += 1
            if curMax < counter[a-1]:
                curMax = counter[a-1]
            maxflag = False
        else:
            if not maxflag:
                counter = [ curMax for i in range(N)]
                maxflag = True
    return counter


def S1(N, A):
    M = len(A)
    counter = [ 0 for i in range(N)]

    for a in A:
        if a  <= N:
            counter[a-1] += 1
        else:
            m = max(counter)
            counter = [ m for i in range(N)]
    return counter
    

def solution(N, A):
    return S(N, A)


if __name__ == "__main__":

    sample = [ 
        (5, [3,4,4,6,1,4,4]),  # [3,2,2,4,2]
        (3, [4,1,3,2]),        # [1,1,1]
        (1, [1,2,1,2,2.2]),    # [2]
        (1, [2,2,2]),          # [0]
        (1, [1,1,1]),          # [3]
        (1, [1]),              # [1]
        (1, [2]),              # [0]
    ]

    for N, A in sample:
        print('-'*60)
        r = solution(N, A)
        print("{} -> {}".format((N,A), r))

