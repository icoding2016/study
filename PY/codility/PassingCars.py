'''
PassingCars
Count the number of passing cars on the road.


A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
'''


'''
NOTE:

Thought: count how many '1's after each 0, add them up
    e.g.        [1, 0, 0, 1, 0, 1, 0]    # A
    '1's behind [2, 2, 2, 1, 1, 0, 0]    # count_of_one behind current position
                    ^  ^     ^
S1() has performance issue
    Task Score 70%, Correctness 100%, Performance 40%
    The reason is, the coding missed one case: "The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000"
'''


from utils import Debug


def S(A):
    N = len(A)
    if N <= 1:
        return 0
    
    # count '1's (go backwards)
    count_of_one = [0]*N
    counter = 0
    total = 0    
    for i in range(N-1):
        if A[N-i-1] == 1:
            counter +=1
        count_of_one[N-i-1-1] = counter

    total = 0    
    for i in range(N-1):
        if A[i] == 0:
            pairs = count_of_one[i]
            total += pairs
            if total > 1000000000:
                return -1
    return total


def S1(A):
    N = len(A)
    if N <= 1:
        return 0
    
    # count '1's (go backwards)
    count_of_one = [0]*N
    counter = 0
    for i in range(N-1):
        if A[N-i-1] == 1:
            counter +=1
        count_of_one[N-i-1-1] = counter

    Debug("count_of_one: {}".format(count_of_one))    

    total = 0    
    for i in range(N-1):
        if A[i] == 0:
            pairs = count_of_one[i]
            total += pairs
    return total


def solution(A):
    return S(A)

if __name__ == "__main__":

    sample = [ 
        [0,1,0,1,1],      # 5
        [1,0,0,1],        # 2
        [1,1,1,1,1],      # 0
        [0],              # 0
        [1],              # 0
        [0,1],            # 1
        [1,0],            # 0 
    ]

    for A in sample:
        print('-'*60)
        r = solution(A)
        print("{} -> {}".format(A, r))

