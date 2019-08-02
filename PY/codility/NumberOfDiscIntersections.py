'''
NumberOfDiscIntersections
Compute the number of intersections in a sequence of discs.


We draw N discs on a plane. The discs are numbered from 0 to N − 1. 
An array A of N non-negative integers, specifying the radiuses of the discs, is given. 
The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and 
K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. 
The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..2,147,483,647].

'''


'''
NOTE:

  Consideration:
    - intersect means   |r1+r2| >= center-distance  ==> A[i]+A[j]>=j-i
    - no order, so we just look 'forward' for pairing, not backward
    special conditions
    - radius = 0 is allowed.  So if r=0 and the center point is on the other disc's border, that count, otherwise not.
    - N = 0:   []
    - N = 1:   
    - [0,0]:   
    - exit conditions, eg. overflow

  Key: 
    - performance

  1st try (S_circel):   wrong understanding of question. Thought it to be a 'circle' 
  2nd try (S_disc1):    Task Score 50%,  Correctness 100%, Performance 0%.

'''


# Performance improving:  'bracket stacking model'
#   To count the overlay at every position, use 'open/close bracket'
#   e.g [1, 5, 2, 1, 4, 0]
#    (''('()'(')'(')')
#         (    )')
#    0  1 32 3 2 0            <- pairs (the open disc on the left of current position),   sum(1,3,2,3,2)
# time complexity:  
def S_disc(A):
    
    N = len(A)

    if N < 2:
        return 0

    disc_opr = []            # for open disc position

    # N >= 2
    for i in range(N):
        disc_opr.append((i-A[i], 'O'))
        disc_opr.append((i+A[i], 'C'))
    disc_opr.sort(key=lambda x: (x[0], 1 if x[1]=='O' else 2)) 
    print(disc_opr)

    count_open = 0
    count_pairs = 0
    for p,o in disc_opr:
        if o == 'O':  #open
            count_pairs += count_open
            count_open += 1
            #print("open: {}, count_open: {}, count_pair: {}".format(p, count_open, count_pairs))
        else:    # o=='C'
            count_open -= 1
            #print("disc_close pop: {}, count_open: {}".format(p, count_open))
        
    return count_pairs



# The 'disc' is an 'area' not circle. So intersect means abs(A[i]+A[j]) >= j-1
# time complexity:  O(N**2)
def S_disc1(A):

    N = len(A)

    def check(i,j):  # True if intersect can happen
        return False if (A[i]+A[j]<j-i) else True

    if N < 2:
        return 0

    # N >= 2
    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if check(i,j):
                count += 1
            else:
                continue
            if count > 10000000:
                return -1
    return count


def S_circle(A):
    
    N = len(A)

    def check(i,j):  # True if intersect can happen in general cases (except r=0)
        if (A[i]+A[j]<j-i) or abs(A[i]-A[j])>j-i:
            return False
        else:
            return True

    if N < 2:
        return 0

    # N >= 2
    count = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if A[i] == 0 or A[j] == 0:  # intersect only when it's center on the other's border
                if abs(A[i]-A[j]) == (j-i):
                    count += 1
                continue
            if check(i,j):
                count += 1
            else:
                continue
            if count > 10000000:
                return -1
    return count


def solution(A):
    return S_disc(A)

if __name__ == "__main__":

    sample = [ 
        [1,5,2,1,4,0],    # 11
        [],               # 0
        [1],              # 0
        [0,0],            # 0
        [1,2],            # 1
        [0,1],            # 1
        [0,2],            # 1
        [0,0,1],          # 1
        [2,1,1,0,0],      # 4
        [1,2,3,4,5],      # 10
    ]

    for A in sample:
        print('-'*60)
        r = solution(A)
        print("{} -> {}".format(A, r))

