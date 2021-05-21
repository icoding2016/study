# Word Break
# Medium
# https://leetcode.com/problems/word-break/

# Given a string s and a dictionary of strings wordDict, return true if s can be
# segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

# Constraints:
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
#
# 
# 
# 
# 
#  


from typing import List
from utils.testtools import test_fixture


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict
        if len(s) == 1:
            return True if s in wordDict else False
        s_set = set(s)
        d_set = set()
        for word in wordDict:
            d_set = d_set.union(word)
        # some shortcut to speed up for special cases
        if any([c not in d_set for c in s_set]):
            return False
        if all([c in wordDict for c in s_set]):
            return True
        # return self.wordBreak_r2(s[0], s[1:])
        return self.wordBreak_dp(s)
        
    # Brutal force (recursive)
    # T(2^N)    for each position, choose from 2 options (break/not-break),
    # with efficency issue for long string. 
    def wordBreak_r(self, cur:str, remain:str) -> bool:
        if not remain:
            if cur in self.wordDict:
                return True
            else:
                return False
        if cur in self.wordDict:
            if self.wordBreak_r(remain[0], remain[1:]):
                return True
        if self.wordBreak_r(cur+remain[0], remain[1:]):
            return True
        return False

    def wordBreak_r2(self, cur:str, remain:str) -> bool:
        if not remain:
            if cur in self.wordDict:
                return True
            else:
                return False
        if cur in self.wordDict:
            # try skip all cur in s
            remain2 = remain.replace(cur, '')
            if self.wordBreak_r2(remain2[0], remain2[1:]):
                return True
            if self.wordBreak_r2(remain[0], remain[1:]):
                return True
        if self.wordBreak_r2(cur+remain[0], remain[1:]):
            return True
        return False

    # T(N*N)    For each i in (0,N) where there are word matches, go through (i+1,N) to check word match in dict. 
    def wordBreak_dp(self, s) -> bool:
        flags = [False for i in range(len(s))]
        extra_word_dict = []
        start = 0
        while start < len(s):
            for i in range(start, len(s)):
                if s[start:i+1] in self.wordDict or s[start:i+1] in extra_word_dict:
                    flags[i] = True
                    if s[:i+1] not in extra_word_dict:
                        extra_word_dict.append(s[:i+1])
            if flags[-1]:
                return True
            start += 1
            while start<len(s) and not flags[start-1]:
                start += 1
        return flags[-1]    


def test():
    data = [
        (("leetcode", ["leet","code"]), True),
        (("applepenapple", ["apple","pen"]), True),
        (("catsandog",["cats","dog","sand","and","cat"]), False),
        (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
          ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]), False),
        (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
          ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]), False),
        (("ababababababababababababababababababababababab", ["ab","cd","aba"]), True),
    ]
    s = Solution()
    test_fixture(s.wordBreak, data)


test()







