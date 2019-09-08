'''
GenomicRangeQuery
Find the minimal nucleotide from a range of sequence DNA.


A DNA sequence can be represented as a string consisting of the letters A, C, G and T, 
which correspond to the types of successive nucleotides in the sequence. 
Each nucleotide has an impact factor, which is an integer. 
Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. 
You are going to answer several queries of the form: What is the minimal impact factor 
of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. 
There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers. 
The K-th query (0 ≤ K < M) requires you to find the minimal impact factor of nucleotides contained 
in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose 
impact factors are 3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, 
so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular 
nucleotide A whose impact factor is 1, so the answer is 1.

Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting 
of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P, Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
'''


'''
NOTE:
  Performance issue.

  Sol1() failed for performance issue:
        Task Score 62%, Correctness 100%, Performance 0%
  Sol2() skipped 'converting 'CGTA..' to value [2341..], only process the particals from P/Q, 
         but didn't solve the performance issue.
  Sol() got 100% by avoiding processing the whole list.
        1) only check the given partical
        2) only check the existance of the smallest, if found then stop
         
'''


from utils import Debug


def Sol(S, P, Q):
    #D = {'A':1, 'C':2, 'G':3, 'T':4}

    N = len(S)
    M = len(P)

    result = [0]*M
    for i in range(M):
        partical = S[P[i]:Q[i]+1] if Q[i] < N-1 else S[P[i]:]
        if 'A' in partical:
            r = 1
        elif 'C' in partical:
            r = 2
        elif 'G' in partical:
            r = 3
        else:
            r = 4
        result[i] = r
    return result

# time complexity: O(N * M)
def Sol1(S, P, Q):
    D = {'A':1, 'C':2, 'G':3, 'T':4}

    N = len(S)
    M = len(P)

    V = [D[k] for k in S]   # S -> V

    result = [0]*M
    for i in range(M):
        partical = V[P[i]:Q[i]+1] if Q[i] < N-1 else V[P[i]:]
        s = set(partical)
        m = min(s)    # postion: P[i], Q[i] --> list index P[i]-1, Q[i] (inclusive)
        result[i] = m
    return result


# time complexity: O(N * M)
def Sol2(S, P, Q):
    D = {'A':1, 'C':2, 'G':3, 'T':4}

    N = len(S)
    M = len(P)

    Debug(S)

    result = [0]*M
    for i in range(M):
        partical = S[P[i]:Q[i]+1] if Q[i] < N-1 else S[P[i]:]
        Debug('partical {}'.format(partical))
        s = set(partical)
        m = min([D[k] for k in s])
        result[i] = m
    return result



def solution(S, P, Q):
    return Sol(S, P, Q)

if __name__ == "__main__":

    sample = [ 
        ('CAGCCTA', [2,5,0], [4,5,6]),      # [2,4,1]
        ('C', [0], [0]),                    # [2]
        ('CT', [0,0], [0,1]),               # [2,2]
        ('CT', [0,1], [0,1]),               # [2,4]
    ]

    for s,p,q in sample:
        print('-'*60)
        r = solution(s,p,q)
        print("{} -> {}".format((s,p,q), r))

