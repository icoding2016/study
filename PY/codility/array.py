'''
CyclicRotation

A zero-indexed array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is also moved to the first place.

For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]. The goal is to rotate array A K times; that is, each element of A will be shifted to the right by K indexes.

Write a function:

struct Results solution(int A[], int N, int K);
that, given a zero-indexed array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given array A = [3, 8, 9, 7, 6] and K = 3, the function should return [9, 7, 6, 3, 8].

Assume that:

N and K are integers within the range [0..100];

In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
'''

A = [3, 8, 9, 7, 6]


def CyclicRotation(A, K):
    # write your code in Python 2.7
    l = len(A)
    B = [0] * l

    for i in xrange(l):
        j = (i + K) % l
        # print("{} -> {}".format(i,j))
        B[j] = A[i]

    return B
CyclicRotation(A, 3)


'''
A non-empty zero-indexed array A consisting of N integers is given.
The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)
that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Assume that:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.

Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(1), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.
'''

def OddOccurrencesInArray(A):       # Passed 100 score
    # write your code in Python 2.7
    S = set(A)
    D = dict()
    for x in S:
        D.setdefault(x, 0)  # D.add({x:0})
    for i in A:
        D[i] = D[i] + 1
        print("{}:{}".format(i, D[i]))
        if D[i] == 2:
            # S.remove(i)
            D[i] = 0
            print("reset {}".format(i))
            if unique==i:
                unique = None
                print("reset unique %s" % i)
        else:
            unique = i
            print("unique={}".format(unique))

    for i in D:
        if D[i] == 1:
            print("======The unique: {}".format(i))

    return unique

T = [9,3,9,3,7,9]  #7
T1 = [3,0,2,3,5,1,0,2,3,5,5,0,1,0,5] #3
OddOccurrencesInArray(T)
OddOccurrencesInArray(T1)
