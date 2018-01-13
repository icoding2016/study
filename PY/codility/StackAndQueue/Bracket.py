'''
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)
that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Assume that:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N) (not counting the storage required for input arguments).
Copyright 2009–2017 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

'''

tc1='(({[]()}[[]]))'
tc2='(3[adf]({d}3[])fg(dd)()[d{},()])'

def BracketsCheck(S):
    N = len(S)
    if N == 0:
        return 1

    validSet = ('(', ')', '[', ']', '{', '}')
    a = 0
    b = 0
    c = 0
    s = []
    outputS = ""

    for i in range(N):
        x = S[i]
        if x in validSet:
            outputS += x
            if x in ['(', '[', '{']:
                s.append(x)
            else:
                if len(s) == 0:
                    return 0
                p = s.pop()
                if (x == ')' and p != '(') or \
                        (x == ']' and p != '[') or \
                        (x == '}' and p != '{'):
                    return 0
    if len(s) > 0:
        return 0
    print(outputS)
    return 1

# test
def Verify():
    #r=BracketsCheck(tc1);
    print("%s -> Result: %d" % (tc1,BracketsCheck(tc1)))
    print("%s -> Result: %d" % (tc2,BracketsCheck(tc2)))



Verify()