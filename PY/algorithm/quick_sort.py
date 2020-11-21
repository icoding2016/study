# Quick sort



# take A[low] as pivot
def partition(A, low, high):
    '''
        low: the lower index of the partition of A
        high: the higher index of the partition of A

        In this implementation, i index goes from left to right, pointing to the right end of 'small' elements.
        j index goes from right to left, pointing to the left end of the 'big' elements.
    '''
    if high == low:
        return low
    if high - low < 2:
        if A[high] < A[low]:
            A[low], A[high] = A[high], A[low]
        return low
    P = A[low]    # choose the left end element as the pivot
    i=low+1
    j=high
    while j > i:      
        while j>i and A[j] > P:
            j -= 1
        while j>i and A[i] <= P:     # one of the 2 compare is <=P, one is <P
            i += 1
        if i < j:
            A[i],A[j] = A[j],A[i]
    if j <= i and A[low] > A[i]:    # beware: the A[low]/[high] condition, the pivot may not be bigger than the last A[i]
        A[low],A[i] = A[i], A[low]
    return i
        

# take A[mid] as pivot
def partition2(A:list, left:int, right:int) -> int:
    if left == right:
        return left
    mid = left + int((right - left)/2)
    P = A[mid]
    i = left
    j = right
    print(A[i:j+1])
    while i < j:
        while i < right and (A[i] < P or i == mid):
            i += 1
        while j > left and (A[j] >= P or j == mid):
            j -= 1 
        if i < j and A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
            print('swap {},{} P={}'.format(A[i], A[j], P))
    if i != mid:
        A[i], A[mid] = A[mid], A[i]
        print(i)
    return i

def quick_sort(A, low, high):
    #print(A[low:high], low, high)
    if high - low <2:
        return
    i = partition(A, low, high)
    #i = partition2(A, low, high)
    if i > low:
        quick_sort(A, low, i-1)
    if i+1 < high:
        quick_sort(A, i+1, high)
    return



if __name__ == "__main__":
    A = [2,8,7,1,3,5,6,4]
    A1 = [3,3,3,3,3,3,3,1]
    A2 = [1,2,3,4,5,6]
    A3 = [2,2,2,2,2,2]
    A4 = [1,3,3,3,3,3]

    print(A)
    quick_sort(A, 0, len(A)-1)
    print('>>',A)

    print(A1)
    quick_sort(A1, 0, len(A1)-1)
    print('>>',A1)

    print(A2)
    quick_sort(A2, 0, len(A2)-1)
    print('>>',A2)

    print(A3)
    quick_sort(A3, 0, len(A3)-1)
    print('>>',A3)

    print(A4)
    quick_sort(A4, 0, len(A4)-1)
    print('>>',A4)
