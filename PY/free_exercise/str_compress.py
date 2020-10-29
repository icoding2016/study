# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).


# Time Complexity:  O(N^2)
#    N+(N-1)+...+1=N(N+1)/2
# Space Complexity:  O(N)
#    The compressed may add a bit each time in N loop
def compress(A):
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


def test(A):
    print(A, ' -> ', compress(A))


test('aabcccccaaa')
test('aaaaaaa')
test('abbccceeeef')
test('abcdeeefghig')
test('a')
test('ab')
test('aa')
test('aaa')