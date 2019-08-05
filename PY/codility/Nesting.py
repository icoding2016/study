'''
Nesting
Determine whether a given string of parentheses (single type) is properly nested.


A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000,000];
string S consists only of the characters "(" and/or ")".

'''


'''


'''



from utils import Debug


# time complexity: 
def S(A):
    N = len(A)
    if N == 0:
        return 1
    
    Stack = []
    for i in range(N):
        if A[i] not in ['(',')']:
            continue
        if A[i] == '(':
            Stack.append(A[i])
            continue
        else:   # A[i] == ')' 
            if not Stack:
                return 0
            else:
                Stack.pop()
                continue
    return 1 if len(Stack)==0 else 0
    



def solution(A):
    return S(A)

if __name__ == "__main__":

    sample = [ 
        '(()(())())',        # 1
        '())',               # 0
        '',                  # 1
        '(',                 # 0
        '.(())',             # 1
        'x)()',              # 0
        'x(x((y)x))x',       # 1
    ]

    for A in sample:
        print('-'*60)
        r = solution(A)
        print("{} -> {}".format(A, r))

