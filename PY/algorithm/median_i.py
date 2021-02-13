# median finding Algorithm
# Given an array A = [1,...,n]A=[1,...,n] of nn numbers and an index i,i, where 1 ≤ i ≤ n,1≤i≤n, find the ith smallest element of A.
# 


# T(NlogN)
def median_i(A:list, I:int):
    if I > len(A):
        return None
    
    left = 0
    right = j = len(A)-1
    pivot = A[0]
    i = left+1
    while i < j:
        while i <= right and A[i]<pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i],A[j]=A[j],A[i]
            #print(A,I)
    if A[j]<pivot:                # note: don't foget the condition 
        A[0],A[j]=A[j],A[0]       # switch the A[j] with pivot. pivot is A[0] in this case, so we pick the 'small' (A[j]). 
    #print(A, I, pivot)
    if I-1 == j:
        return pivot
    elif I-1 < j:
        return median_i(A[:j], I)
    else:
        return median_i(A[j+1:], I-j-1)



def test_fixture():
    testdata = [  # (input, expect),
        (([7,3,5,1,4,6,8,2], 3), 3),
        (([3,5,1,4,7,6,8,2], 3), 3),
        (([3,5,1,4,7,6,8,2], 5), 5),
        (([3], 1), 3),
   ]

    for i in range(len(testdata)):
        ret = median_i(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t expect {}".format("testdata[i][0]", ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))


import timeit
def test():
    #s = Solution()
    test_fixture()

test()
