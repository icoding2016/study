A = [3, 8, 9, 7, 6]

def solution(A, K):
    # write your code in Python 2.7
    l = len(A)
    B = A.copy()

    for i in range(0 ,l):
        j = ( i +K ) %l
        print("{} -> {}".format(i ,j))
        B[i] = A[j]

    return B


