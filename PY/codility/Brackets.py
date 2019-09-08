'''
Brackets
Determine whether a given string of parentheses (multiple types) is properly nested.


A string S consisting of N characters is considered to be properly nested 
if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
'''



from utils import Debug


# time complexity: 
def S(A):
    N = len(A)
    if N < 1:
        return 1
    if N == 1:
        return 0

    token = ('{','}','(',')','[',']')
    token_open = ('{','(','[')
    token_close = ('}',')',']')
    def GetPair(a):
        if a == '{':  return '}'
        if a == '}':  return '{'
        if a == '[':  return ']'
        if a == ']':  return '['
        if a == '(':  return ')'
        if a == ')':  return '('
        
    def IsPair(x,y):
        return x == GetPair(y)

    if A[0] not in token:
        return 0

    stack = []
    for i in range(N):
        if A[i] not in token:
            continue
        if A[i] in token_open:
            stack.append(A[i])
        else:    # in token_close
            if len(stack) == 0:
                return 0
            x = stack.pop()
            if not IsPair(x, A[i]):
                return 0
    if len(stack) > 0:
        return 0
    return 1
    



def solution(A):
    return S(A)

if __name__ == "__main__":

    sample = [ 
        "{[()()]}",        # 1
        "([)()]",          # 0
        "{[1,2,3]}",       # 1
        "[1",              # 0
        "",                # 1 
        "[)]",             # 0
        "{}()()[]",        # 1
        ".{[()]}",         # 0
    ]

    for A in sample:
        print('-'*60)
        r = solution(A)
        print("{} -> {}".format(A, r))

