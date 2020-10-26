# Find all pairs of 3 in an array that add to n
# e.g. [3,1,2,2,6,4,0,8,5]     N=8
#      then  [2,2,4]. [1,3,4], [0,3,5], [1,2,5], [1,2,5], [2,6,0], [2,6,0]
#
# Time complexity:  O(N*N)
# Space complexity: ?   O(1)
# 


from collections import Counter

def solution(A, N):
    S = sorted(A)
    print(S)
    result = []
    C = Counter(S)

    L = len(A)
    for i in range(L-2):
        for j in range(i+1, L-1):
            remain = N - S[i] - S[j]
            K = S.copy()
            K.remove(S[i]); K.remove(S[j])
            if remain not in K:
                continue
            else:
                if remain < S[j]:
                    continue
                for x in range(Counter(K)[remain]):
                    result.append([S[i], S[j], remain])
    return result

def solution1(A, N):
    ''' This solution is suitable for the case thatthe array elements >=0
    '''
    print(A)
    C = Counter(A)
    # S = sorted(C.items(), key=lambda x:x[0])
    D = {k:v for k,v in sorted(C.items(), key=lambda x:x[0]) if k <= N}   # sorted dict, and cut value > N
    # the couter may not be a good idea, since all element including the repeated value can be used to form the permutation
    # So this isnt a good approach


def test():
    data = [3,1,2,2,6,4,0,8,5, 9, 10]
    r = solution(data, 8)    
    print(r)

test()
