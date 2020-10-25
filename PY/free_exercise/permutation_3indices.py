# Given an array of integers find indices I < j < k such that a[I] < a[j] < a[k]
# 
# solution1 : 
#   sort, iterate
#   

def solution1(A):
    if len(A) < 3:
        return []
    L = [(A[i],i) for i in range(len(A))]
    print(L)
    S = sorted(L, key=lambda x:x[0])
    answer = []
    for i in range(0, len(A)-2):
        for j in range(i+1, len(A)-1):
            for k in range(j+1, len(A)):
                answer.append((S[i][1], S[j][1], S[k][1]))
    return answer


def test(A):
    answer = solution1(A) 
    for x in answer:
        print(x)   


test([3,2,1])
test([3,2,4,1])