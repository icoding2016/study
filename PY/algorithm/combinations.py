# Giving N elements and pick K out of them A[N]
# generating all combinations (no matter the order)
# 
# A good coding reference: https://www.youtube.com/watch?v=VyXDQxuIwPU
#
# 
# Time Complexity:
#   1. Mathematically..   N choose K combination:  C(n,k) = n!/((n-k)!*k!)                <-- Accurate one
#                         [How]: possibilities: n*(n-1)*(n-2)*..*(n-k+1) -> n!/((n-k)!*k!)
#   2. O() by recursive iteration
#                         O(n*(-1)*..(n-k+1))=>O(n^k)                                     <-- rough O()
#   3. O() by Binary selection:  
#                         For each of N elelment, we can choose (1) or no-choose (0)
#                         So this form a  N height b-tree
#                         O(2+2^2+...2^n) => O(2^n)                                       <-- rough O()
#   Which is O() more accurate?


import itertools
from call_counter import call_counter, show_call_counter


# T(N^K)
# S(K*N)    K level of stacks, 2*N memory for each call.
@call_counter
def combinations_iter(A:list, K:int, picked:list=None) -> None:
    if None == picked:
        picked = []
    if K == len(picked):
        yield picked
        return
    if not len(A):
        return
    
    for c in combinations_iter(A[1:], K, picked+[A[0]]):
        yield c
    for c in combinations_iter(A[1:], K, picked):
        yield c






def test():
    A = [1,2,3,4]
    print('standard:')
    print([c for c in itertools.combinations(A, 2)])

    print('combinations_iter')
    print([c for c in combinations_iter(A, 2)])
    show_call_counter()

test()

