'''
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7 
P = 2, difference = |4 − 9| = 5 
P = 3, difference = |6 − 7| = 1 
P = 4, difference = |10 − 3| = 7 
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
'''


from utils import Debug


# time complexity: O(N)
def S(A):
    N = len(A)
    B = []
    adding = 0
    for i in range(N):
        adding += A[i]
        B.append(adding)          # B[A0, (A0+A1), .. (A0+..An-1)]
    Total = B[N-1]

    Debug(B)
    Debug("total: %i" % Total)

    #Gap = [Total-B(i)-B[i] for i in range(len(B))]
    #m = min([abs(Total-B[i]*2) for i in range[N-1]])
    diff = [abs(Total-x*2) for x in B[:(N-1)]]
    Debug(diff)
    m = min(diff)
    return m





def solution(A):
    return S(A)

if __name__ == "__main__":

    sample = [ 
        [-2,-5,3,1],        # 3
        [3,1,2,4,3],        # 1
        [1,2],              # 1
        [-1000, 1000],      # 2000
    ]

    for A in sample:
        print('-'*60)
        r = solution(A)
        print("{} -> {}".format(A, r))




