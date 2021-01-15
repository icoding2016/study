# Longest Uncommon Subsequence II
# Medium
# Given a list of strings, you need to find the longest uncommon subsequence among them. 
# The longest uncommon subsequence is defined as the longest subsequence of one of these strings 
# and this subsequence should not be any subsequence of the other strings.
# A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. 
# Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.
# The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. 
# If the longest uncommon subsequence doesn't exist, return -1.
#
# Example 1:
# Input: "aba", "cdc", "eae"
# Output: 3
# Note:
#
# All the given strings' lengths will not exceed 10.
# The length of the given list will be in the range of [2, 50].
# 
# 
# Ideas:
#   1) BF: find all subsequences for each str, remove the duplicated from each other. 
#           then get the longest of all the subsequences.
#  
#   2) couldn't get this. https://leetcode.com/problems/longest-uncommon-subsequence-ii/discuss/99453/Python-Simple-Explanation
# # 

from typing import List
from collections import defaultdict


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        #return self.findLUSlength_BF(strs)
        return self.findLUSlength1(strs)


    def findLUSlength1(self, strs: List[str]) -> int:
        strs.sort(key=len, reverse=True)
        for i, s1 in enumerate(strs):
            if all(not self.is_subsequence(s1, s2) for j, s2 in enumerate(strs) if j != i):
                return len(s1)
        return -1


    def is_subsequence(self, s1:str, s2:str) ->bool:
        '''check if s1 is a subsequence of s2'''
        if len(s2) < len(s1):
            return False
        i = j = 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i==len(s1)


    # Brutal force ver.2
    #  find all the subsequence of each string, use set() to skip duplicates
    def findLUSlength_BF(self, strs: List[str]) -> int:
        subs = []
        for st in strs:
            subs.append(self.all_subsequence(st))
        print(subs)
        for i in range(len(subs)):
            for s in subs[i].copy():
                for othersb in subs[:i]+subs[i+1:]:
                    if s in othersb:
                        #remove_str(s, subs)
                        for sub in subs:
                            if s in sub:
                                sub.remove(s)
                        break
        mx = 0
        for st in subs:
            if st:
                m = max([len(s) for s in st])
                mx = m if m > mx else mx
        return mx if mx else -1


    def all_subsequence(self, s:str, cur:str=None, output:set=None)->set:
        if None == output:
            output = set()
        if None == cur:
            cur = ''
        if not len(s):
            output.add(cur)
            return output
        for i in range(len(s)):
            _ = self.all_subsequence(s[i+1:], cur+s[i], output)
            _ = self.all_subsequence(s[i+1:], cur, output)
        return output

    def all_subsequence2(self, s:str, cur:str=None, output:list=None)->list:
        if None == output:
            output = []
        if not cur:
            cur = ''
        if len(s) == 0:
            if cur not in output:
                output.append(cur)
            return
        for i in range(len(s)):
            _ = self.all_subsequence2(s[i+1:], cur+s[i], output)
            _ = self.all_subsequence2(s[i+1:], cur, output)
        return output

    # Brutal force ver.1
    #  find all the subsequence of each string, removing the common ones
    def findLUSlength_BF1(self, strs: List[str]) -> int:
        substrs = []
        for st in strs:
            substrs.append(self.all_subsequence(st))
        for i in range(len(substrs)):
            for s in substrs[i]:
                for othersubstrs in substrs[:i]+substrs[i+1:]:
                    if s in othersubstrs:
                        self.remove_str(s, substrs)
        max_len = 0
        for lst in substrs:
            m = max([len(s) for s in lst])
            if m > max_len:
                max_len = m
        return max_len if max_len != 0 else -1

    def remove_str(self, s:str, strlists:list) -> None:
        for lst in strlists:
            if s in lst:
                lst.remove(s)





def test_fixture(solution):
    testdata = [  # (input, expect),
        # (["aba", "cdc", "eae"], 3),
        # (['ab','cde'], 3),
        # (['ab'], 2),
        (["ab","ab"], -1),
        (["yyab", "xabc"], 2),
        (["xaxby", "yyayef"], 6),
        (['ab', 'ba'], 2),
        (["ab", "ba", "aa"], 2),
        # ([], ),
        # ([], ),
    ]

    for i in range(len(testdata)):
        ret = solution.findLUSlength(testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t\t{} expect {}".format((testdata[i][0],testdata[i][1]), ret, 'pass' if ret==exp else 'fail', exp))


def test():
    s = Solution()
    test_fixture(s)


test()    

