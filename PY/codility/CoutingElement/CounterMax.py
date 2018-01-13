'''
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty zero-indexed array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty zero-indexed array A consisting of M integers, returns a sequence of integers representing the values of the counters.

The sequence should be returned as:

a structure Results (in C), or
a vector of integers (in C++), or
a record Results (in Pascal), or
an array of integers (in any other programming language).
For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Assume that:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
Complexity:

expected worst-case time complexity is O(N+M);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.

'''

def CounterMax1(N,A):        # Correctness 100%, performance 40%
    Counter = [0] * N
    for K in range(len(A)):
        X = A[K]
        if X < 1 or X > N+1:
            print("X(%d) out of range." % X)
            continue
        if X <= N:
            Counter[X-1] += 1
            print(Counter)
        else:
            maxInC = max(Counter)
            for i in range(N):
                Counter[i] = maxInC
                print(Counter)

    return Counter

def CounterMax2(N,A):        # Correctness 100%, performance 60% ( time complexity:O(N*M) )
    Counter = [0] * N
    maxInC=0
    M = len(A)
    for K in range(M):
        X = A[K]
        if X < 1 or X > N+1:
            #print("X(%d) out of range." % X)
            continue
        if X <= N:
            Counter[X-1] += 1
            if maxInC < Counter[X-1]:
                maxInC = Counter[X-1]
            #print(Counter)
        else:
            Counter = [maxInC]*N
            #print(Counter)

    return Counter

def CounterMax(N,A):        # Correctness 100%, performance % ( time complexity: )
    Counter = [0] * N
    maxInC=0
    for K in range(len(A)):
        X = A[K]
        if X < 1 or X > N+1:
            #print("X(%d) out of range." % X)
            continue
        if X <= N:
            Counter[X-1] += 1
            if maxInC < Counter[X-1]:
                maxInC = Counter[X-1]
            #print(Counter)
        else:
            Counter = [maxInC]*N
            #print(Counter)

    return Counter

def Verify():
    X=[5,5,3,1]
    A1 = [3,4,4,6,1,4,4]      #(3, 2, 2, 4, 2)
    A2 = [1,4,2,3,1,7,2]            #3
    A3 = [2,3,3]                #-1
    A4 = [1]
    A5 = [6]
    AA=[A1,A2,A3,A4,A5]
    for i in range(len(AA)):
        r = CounterMax(X[i], AA[i])
        print("---------%s, result:%s" %(AA[i], r))

Verify()
