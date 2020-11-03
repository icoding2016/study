# Merge Sort
# - Split the array into 2 parts from the middle, 
# - apply merge sort to left and right sides (recursively).
# - Then merge the two parts
#
# Time Complexity:  O(NlogN)
#     N + (N/2 + N/2) + (N/4 + N/4 + N/4 + N/4) ...  <repeat logN) = NlogN
# Space Compexity:  O(N) worst case     !! not O(NlogN)
#     In below case of Python implementation,   each merge_sort: new allocations are 2 args A[:mid], B[mid:], output[]
#     so each level of spliting -- space 3N,  but the 2 args and l[] & r[] are only temporary for current merge_sort,  
#                                  So it is always 3N  -->  O(N)
#                             N 
#                   3N/2      +      3N/2
#              3N/4  +  3N/4      3N/4 + 3N/4
#            ...
#     But in some other implimentations, we can pass in the sub-list by reference. so it could be 1xN.
#

from typing import TypeVar


T = TypeVar('T')

def merge_sort(A:list[T]) -> list[T]:
    if len(A) < 2:
        return A
    mid = int(len(A)/2)
    l = merge_sort(A[:mid])
    r = merge_sort(A[mid:])
    return merge(l, r)

def merge(A:list[T], B:list[T]) -> list[T]:
    i = j = 0
    output = []
    while i < len(A) or j < len(B):
        if i >= len(A):  # A out
            output.append(B[j])
            j += 1
            continue
        if j >= len(B):  # B out
            output.append(A[i])
            i += 1
            continue
        if A[i] < B[j]:
            output.append(A[i])
            i += 1
        else:
            output.append(B[j])
            j += 1
    return output
        


def test():
    A = [7,4,5,1,3,9,6,8,10,2,0]
    print(A)
    print('-> ', merge_sort(A))


test()
