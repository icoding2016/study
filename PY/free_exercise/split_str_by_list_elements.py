# Write a python function that inputs a string and a list, 
# then uses the list values to split the string into another list
# 
# e.g  
#   str: 'This is a test string', 
#   list:['s','t']       -> ['Thi',' i', ' a ', 'e', ' ', 'ring']
#   list:[' ']           -> ['This','is', 'a', 'test', 'string'] 
# 
# 
# #

class Solution():
    def split(self, s:str, l:list) -> list:
        if not s:
            return [s]
        if not l:
            return [s]

        result = []
        openflag = False
        cur = ''
        for i,x in enumerate(s):
            if x not in l:
                if openflag:
                    cur += x
                    if i == len(s)-1:
                        result.append(cur)
                        break
                else:
                    cur = '{}'.format(x)
                    if i == len(s)-1:
                        result.append(cur)
                        break
                    openflag = True
            else:
                if openflag:
                    if cur:
                        result.append(cur)
                    openflag = False
                else:
                    continue
        return result
             


def test_fixture(s):
    testdata = [  # (input, expect),
        (('This is a test string', ['s','t']),  ['Thi',' i', ' a ', 'e', ' ', 'ring']),
        (('This is a test string', [' ']),  ['This','is', 'a', 'test', 'string']),
        (('This is a test string', []),  ['This is a test string']),
        (('bbaaaabaaab', ['b']),  ['aaaa','aaa']),
        (('aaaabaaabaa', ['b']),  ['aaaa','aaa','aa']),
        (('caaacbaacabaa', ['b','c']),  ['aaa','aa','a','aa']),
        (('', ['a','b']),  ['']),
    ]

    def compResult(r, e):
        if len(r) != len(e):
            return False
        rr = [sorted(x) for x in r]
        ee = [sorted(x) for x in e]
        while rr:
            if rr[0] in ee:
                ee.remove(rr[0])
                rr.remove(rr[0])
            else:
                return False
        return not bool(ee)

    for i in range(len(testdata)):
        ret = s.split(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t expect {}".format(testdata[i][0], ret, exp), end='\t')
        print("{}".format('pass' if compResult(ret, exp) else 'fail'))


import timeit
def test():
    s = Solution()
    test_fixture(s)

test()



