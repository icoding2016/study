# median finding Algorithm
# Given an array A = [1,...,n]A=[1,...,n] of nn numbers and an index i,i, where 1 ≤ i ≤ n,1≤i≤n, find the ith smallest element of A.
# 
# A typical case is to find the median value of an unsorted array. 
# - pick a pivot, put smaller to the left, bigger to the right.
# - if pivot in the middle 'len(A)/2', then pivot is the median
# - if pivot < middle position (median is in the right side), keep searching in the right
# - if pivot > middle position (median is in the left side), keep searching in the left
# - When the pivot (A[i]) is done, Recurse left A[:i] or right[]
# - When exiting 'while i<j', it is always i>j, since i seeks bigger value, j seek smaller value, it cannnot be the same.
#   so if A[i]>pivot when exit, i need move back to i-1, 
#   The A[i] (adjusted if need) should swap with pivot --- A[i] is the pivot after one round, this positin is sorted.
# Note:
# - the median of 1~N is (N+1)/2, so index is len(N)/2 of [0,N-1]
# - When len(A) < 3, we can directly handle the sort and median
# 
# Time Complexity:  
#     Worst-case:O(N*N),  best(LogN), 
# Space Complexity:
#     

def median_finding(A:list, k:int =None):
    '''
        A: the array to search
        k: the index of the 'middle position'
    '''
    #print(A, k)
    if k is None:
        k = int(len(A)/2)
    if len(A) <= 2:
        return sorted(A)[k]
     
    pivot = A[0]
    i = 1
    j = len(A)-1
    while i < j:
        while i < j and A[i] < pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    if i > j:    # if A[i] > pivot:
        i -= 1
    if A[i] < pivot:
        A[i],A[0] = A[0],A[i]
    if i == k:
        return pivot
    if i < k:
        return median_finding(A[i+1:], k - i -1)
    else:  # i>k
        return median_finding(A[:i], k)


def median_finding_by_sort(A):
    return sorted(A)[int(len(A)/2)]

def mean(A):
    sum=0
    for x in A:
        sum += x
    return sum/len(A)

def test(A):
    print('-'*40)
    print(A)
    r = median_finding(A)
    print('median:', r,end=' vs:')
    print(median_finding_by_sort(A), end='  ')   # checking with another algorithm
    print('mean:', mean(A))



test([3,5,1,7,2,9,6,4,8,10,11,12,13])
test([3,5,1,7,2,9,6,4,8,10,11,12])
test([4,1,3,6,2,5,7])
test([6,5,4,3,2,1])
test([1,2,3,4])
test([3,1,2])
test([1,2])
test([1])


