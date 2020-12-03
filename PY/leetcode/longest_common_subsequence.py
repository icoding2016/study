# Longest Common Subsequence
# Medium
# Given two strings text1 and text2, return the length of their longest common subsequence.
# A subsequence of a string is a new string generated from the original string with some characters
# (can be none) deleted without changing the relative order of the remaining characters. 
# (eg, "ace" is a subsequence of "abcde" while "aec" is not). 
# A common subsequence of two strings is a subsequence that is common to both strings.
# If there is no common subsequence, return 0.
#
# Example 1:
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
#  
# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#  
# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
# Constraints:
# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# The input strings consist of lowercase English characters only.
# 
# 
# Ideas:
#   Solution 1:
#     Find common chars from 2 strings ->set1,set2,  take each of the char as 1st letter of subsequnce.
#     pick letters one by one from one set to match the other. 
#     TimeComplexity: O(Nc*2^Nd)  Nc=CommonElementNum, Nd=nonCommonElementNum
# 
#   Solution 2: DP
#     This question only ask for the number (the longest)
#     For sublen(i,j): = max(sublen(str1[i+1], str2[j]), sublen(str1[i], str2[j+1]) 
#                           or sublen(str[i+1], str2[j+1])+1 if str1[i]==str2[j] else 0
# 
#  #


# T(C*2^d)   C=common-char#, d=non-common-char# (d=min(d1,d2))..   
#            at each non-common char, there are 2 routings. so 2^d.  
#            each routing go through the rest of the common-chars (worst O(C)), so O(C*2^d)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        sub1 = ''.join([c for c in text1 if c in text2])
        sub2 = ''.join([c for c in text2 if c in text1])
        #l, c = self.commonSubsequence_bf(sub1, sub2);     print(c)
        l = self.commonSubsequence(sub1, sub2)
        return l

    # brutal force with the max common subsequence value.
    def commonSubsequence_bf(self, s1: str, s2: str, comm: str=None) -> (int, str):
        if None == comm:
            comm = ''
        length = 0

        if not len(s1) or not len(s2):
            return 0, comm
        i = 0
        while i < len(s1) and i < len(s2):
            if s1[i] == s2[i]:
                comm += s1[i]
                i += 1
            else:
                break
        length += i
        if i < min(len(s1), len(s2)):
            len1, c1 = self.commonSubsequence_bf(s1[length+1:], s2[length:], comm[:])
            len2, c2 = self.commonSubsequence_bf(s1[length:], s2[length+1:], comm[:])
            length += max(len1, len2)
            comm = c1 if len1 > len2 else c2
        return length, comm
                

    # count only, recursive
    def commonSubsequenceLen(self, s1: str, s2: str) -> int:
        if not s1 or not s2:
            return 0
        if len(s1) == 1 and len(s2) == 1:
            return 1 if s1[0]==s2[0] else 0
        
        i = 0
        while i < len(s1) and i < len(s2) and s1[i]==s2[i]:
            if s1[i] == s2[i]:
                i += 1
            else:
                break
        length = i
        if i < len(s1) and i < len(s2):
            length += max(self.commonSubsequenceLen(s1[length:], s2[length+1:]),  \
                          self.commonSubsequenceLen(s1[length+1:], s2[length:]))
        return length


    # dp
    def commonSubsequence(self, s1: str, s2: str) -> int:
        if not s1 or not s2:
            return 0
        dp = [[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]
        dp[1][1] = 1 if s1[0] == s2[0] else 0
        for j in range(1, len(s2)+1):
            for i in range(1, len(s1)+1):
                if s1[i-1] == s2[j-1]:
                    dp[j][i] = dp[j-1][i-1] + 1
                else:
                    dp[j][i] = max(dp[j][i-1], dp[j-1][i])
        # for j in range(len(s2)+1):
        #     print(dp[j])
        return dp[-1][-1]




def test_fixture(solution):
    testdata = [  # (input, expect),
        ('cbbd', 'cbde',    3), 
        ("abcba", "abcbcba", 5),
        ('a', 'a',          1),
        ('ac', 'ca',        1),
        ('abcde', 'ace',    3),
        ('abc', 'def',      0),
        ('xaxxbxcxx', 'yyaybbyyc', 3),  
        ('abxxcx', 'xaxbcy',3),  
    ]

    for i in range(len(testdata)):
        ret = solution.longestCommonSubsequence(testdata[i][0], testdata[i][1])
        print("{} -> {} \t\t{} expect {}".format((testdata[i][0], testdata[i][1]), ret, 'pass' if ret==testdata[i][2] else 'fail', testdata[i][2]))


def test():
    s = Solution()
    test_fixture(s)


test()    
