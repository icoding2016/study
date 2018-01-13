'''
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Assume that:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
Complexity:

expected worst-case time complexity is O(1);
expected worst-case space complexity is O(1).

'''

'''
COMMNET:
Python3: /  float division      5/2=2.5
         // integer division    5//2=2
'''

def CountDiv1(A,B,K):        # Correctness 100%, performance 0%, total 50%
                             # Time complexity: O(B-A)
    count = 0
    for x in range(A,B+1):
        if (x % K)==0:
            count += 1
    return count

def CountDiv(A, B, K):  # Correctness 100%, performance 100%
    high = B//K
    low = (A-1)//K

    return high-low

#############################
def Verify():
    AA = [
        [1,9,3],
        [2,10,4],
        [4,20,6]
    ]
    for a in AA:
        r = CountDiv(a[0],a[1],a[2])
        print("%s, count=%d" % (a, r))

Verify()
