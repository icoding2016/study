# -*- coding: utf-8 -*-


'''
MissingInteger
-- Find the minimal positive integer not occurring in a given sequence.

Write a function:

def solution(A)
that, given a non-empty zero-indexed array A of N integers,
returns the minimal positive integer (greater than 0) that does not occur in A.

For example, given:

  A[0] = 1
  A[1] = 3
  A[2] = 6
  A[3] = 4
  A[4] = 1
  A[5] = 2
the function should return 5.

Assume that:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.


'''

A1=[1,3,6,4,1,2]        #5
A2=[5,7,6,8,3,3,9,11]   #1
A3=[3]                  #1
A4=[2,3,4,5]            #1
A5=[-1,7,6,5,4,3,3,1]   #2
A6=[1]                  #2
A7=[-1]                 #1
A8=[-2147483648, -1] #1
A9=[-2147483648, 1]  #2
A10=[-2147483648, -2, 1, 3,4,9, 2147483647] #2


def MissingInteger1(A):        # Failed in test
    # write your code in Python 2.7
    S = set(A)
    m1 = min(min(S),1)
    m2 = max(S)
    for i in range(m1, m2 + 1):
        if i > 0 and i not in S:
            print("{}: m=({},{}), i={}".format(S, m1, m2, i))
            return i
    return max(i+1,1)
    '''
    FAILED AT test: extreme_min_max_int MININT and MAXINT (with minus)
    stderr:
    Traceback (most recent call last):
      File "exec.py", line 111, in <module>
        main()
      File "exec.py", line 86, in main
        result = sol.solution ( A )
      File "/tmp/solution.py", line 9, in solution
        for i in range(m1, m2 + 1):
    MemoryError
    '''

def MissingInteger2(A):    # Failed in test
    # write your code in Python 2.7
    S = set(A)

    m1 = min(S)
    m2 = max(S)

    i = 0
    if m1 <=0 and m2<=0:
        i = 0; m2=0
    elif m1 <=0 and m2 >0:
        i = 0

    #print("m1: {}, m2: {}, i:{}".format(m1, m2, i))
    while (i<=m2):
        if i > 0 and i not in S:
            print("{}: m=({},{}), i={}".format(S, m1, m2, i))
            return i
        i += 1
    return 1


def MissingInteger3(A):      # Failed the test at "extreme_single (a single element)" and "negative_only"
    AA=[]

    for x in A:
        if x > 0:
            AA.append(x)
    print(AA)

    bottom=1
    minA=min(AA)
    print("min: %d" % min(AA))

    if minA > bottom:
        return bottom

    AS = sorted(AA)

    bottom += 1
    for x in AS:
        if x == bottom:
            bottom += 1
    return bottom

def MissingInteger4(A):
    AA=[]

    for x in A:
        if x > 0:
            AA.append(x)
    print("%s -> %s" % (A,AA))
    if len(AA)==0:
        return 1

    bottom=1
    minA=min(AA)
    print("min: %d" % min(AA))

    if minA > bottom:
        return bottom

    AS = sorted(AA)

    bottom += 1
    for x in AS:
        if x == bottom:
            bottom += 1
    return bottom

MissingInteger = MissingInteger4

def Verify():
    AA=[A1,A2, A3,A4,A5,A6,A7,A8,A9,A10]
    for a in AA:
        r = MissingInteger(a)
        print(r)


if __name__ == "__main__":
    Verify()









