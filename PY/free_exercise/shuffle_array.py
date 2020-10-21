# shuffle an array, make sure every element is not on the previous position
#
# Ideas:
#  1) swapping all item by random pairing
#     form pairs for all element, swap, if odd number, do one more swap    
#     use set to record the indexes that haven't been swapped
#   

import random

def shuffle(A):
    '''very simple way, to swap the neighbor items, not randomly
    '''
    remain_id = set([x for x in range(len(A))])

    A_bak = A.copy()    
    while len(remain_id) > 0:
        i = remain_id.pop()
        if len(remain_id) > 0:
            j = remain_id.pop()
            A[i], A[j] = A[j], A[i]
        else:
            A[i], A[0] = A[0], A[i]

def shuffle2(A):
    '''shuffle in random
    '''
    remain_id = set([x for x in range(len(A))])

    while len(remain_id) > 0:
        i = random.choice([x for x in remain_id])
        remain_id -= { i }
        if len(remain_id) > 0:
            j = random.choice([x for x in remain_id])
            remain_id -= {j}
        else:
            j = int(random.random()*(len(A)-1))
            if j == i:
                j = i + 1
        A[i], A[j] = A[j], A[i]


def verify(A, B):  # may not work properly when there is no repeating values
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] == B[i]:
            return False
    return True

def test(A):
    B = A.copy()
    shuffle2(A)
    r = verify(A, B)
    print(r)
    print('  ', B)
    print('->', A)


test([1,2,3,4,5,6,7,8,9])
test([1,2,3,4,5,6,7,8])
