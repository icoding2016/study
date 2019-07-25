'''
CountDiv
Compute number of integers divisible by k in range [a..b].


Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, 
for A = 6, B = 11 and K = 2, your function should return 3, 
because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
'''


'''
Note:
  1) Take care of the Boundary conditions
  2) Use 'calculation' instead of going through the list.
'''



from utils import Debug


# time complexity: 
def S(A, B, K):
    if A == B:    return 1 if A%K == 0 else 0
    if A == 0 and B > 0:    return int(B/K)+1    # 0 is counted
    
    return int(B/K) - int(A/K) + (1 if A%K == 0 else 0)
    



def solution(A, B, K):
    return S(A, B, K)

if __name__ == "__main__":

    sample = [ 
        [6,11,2],         # 3
        [3,20,6],         # 3
        [0,1,5],          # 1
        [3,3,1],          # 1
        [3,3,2],          # 0
        [3,3,3],          # 1
        [3,3,5],          # 0
        [0,0,1],          # 1
    ]

    for A, B, K in sample:
        print('-'*60)
        r = solution(A, B, K)
        print("{} -> {}".format((A, B, K), r))


