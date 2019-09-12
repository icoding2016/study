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

'''
Note: 
  Go through the list A once and record all required result.  (avoid loop in loop)
  Analyse record to get anwser afterwards.
  In solution S(), 
  1) process both left and right in current round
  2) use ELCounter.snap to record the left-leader and right-leader found at each position
  3) use structure (class) to record information.
  snap:        0                        1                 ...             N
     Leader-l[value, count]_0,  Leader-l[value, count]_1, ...
     Leader-r[value, count]_0,  Leader-l[value, count]_1, ...
'''



# Correctness 100%, Performance 100%
# time complexity:  
def S(A):
    class ELCounter():   #

        def __init__(self, A):
            self.A = A
            self.LEN = len(A)
            self.LC = dict()   # left-counter
            self.RC = dict()
            self.leader_l = None
            self.leader_r = None
            self.snap = [ (None, None) ] * self.LEN

        def run(self, idx):
            if idx >= self.LEN:
                return
            kl = self.A[idx]
            if kl not in self.LC.keys():
                self.LC[kl] = 1
            else:
                self.LC[kl] += 1

            if self.LC[kl] > int((idx+1)/2):
                self.leader_l = (kl, self.LC[kl])
            elif self.leader_l and self.leader_l[0] != kl and self.leader_l[1] > int((idx+1)/2):
                pass;         # self.leader_l unchange
            else:
                self.leader_l = None

            # right
            kr = self.A[self.LEN-idx-1]
            if kr not in self.RC.keys():
                self.RC[kr] = 1
            else:
                self.RC[kr] += 1

            if self.RC[kr] > int((idx+1)/2):
                self.leader_r = (kr, self.RC[kr])
            elif self.leader_r and self.leader_r[0] != kr and self.leader_r[1] > int((idx+1)/2):
                pass;         # self.leader_r unchange
            else:
                self.leader_r = None

            self.snap[idx] = (self.leader_l, self.snap[idx][1])
            self.snap[self.LEN-idx-1] = (self.snap[self.LEN-idx-1][0], self.leader_r)
            # print(self.snap)

    if len(A) == 1:
        return 0

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


# Correctness 60%, Performance 100%
# time complexity:  
# Mistake:   the code making judgement for 'leader' (definition)
def S1(A):
    class ELCounter():   #

        def __init__(self, A):
            self.A = A
            self.LEN = len(A)
            self.LC = dict()   # left-counter
            self.RC = dict()
            self.leader_l = None
            self.leader_r = None
            self.snap = [ (None, None) ] * self.LEN

        def run(self, idx):
            if idx >= self.LEN:
                return
            kl = self.A[idx]
            if kl not in self.LC.keys():
                self.LC[kl] = 1
            else:
                self.LC[kl] += 1

            if not self.leader_l:
                self.leader_l = (kl, self.LC[kl])
            else:
                k, v = self.leader_l
                if self.LC[kl] > v:
                    self.leader_l = (kl, self.LC[kl])
                elif self.LC[kl] == v and k != kl:
                    self.leader_l = None

            # right
            kr = self.A[self.LEN-idx-1]
            if kr not in self.RC.keys():
                self.RC[kr] = 1
            else:
                self.RC[kr] += 1

            if not self.leader_r:
                self.leader_r = (kr, self.RC[kr])
            else:
                k, v = self.leader_r
                if self.RC[kr] > v:
                    self.leader_r = (kr, self.RC[kr])
                elif self.RC[kr] == v and k != kr:     # <-- mistake
                    self.leader_r = None

            self.snap[idx] = (self.leader_l, self.snap[idx][1])
            self.snap[self.LEN-idx-1] = (self.snap[self.LEN-idx-1][0], self.leader_r)
            print(self.snap)

    if len(A) == 1:
        return 0

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
        [1,1,1,1,1],      # 4
        [0],              # 0
        [1,2,1,1],        # 2
        [1,2,1],          # 0
        [1,2,3,4],        # 0
        [-1,-1,1,-1,-1,2],# 3
        # failed case
        [4, 4, 2, 5, 3, 4, 4, 4], # 3
    ]

    for A in sample:
        print('-'*60)
        r = solution(A)
        print("{} -> {}".format(A, r))

