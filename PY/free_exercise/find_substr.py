# Given s1 and s2, find if s2 is a substring.
# if so reverse s2 and change it in place in str s1
#
#
# >>> For Python, str is immutable, so cannot change in place.
# 

class Solution(object):
    def substr_reverse(self, s1:str, s2:str)->(bool, str):
        if not s1 or not s2 or len(s2) > len(s1):
            return (False, s1)
        return self.substr_reverse1(s1, s2)
        #return self.substr_reverse_lib(s1, s2)

    def substr_reverse_lib(self, s1:str, s2:str)->(bool, str):
        b =  True if s2 in s1 else False
        return b, s1.replace(s2, s2[::-1]) if b else s1

    def substr_reverse1(self, s1:str, s2:str)->(bool, str):
        L1 = len(s1)
        L2 = len(s2)
        i = 0
        found = False
        newstr = ""
        while i < L1:
            if i <= L1-L2 and s1[i:i+L2] == s2:
                found = True
                #for j in range(L2):
                #    s1[i+j] = s2[-j]
                newstr += s2[::-1]
                i += L2
                continue
            newstr += s1[i]
            i += 1
        #return found, s1
        return found, newstr



def test_fixture(s):
    testdata = [  # (input, expect),
        (("the sampe string of s1", "ring"),  (True, "the sampe stgnir of s1")),
        (("let's sing tik tok, tiktok, go, go ", "tok" ), (True, "let's sing tik kot, tikkot, go, go " )),
        (("s2s1", "s2"), (True, "2ss1")),
        (("ab", "ab"), (True, "ba")),
        (("abc", "abcd"), (False, "abc")),
        (("abc", "de"), (False, "abc")),
        (("abc", ""), (False, "abc")),
        (("", "de"), (False, "")),
   ]

    for i in range(len(testdata)):
        ret = s.substr_reverse(*testdata[i][0])
        exp = testdata[i][1]
        #print("{} -> \t{} \t expect {}".format("testdata[i][0]", ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))


import timeit
def test():
    s = Solution()
    test_fixture(s)

test()

