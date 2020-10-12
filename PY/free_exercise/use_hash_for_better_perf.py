# Given an array of distinct integer values, count the number of pairs of integers that
# have difference k. 
# # For example, given the array { 1, 7, 5, 9, 2, 12, 3} and the difference
# k = 2,there are four pairs with difference2: (1, 3), (3, 5), (5, 7), (7, 9).
#
# Solution 1: brutal force O(N^2)
#
# Solution 2: Sort & check v[i+1] - v[i]  -- O(N*logN)
#
# Solution 3: Hash-table -- O(N)
#   Throw all elements into a hash table, then check: for each element v if v+k or v-k exist.
#

A = [1, 7, 5, 9, 2, 12, 3]
K = 2

def solution1(A, K):
    if len(A) < 2:
        return []
    result = list()
    for x in A:
        for y in A:
            if y - x == K:
                result.append((x, y))
    print(result)
    return result

def solution2(A: list, K: int) -> list:
    if len(A) < 2:
        return []
    result = list()
    AA = sorted(A.copy())
    for i in range(len(AA)-1):
        if AA[i] + K in AA:
            result.append((AA[i], AA[i]+K))
    print(result)
    return result

def solution3_a(A: list, K: int) -> list:
    if len(A) < 2:
        return []
    result = list()
    #HA = {k:v for k,v in zip(A, [x for x in map(hash,A)])}
    HA = A
    for x in HA:
        if x + K in HA:   # No, list() is not hash table, so not O(1)
            result.append((x, x + K))
    print(result)
    return result

def solution3(A: list, K: int) -> list:
    if len(A) < 2:
        return []
    result = list()
    #HA = {k:v for k,v in zip(A, [x for x in map(hash,A)])}
    HA = {k:1 for k in set(A)}
    for x in HA.keys():
        if x + K in HA.keys():   # No, list() is not hash table, so not O(1)
            result.append((x, x + K))
    print(result)
    return result

if __name__ == "__main__":
    solution1(A, K)
    print("-"*80)
    solution2(A, K)
    print("-"*80)
    solution3(A, K)


