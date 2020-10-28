# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bae -> false
#
# 1. one_edit_away
# 2. one_away_shaffle1 and one_away_shaffle2 are not exactly what the question asks for, it has the shuffled cases counted in
#

from collections import Counter


def one_edit_away(A, B):
    len_diff = len(A)-len(B)
    if abs(len_diff)>1:
        return False
    if len_diff == 1 :
        return check_remove(A, B)
    elif len_diff == -1:
        return check_insert(A, B)
    else:  # 0
        return check_replace(A, B)

def check_replace(A, B):
    count = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            count += 1
    if count > 1:
        return False
    else:
        return True

def check_insert(A, B):
    for i in range(len(A)):
        if A[i] != B[i]:
            if A[i:] == B[i+1:]:
                return True
            else:
                return False
    return False

def check_remove(A, B):
    for i in range(len(A)):
        if A[i] != B[i]:
            if A[i+1:] == B[i:]:
                return True
            else:
                return False
    return False



# 
# Time Complexitiy: O(N*N)
# Space Complexity: O(N) ?
def one_away_shaffle1(A, B):
    if abs(len(A)-len(B))>1:
        return False
    
    diff = 0
    a = [x for x in A]
    b = [x for x in B]

    for x in a:
        if x not in b:
            diff += 1
            if diff > 1:
                return False
        else:
            a.remove(x)
            b.remove(x)
    if abs(len(a)-len(b)) > 1:
        return False
    if abs(len(a)-len(b)) == 1 and a[0] != b[0]:
        return False
    return True


# Time Complexitiy: O(N*N)
# Space Complexity: O(N) ?
def one_away_shaffle2(A, B):
    if abs(len(A)-len(B))>1:
        return False
    ca = Counter(A)
    cb = Counter(B)
    dd = {}   # diff
    for x in ca:
        if x not in cb:
            dd[x] = ca[x]
        else:
            dd[x] = ca[x] - cb[x]
    for x in cb:
        if x not in ca:
            dd[x] = - cb[x]
    dd_r = {}
    for v, c in dd.items():
        if c == 0:
            continue
        elif abs(c) > 1:
            return False
        else:
            dd_r[v] = c
    print(dd, dd_r)
    if len(dd_r) < 2:
        return True
    if len(dd_r) > 2:
        return False
    # len(dd) == 2
    sum = 0
    for _, c in dd_r.items():
        sum += c
    if sum > 0:
        return False
    return True


def test(A, B):
    #print(A, B, one_edit_away(A,B))
    #print(A, B, one_away_shaffle2(A,B))
    print(A, B, one_edit_away(A, B))

# test one_edit_away
test('abcd', 'abcd')
test('abcd','abecd')
test('abcd','bcd')
test('xbcd','abcd')
test('abcd','abxd')
test('abcd','acbd')
test('abcd','abcdef')
test('abefcd','abcd')
test('abcd','ac')
test('abcd', 'bca')


# test one_away_shaffle
# test('abcd', 'bca')
# test('fbac','acbd')
# test('aebcd','bdca')
# test('aebcd','bdc')
# test('abcd','aoped')
# test('','')

