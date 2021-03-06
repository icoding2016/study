# Given a string s and a string t, check if s is subsequence of t.
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters. 
# (ie, "ace" is a subsequence of "abcde" while "aec" is not).
# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, 
# and you want to check one by one to see if T has its subsequence. 
# In this scenario, how would you change your code?
#
# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true
# 
# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false
# 
# Constraints:
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# Both strings consists only of lowercase characters.


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # return self.is_subsequence1(s, t)
        # return self.is_subsequence2(s, t)
        return self.is_subsequence3(s, t)

    # T(len(t))
    # S(1) 
    def is_subsequence1(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(s) > len(t):
            return False
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(s)

    # T(len(t))
    # S(1)
    def is_subsequence2(self, s:str, t: str) -> bool:
        if not s:
            return True
        if len(s) > len(t):
            return False
        i = 0
        for c in t:
            if i < len(s) and c == s[i]:
                i += 1
        return i == len(s)

    # 
    def is_subsequence3(self, s:str, t: str) -> bool:
        it = iter(t)
        return all(c in it for c in s)


def test_fixture(solution):
    testdata = [  # (input, expect),
        (["",  "absy"], True),
        (["", ""], True),
        (["aba", "cdc"], False),
        (['abcd','abc'], False),
        (['ab', 'aabc'], True),
        (["ab","ab"], True),
        (["axb", "xayyxxbc"], True),
        (['abc', 'ahbgdc'], True),
        (['abc', 'ahhgdc'], False),
        (['abc', 'xahhbgdcg'], True),
        (["ab", "ba"], False),
    ]

    for i in range(len(testdata)):
        ret = solution.isSubsequence(*testdata[i][0])
        exp = testdata[i][1]
        print("{:<30} -> {:<10} {} expect {}".format(str(testdata[i][0]), str(ret), 'pass' if ret==exp else 'fail', exp))


def test():
    s = Solution()
    test_fixture(s)


test()    

