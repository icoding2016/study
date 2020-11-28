# String Compression: 
# exec1:
# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).
#
# exec2:
# Compress string "aabcaaaaade" to "aabc5xade". 
# Only compress if it shortens the string. 5xa means char a is repeated 5 times




# That's not a proper or good implementation, redo it at compress11
#  Time Complexity:  O(N^2)
#    N+(N-1)+...+1=N(N+1)/2
# Space Complexity:  O(N)
#    The compressed may add a bit each time in N loop
def compress1(A):
    compressed = ''
    i = 0
    #for i in range(len(A)):    # Note: that is a wrong way since i will go 0,1,2... even if the j loop set i=j
    while i < len(A):
        count = 1
        if i == len(A) - 1:
            compressed += A[i] + '1'
            break
        for j in range(i+1, len(A)):
            if A[j] == A[i]:
                count += 1
                if j == len(A)-1:
                    compressed += A[i] + '{}'.format(count)
                    i = len(A)
                    break
                j += 1
            else:
                compressed += A[i] + '{}'.format(count)
                i = j
                break        

    if len(compressed) < len(A):
        return compressed
    else:
        return A 

# T(N)
# S(N2)
def compress11(A):
    A2 = ''
    cont = 1
    #pre = None
    for i in range(1, len(A)):
        if A[i] == A[i-1]:
            cont += 1
        else:
            A2 += '{}{}'.format(A[i-1],cont)
            cont = 1
        if i == len(A) - 1:
            if cont == 1:
                A2 += A[i]
            else:
                A2 += '{}{}'.format(A[i-1],cont)
    return A2 if len(A2) < len(A) else A


# T(N)   N = len(A)
# S(NS)  NS = len(newstr)
def compress2(A):
    newstr = ''
    cont = 0
    cur = None
    for i in range(len(A)):
        if cur == A[i]:
            cont += 1
        else:
            if cur != None:
                s2 = '{}x{}'.format(cont, cur)
                newstr += s2 if len(s2)<cont else cur*cont
            cont = 1
            cur = A[i]
        if i == len(A)-1:
            s2 = '{}x{}'.format(cont, cur) 
            newstr += s2 if len(s2)<cont else cur*cont
    
    return newstr



def test_func(A, func):
    print(A, func.__name__, ' -> ', func(A))

def _test(f):
    print('-'*10)
    test_func('aabcccccaaa', f)
    test_func('aaaaaaa', f)
    test_func('abbccceeeef', f)
    test_func('abcdeeefghig', f)
    test_func('a', f)
    test_func('ab', f)
    test_func('aa', f)
    test_func('aaa', f)
    test_func('aaaa', f)
    test_func('baaaab', f)




def test():
    #func = test1
    _test(compress11)
    _test(compress2)



test()