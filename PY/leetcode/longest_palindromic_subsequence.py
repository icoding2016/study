#  Longest Palindromic Subsequence
# Medium
# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
# Input:
# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
#
# Example 2:
# Input:
# "cbbd"
# Output:
# 2
# One possible longest palindromic subsequence is "bb".
#
# Constraints:
# 1 <= s.length <= 1000
# s consists only of lowercase English letters.
# 
# Note:
#   'subsequence' means either a 'substring' or a 'substring with some letters missing'
#   so skipping a few characters is allowed, but the order cannot be messed up 
#   e.g. Example 1 'bbbb' is a subsequence of 'bbbab'
#   
# Ideas:
#   start from the 2 ends. pick the max from the 2 optins:
#   1) fix left end and search match from right most to left;  
#   2) fix right end and search match from the left most to right
# 
#   

from collections import defaultdict


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        #return self.countkPalindromeSub(s)
        return self.countkPalindromeSub_memo(s)

    # T(C*2^S)   C=parlindrone char number, S=skipped char num,   
    #            best O(N),  worst O(2^N)
    def countkPalindromeSub(self, s:str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        l = 0
        r = len(s) - 1
        count = 0
        while l < r:
            if s[l] == s[r]:
                count += 2
                l += 1
                r -= 1
            else:
                c1 = self.countkPalindromeSub(s[l:r])
                c2 = self.countkPalindromeSub(s[l+1:r+1])
                count += max(c1, c2)
                break
        if l == r:
            count += 1
        return count

    # T(C*2^S)
    def countkPalindromeSub_memo(self, s:str, memo:dict=None) -> int:
        if len(s) < 2:
            return len(s)
        if None == memo:
            memo = dict()
        if s in memo:
            return memo[s]
        l = 0
        r = len(s) - 1
        count = 0
        while l < r:
            if s[l] == s[r]:
                count += 2
                l += 1
                r -= 1
            else:
                c1 = self.countkPalindromeSub_memo(s[l:r], memo)
                c2 = self.countkPalindromeSub_memo(s[l+1:r+1], memo)
                count += max(c1, c2)
                break
        if l == r:
            count += 1
        memo[s] = count
        return count




def test_fixture(solution):
    testdata = [  # (input, expect),
        ('cbbd', 2), 
        ('a',   1),
        ('ac',  1), #1
        ('bab', 3), #3
        ('bbab', 3), #3
        ('bbbab', 4),   #4  bbbb
        ('babad', 3),   #3
        ("babbabd",6),  #6
        ('aaaaaaa', 7),
    ]

    for i in range(len(testdata)):
        ret = solution.longestPalindromeSubseq(testdata[i][0])
        print("{} -> {} \t\t{} expect {}".format(testdata[i][0], ret, 'pass' if ret==testdata[i][1] else 'fail', testdata[i][1]))


def test():
    s = Solution()
    test_fixture(s)


test()    

