'''
A non-empty array A consisting of N integers is given.
The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences 
A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, 
returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
'''


# Correctness 60%, Performance 100%
# time complexity:  
def S(A):
    class ELCounter():   #

        def __init__(self, A):
            self.A = A
            self.LEN = len(A)
            self.LC = dict()   # left-counter
            self.RC = dict()
            self.max_l = None
            self.max_r = None
            self.snap = [ (None, None) ] * self.LEN

        def run(self, idx):
            if idx >= self.LEN:
                return
            kl = self.A[idx]
            if kl not in self.LC.keys():
                self.LC[kl] = 1
            else:
                self.LC[kl] += 1

            if not self.max_l:
                self.max_l = (kl, self.LC[kl])
            else:
                k, v = self.max_l
                if self.LC[kl] > v:
                    self.max_l = (kl, self.LC[kl])
                elif self.LC[kl] == v and k != kl:
                    self.max_l = None

            # right
            kr = self.A[self.LEN-idx-1]
            if kr not in self.RC.keys():
                self.RC[kr] = 1
            else:
                self.RC[kr] += 1

            if not self.max_r:
                self.max_r = (kr, self.RC[kr])
            else:
                k, v = self.max_r
                if self.RC[kr] > v:
                    self.max_r = (kr, self.RC[kr])
                elif self.RC[kr] == v and k != kr:
                    self.max_r = None

            self.snap[idx] = (self.max_l, self.snap[idx][1])
            self.snap[self.LEN-idx-1] = (self.snap[self.LEN-idx-1][0], self.max_r)
            #print(self.snap)

    leader = []
    elCounter = ELCounter(A)
    N = len(A)
    for i in range(N):
        elCounter.run(i)
    #print(elCounter.snap)

    total = 0
    for i in range(N-1):
        lmax, _ = elCounter.snap[i]
        _, rmax = elCounter.snap[i+1]
        if lmax and rmax and lmax[0] == rmax[0]:
            leader.append(i)
            total += 1

    #print(leader)
    return total


def solution(A):
    return S(A)

if __name__ == "__main__":

    sample = [ 
        [4,3,4,4,4,2],    # 2
        [3, 3],           # 1
        [1,2,2],          # 0
        [1,2,1,2],        # 0
        [1,1,1,1,1],      # 4
        [1,1,2,1],        # 2
    ]

    for A in sample:
        print('-'*60)
        r = solution(A)
        print("{} -> {}".format(A, r))

