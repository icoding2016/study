# Find the shortest distance among 2 given keys in a list.
# suppose all keys >=0
# Solution 1: Brutal  O(M*N)
# Solution 2: 2 pointer (sliding)   O(M+N)
# 
# # 


import sys

L=[3, 165, 90, 1, 88, 72, 33, 49, 3, 88, 111, 90]
D=dict()

def solution(L, x, y):
    # build dict 
    for i in range(len(L)):
        k = L[i]
        if k in D:
            D[k].append(i)
        else:
            D[k] = [i]
    #gap = getDistance(D, x, y)
    gap = getDistance2(D, x, y)
    print('-'*80)
    print(gap)   


# brutal force
def getDistance(d, a,b):
    if a not in d:
        return None
    if b not in d:
        return None
    
    gap = None
    for i in d[a]:
        for j in d[b]:
            g = abs(i-j)
            if not gap or g < gap:
                gap = g
    return gap

# 'Slid and compare' (2 pointers)
#       <-list1 
#   list2->
def getDistance2(d, a,b):
    d1 = d[a];  
    # # d1.sort()    # no need sort, the indexes are already in order due to the way we create the dict list
    d2 = d[b];  
    # d2.sort()      # no need sort

    i = 0
    j = len(d2)-1
    mingap = sys.maxsize
    pregap = None 
    flag = True
    while i<len(d1) and i>=0 and j<len(d2) and j>=0:
        gap = abs(d1[i] - d2[j])
        if gap < mingap:
            mingap = gap
        if flag:
            i += 1
            flag = False
        else:
            j -= 1
            flag = True
        print(pregap, gap, mingap)
        if pregap:
            if gap > pregap:
                break
        pregap = gap
    return mingap


if __name__ == "__main__":
    solution(L, 3, 88)
    solution(L, 90, 88)

