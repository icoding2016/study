'''
Dominator
Find an index of an array such that its value occurs at more than half of indices in the array.


An array A consisting of N integers is given. 
The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A 
(namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)

that, given an array A consisting of N integers, 
returns index of any element of array A in which the dominator of A occurs. 
The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
'''




# time complexity:  O(N*log(N)) or O(N)
def S(A):
    N = len(A)
    if N == 0:
        return -1
    if N == 1:
        return 0
    

    class DominatorCounter(object):
        def __init__(self, value):
            self.value = value
            self.count = 0
            self.index = []
        def add(self, index):
            self.count += 1
            self.index.append(index)
    
    D = {}
    for i in range(N):
        if A[i] not in D.keys():
            d = DominatorCounter(A[i])
            d.add(i)
            D[A[i]] = d
            #print("add: {}-{}".format(A[i], d.count))
        else:  # exist
            d = D[A[i]]
            d.add(i)
            #print("exist: {}:{}".format(d.value, d.count))

    for v in D.values():
        if v.count > int(N/2):
            return v.index[0]
    return -1
    

# Correctness issue:  the condition: 'more than half'
# time complexity:  O(N*log(N)) or O(N)
def S1(A):
    N = len(A)
    if N == 0:
        return -1
    if N == 1:
        return 0
    

    class DominatorCounter(object):
        def __init__(self, value):
            self.value = value
            self.count = 0
            self.index = []
        def add(self, index):
            self.count += 1
            self.index.append(index)
    
    D = {}
    for i in range(N):
        if A[i] not in D.keys():
            d = DominatorCounter(A[i])
            d.add(i)
            D[A[i]] = d
            #print("add: {}-{}".format(A[i], d.count))
        else:  # exist
            d = D[A[i]]
            d.add(i)
            #print("exist: {}:{}".format(d.value, d.count))

    for v in D.values():
        if v.count > int((N+1)/2):          # <<---- wrong
            return v.index[0]
    return -1
    



def solution(A):
    return S(A)

if __name__ == "__main__":

    sample = [ 
        [],            # -1           -> -1
        [3],           # 0            -> 0
        [1,2],         # -1           -> -1
        [1,2,1],       # 0,2          -> 0
        [1,1,1,1,1],   # 0,1,2,3,4    -> 0
        [3,1,1,2,1],   # 0,1,2,4      -> 1
    ]

    for A in sample:
        print('-'*60)
        r = solution(A)
        print("{} -> {}".format(A, r))

