# question  given a string, output all the permutation of the possible jumbled string
#  e.g.   'abc' -> 'acb', 'bac', 'bca', 'cba
#          


def jumble(S, output=None):
    if output is None:
        output = ''
    L = len(S)
    if L <= 1:
        o = output + S
        print(o)
        return
    for i in range(L):
        o = output+S[i]
        s1 = S[:i]+S[i+1:]
        jumble(s1, o)
    return


def test():
    jumble('abc')    


test()

