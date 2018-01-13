
'''
Task description
A binary gap within a positive integer N is any maximal sequence of consecutive zeros
  that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
  The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
  The number 20 has binary representation 10100 and contains one binary gap of length 1.
  The number 15 has binary representation 1111 and has no binary gaps.

Write a function:

def solution(N)
that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5,
  because N has binary representation 10000010001 and so its longest binary gap is of length 5.

Assume that:

N is an integer within the range [1..2,147,483,647].
Complexity:

expected worst-case time complexity is O(log(N));
expected worst-case space complexity is O(1).
'''


from __future__ import print_function

'''
Assessment: Correctness 46%
# Wrong, the bnum is in reverse order so the result is wrong
'''
def solution0(N):
    # write your code in Python 2.7 bnum=[]
    num=N
    bnum=[]
    # turn N into binary string
    while True:
        r = int(num/2) #
        m = num%2  # mod
        bnum.append(m)
        if r <= 1:
            bnum.append(1)
            break
        else:
            num=r # print("bin: %s" % bnum)

    start = 0
    l = 0
    maxl = 0
    for i in range(len(bnum)):
        # print("====bunm[%d]=%s" % (i,bnum[i]), end='')
        # print("start: %d" % start)
        if bnum[i] == 0:
            l = l + 1
            # print("l ++ -> %d" % l)
            if i == len(bnum)-1:
                pass
                #if l > maxl:
                #    max = l
        else:
            # print("start set to %d" % start)
            if maxl < l:
                maxl = l
                l = 0
                # print("maxl= %d" % maxl)

    # print("max length: %s" % maxl)

    return bnum, maxl

'''
Assessment: Correctness 80%
  Corrected the bmun mistake by reversing it.
  But still failed at sample number n=561892=10001001001011100100_2 and n=9=1001_2, got 4 expect 3.
  Mistake 1) under condition (if bnum[i] == 0 & last bit) l shouldn't be +1.
          2) l = 0 is put under condition of 'if maxl < l' by mistake.
'''
def solution2(N):
    # write your code in Python 2.7 bnum=[]
    num=N
    bnum=[]
    # turn N into binary string
    while True:
        r = int(num/2) #
        m = num%2  # mod
        bnum.append(m)
        if r <= 1:
            bnum.append(1)
            break
        else:
            num=r # print("bin: %s" % bnum)
    bnum.reverse()

    start = 0
    l = 0
    maxl = 0
    for i in range(len(bnum)):
        # print("====bunm[%d]=%s" % (i,bnum[i]), end='')
        # print("start: %d" % start)
        if bnum[i] == 0:
            l = l + 1
            # print("l ++ -> %d" % l)
            if i == len(bnum)-1:
                pass
                #if l > maxl:
                #    max = l
        else:
            # print("start set to %d" % start)
            if maxl < l:
                maxl = l
                l = 0
                # print("maxl= %d" % maxl)

    # print("max length: %s" % maxl)

    return bnum, maxl

'''
Corrected mistakes.
But still can have num->bin_str convertion code replaced by python internal function bin()
'''
def solution3(N):
    # write your code in Python 2.7 bnum=[]
    num=N
    bnum=[]
    # turn N into binary string
    while True:
        r = int(num/2) #
        m = num%2  # mod
        bnum.append(m)
        if r <= 1:
            bnum.append(1)
            break
        else:
            num=r # print("bin: %s" % bnum)
    bnum.reverse()

    start = 0
    l = 0
    maxl = 0
    for i in range(len(bnum)):
        # print("====bunm[%d]=%s" % (i,bnum[i]), end='')
        # print("start: %d" % start)
        if (bnum[i] == 0):
            if (i == len(bnum)-1):
                pass
            l = l + 1
            print("l ++ -> %d" % l)
        else:
            # print("start set to %d" % start)
            if maxl < l:
                maxl = l
            l = 0
                # print("maxl= %d" % maxl)

    # print("max length: %s" % maxl)

    return bnum, maxl

def solution(N):
    # write your code in Python 2.7 bnum=[]
    num=N
    #bnum=[]
    # turn N into binary string
    bnum = bin(N)[2:]
    print(len(bnum))

    start = 0
    l = 0
    maxl = 0
    for i in range(len(bnum)):
        # print("====bunm[%d]=%s" % (i,bnum[i]), end='')
        # print("start: %d" % start)
        print(bnum[i])
        if (bnum[i] == 0):
            if (i == len(bnum)-1):
                pass
            l = l + 1
            print("l ++ -> %d" % l)
        else:
            # print("start set to %d" % start)
            if maxl < l:
                maxl = l
            l = 0
                # print("maxl= %d" % maxl)

    # print("max length: %s" % maxl)

    return bnum, maxl

def test():
    num, max = solution(561892)
    print (num, max)

if __name__ == "__main__":
    test()