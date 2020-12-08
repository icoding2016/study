# Given an array of integers find indices I < j < k such that a[I] < a[j] < a[k]
# 

from collections import defaultdict


# solution1 : 
#   sort, iterate
#   it doesn't consider the duplicate
def solution1(A):
    if len(A) < 3:
        return []
    L = [(A[i],i) for i in range(len(A))]
    #print(L)
    S = sorted(L, key=lambda x:x[0])
    answer = []
    for i in range(0, len(A)-2):
        for j in range(i+1, len(A)-1):
            for k in range(j+1, len(A)):
                answer.append((S[i][1], S[j][1], S[k][1]))
    return answer


# consider duplicates
# T((N-2)^3)
def solution2(A):
    if len(A) < 3:
        return []
    D = defaultdict(list)
    output = []
    for i,n in enumerate(A):
        D[n].append(i)
    D = {n:D[n] for n in sorted(D)}   # sort by nums
    nums = [n for n in D]
    N = len(D)
    for ii in range(N-2):
        #print(a, D[a])
        for idx1 in D[nums[ii]]:
            for jj in range(ii+1, N-1):
                for idx2 in D[nums[jj]]:
                    for kk in range(jj+1,N):
                        for idx3 in D[nums[kk]]:
                            output.append([idx1, idx2, idx3])
    return output




def test(A):
    answer1 = solution1(A)
    print('solution1:',answer1)
    answer2 = solution2(A) 
    print('solution2:', answer2)


test([3,2,1])
test([3,2,4,1])
test([2,3,1,1,3])