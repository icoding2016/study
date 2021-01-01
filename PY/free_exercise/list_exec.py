# Quesitons
# 1.  A array contains the number(1~n), the len(a)=n
#     There are one missing number and one repeated number
#     Find out the missing and repeated ones

from collections import defaultdict


def find_duplicate(a:list[int]) -> int:
    d = {}
    for x in a:
        if x in d:
            return x
        else:
            d[x] = 1
    return None

def find_missing(a:list[int]) -> int:
    return sum([x for x in range(1, len(a)+1)]) - sum(set(a))


def find_missing_dup(data:list[int])->(int, int):
    s1 = set([i for i in range(1,len(data)+1)])
    s2 = set(data)
    miss = s1 - s2
    dup = sum(data) -  sum(s2)
    return miss, dup


def find_missing_dup2(data:list[int])->(int, int): 
    c = defaultdict(int)
    dup = None
    for d in data:
        c[d] += 1
        if c[d] > 1:
            dup = d
    N = len(data)
    missing = int(N*(N+1)/2) - sum(c)
    return missing, dup

def merge_list(l1:list, l2:list)->list:
    ''' merge l2 to l1 if the elements in l2 is not in l1'''
    return l1 + [x for x in l2 if x not in l1]

def test():
    A = [1,2,3,4,5,6,7,8,9,10]
    A1 = [1,2,3,8,5,6,7,8,9,10]
    A2 = [10,2,3,4,5,6,7,8,9,10]
    print(find_duplicate(A1))
    print(find_missing(A1))
    print(find_duplicate(A2))
    print(find_missing(A2))    
   
    r = 100
    mis = 30
    dup = 51
    data = [i for i in range(1,r+1) if i != mis] + [dup]
    print(find_missing_dup(data))
    print(find_missing_dup2(data))

    l1 = [1,1,2,3]
    l2 = [3,4,5]
    print('merge {},{} -> {}'.format(l1, l2, merge_list(l1, l2)))

test()
