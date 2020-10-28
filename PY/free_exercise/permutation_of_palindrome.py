# Palindrome Permutation: 
# Question 1) 
# Given a string, write a function to check if it is a permutation of
# a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A
# permutation is a rearrangement of letters. The palindrome does not need to be limited to just
# dictionary words.
#   conditions:   capital doesn't matter 
# EXAMPLE
# Input: 'Tact Coa '
# Output: True (permutations: "tac o cat'; "atc o cta·; etc.).
# 
# Question 2)
# Extened question: Give all the possible permutation of palindrome for the string.
# 

from collections import Counter

def is_palindrome(A):
    B = A.lower()
    C = Counter(B)
    #for x, c in C.items():          print(x, c)
    odd = []
    for x, c in C.items():
        if c%2 != 0:
            odd.append(x)
    if len(odd) <= 1:
        return True, odd
    return False, odd



def permutate_palindrome(A):
    B = A.lower()            # if do the solution with case sensitive
    C = Counter(B)
    odd = []
    for v, c in C.items():
        if c%2 != 0:
            odd.append(v)
    if len(odd) > 1:
        print("Error: more than 1 odd elements {}".format(odd))
        return
    
    # create the str with the char in pair
    s = ''.join([v*int(c/2) for v,c in C.items() if c%2==0])
    if odd and C[odd[0]]>1:       # if the middle character has > 1 number
        s += ''.join(odd[0]*int((C[odd[0]]-1)/2))
    #print(s)
    result = jumble_str(s)
    #print(result)

    for x in result:
        if x:
            if odd:
                s = x + odd[0] + x[::-1]
            else: 
                s = x + x[::-1]
            print('"' + s + '"')

def jumble_str(s, output=None, result=None):
    if output is None:
        output = ''
    if result is None:
        result = []
    if len(s) <= 1:
        o = output + s
        # print(o)
        result.append(o)
        return result
    for i in range(len(s)):
        s1 = s[:i] + s[i+1:]
        jumble_str(s1, output+s[i], result)
    return result

def test(A):
    r, odd = is_palindrome(A)
    #print(r, odd)

    print("permutate_palindrome: ", A)
    permutate_palindrome(A)


test('papa')
test('hahah')
#test('Taco Cat AA')

