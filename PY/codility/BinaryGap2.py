'''
Task
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''


'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Notes:
  Be careful for the logic.
  10010001
     ^
     The 1 ending current pairing could also be the 1 starting a new pairing
     
  S1() is the example of the mistake
'''



DEBUG = 1

def Debug(s):
    global DEBUG
    if (DEBUG):
        print(s)


def S(N):
    b = str(bin(N))[2:]
    max_len = 0
    cur_len = 0
    pairing = False
    found_pair = False
    l = len(b)

    Debug("{} - {}".format(N,b))

    if len(b) < 3:
        return 0

    for i in range(len(b)):
        if b[i] == '1' and not pairing:    #  1x, start pairing
            cur_len = 0
            pairing = True
            Debug("{}: start pairing".format(b[i]))
        elif b[i] == '1' and pairing:     #  1x or 11x
            if cur_len == 0:            #  11x
                Debug("{}: continue 1 to start pairing".format(b[i]))
                continue
            else:   # end of current pairing
                if cur_len > max_len:    max_len = cur_len
                Debug("{}: end pairing. cur_len={}".format(b[i], cur_len))
                #pairing = False
                cur_len = 0
                found_pair = True
        elif b[i] == '0' and not pairing:   #  00x
            Debug("{}: 0 without pairing".format(b[i]))
            continue
        elif b[i] == '0' and pairing:       #  10
            Debug("{}: 0 within pairing".format(b[i]))
            cur_len += 1
        else:
            print("WRONG")
    if not found_pair:
        return 0
    return max_len


#### Failed case  (80% correctness) #####
def S1(N):
    b = str(bin(N))[2:]
    max_len = 0
    cur_len = 0
    pairing = False
    found_pair = False
    l = len(b)

    Debug("{} - {}".format(N,b))

    if len(b) < 3:
        return 0

    for i in range(len(b)):
        if b[i] == '1' and not pairing:    #  1x, start pairing
            cur_len = 0
            pairing = True
            Debug("{}: start pairing".format(b[i]))
        elif b[i] == '1' and pairing:     #  1x or 11x
            if cur_len == 0:            #  11x
                Debug("{}: continue 1 to start pairing".format(b[i]))
                continue
            else:   # end of current pairing                      
                if cur_len > max_len:    max_len = cur_len
                Debug("{}: end pairing. cur_len={}".format(b[i], cur_len))
                pairing = False                         # <-- logic defect here. The 1 ending current pairing could also be the 1 starting a new pairing
                cur_len = 0
                found_pair = True
        elif b[i] == '0' and not pairing:   #  00x
            Debug("{}: 0 without pairing".format(b[i]))
            continue
        elif b[i] == '0' and pairing:       #  10
            Debug("{}: 0 within pairing".format(b[i]))
            cur_len += 1
        else:
            print("WRONG")
    if not found_pair:
        return 0
    return max_len

def solution(N):
    # write your code in Python 3.6
    return S(N)

if __name__ == "__main__":

    sample = [
        1,
        6,    #2
        328,  #2
        9,
        529,
        20,
        15,
        32,
        1162,   #3
        66561,  #9
    ]

    for x in sample:
        r = solution(x)
        print("{} -> {}".format(x, r))

