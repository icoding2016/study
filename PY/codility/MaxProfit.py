'''
MaxProfit
Given a log of stock prices compute the maximum possible earning.

An array A consisting of N integers is given. 
It contains daily prices of a stock share for a period of N consecutive days. 
If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, 
then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. 
Otherwise, the transaction brings loss of A[P] − A[Q].

For example, consider the following array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
If a share was bought on day 0 and sold on day 2, 
a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. 
If a share was bought on day 4 and sold on day 5, 
a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. 
Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.

Write a function,

def solution(A)

that, given an array A consisting of N integers containing daily prices of a stock share 
for a period of N consecutive days, returns the maximum possible profit from one transaction 
during this period. The function should return 0 if it was impossible to gain any profit.

For example, given array A consisting of six elements such that:

  A[0] = 23171
  A[1] = 21011
  A[2] = 21123
  A[3] = 21366
  A[4] = 21013
  A[5] = 21367
the function should return 356, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..400,000];
each element of array A is an integer within the range [0..200,000].

'''


# Correctness 100%, Performance 100%
# time complexity:  O(N)
# Key: Kadane's Algorithm
def S(A):
    N = len(A)

    if N==1:
        return 0   

    curMax = 0  # A[1] - A[0] if A[1]>A[0] else 0
    globalMax = curMax
    for i in range(1, N):
        gap = A[i] - A[i-1]
        curMax = max(curMax+gap, gap)
        if curMax > globalMax:
            globalMax = curMax

    return globalMax


# Correctness 100%, Performance 25%
# time complexity:  O(N**2)
def S1(A):
    N = len(A)

    if N==1:
        return 0   
    if N == 2:
        p = A[1]-A[0] 
        return p if p >0 else 0

    PQ = []  # PQ[0] = [ Ap~q... ]
    maxP = 0
    for p in range(N):
        for q in range(p, N):
            profit = A[q] - A[p]
            PQ.append(profit)
            if profit > maxP:
                maxP = profit
    print(PQ)
    return maxP


def solution(A):
    return S(A)

if __name__ == "__main__":

    sample = [ 
        [23171, 21011, 21123, 21366, 21367],    # 356
        [22000, 21583, 21333, 20584, 20018],    # 0       # 1
        [22222],          # 0
        [11111,22222],    # 11111
        [300, 200],  # 0
        [100, 200, 100],  # 100
        [300, 100, 200, 400, 250],  # 300
        # failed case
        #[4, 4, 2, 5, 3, 4, 4, 4], # 3
    ]

    for A in sample:
        print('-'*60)
        r = solution(A)
        print("{} -> {}".format(A, r))

