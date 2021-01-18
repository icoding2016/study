# 
# LongestPassword 
# Given a string containing words, find the longest word that satisfies specific conditions.
# You would like to set a password for a bank account. However, there are three restrictions on the format of the password:
# - it has to contain only alphanumerical characters (a−z, A−Z, 0−9);
# - there should be an even number of letters;
# - there should be an odd number of digits.
#  
# You are given a string S consisting of N characters. 
# String S can be divided into words by splitting it at, and removing, the spaces. 
# The goal is to choose the longest word that is a valid password. 
# You can assume that if there are K spaces in string S then there are exactly K + 1 words.
#
# For example, given "test 5 a0A pass007 ?xy1", 
# there are five words and three of them are valid passwords: "5", "a0A" and "pass007". 
# Thus the longest password is "pass007" and its length is 7. 
# Note that neither "test" nor "?xy1" is a valid password, 
# because "?" is not an alphanumerical character and "test" contains an even number of digits (zero).
#
# Write a function:
# def solution(S)
# that, given a non-empty string S consisting of N characters, 
# returns the length of the longest word from the string that is a valid password. 
# If there is no such word, your function should return −1.
#
# For example, given S = "test 5 a0A pass007 ?xy1", your function should return 7, as explained above.
#
# Assume that:
#
# N is an integer within the range [1..200];
# string S consists only of printable ASCII characters and spaces.
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
#


def solutions(S):
    words = S.split(" ")
    wl = {}    # {words:len}
    longest = -1
    for ws in words:
        b, l = checkPass(ws)
        if not b:
            continue
        else:
            longest = max(longest, l)
    return longest

def checkPass(ws:str)->(bool,int):
    lc = 0
    dc = 0
    for x in ws:
        if 'a'<=x<='z' or 'A'<=x<='Z':
            lc += 1
        elif '0'<=x<='9':
            dc += 1
        else:
            return False, 0
    if lc%2 != 0 or dc%2 != 1:
        return False, lc+dc
    return True, lc+dc




def test_fixture():
    testdata = [  # (input, expect),
        (("test 5 a0A pass007 ?xy1",), 7),
        (("tst 50 b1a0A pass_007 ?xy1",), -1),
        (("1"), 1),
        (("a"), -1),
   ]

    for i in range(len(testdata)):
        ret = solutions(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t expect {}".format("testdata[i][0]", ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))


import timeit
def test():
    #s = Solution()
    test_fixture()

test()


