# Find All Anagrams in a String
# Medium
# https://leetcode.com/problems/find-all-anagrams-in-a-string/
#  
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
# The order of output does not matter.
#
# Example 1:
# Input:
# s: "cbaebabacd" p: "abc"
# Output:
# [0, 6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# 
# Example 2:
# Input:
# s: "abab" p: "ab"
# Output:
# [0, 1, 2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".






from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        return self._findAnagrams2(s, p)
        
    def _findAnagrams1(self, s: str, p: str) -> List[int]:
        LS = len(s)
        LP = len(p)
        if LP > LS:
            return []
        
        result = []
        for i in range(LS-LP+1):
            if s[i] not in p:
                continue
            if self.checkAnagram2(s[i:i+LP], p):
                result.append(i)
        return result
    
    def _findAnagrams2(self, s: str, p: str) -> List[int]:
        LS = len(s)
        LP = len(p)
        if LP > LS:
            return []
        
        result = []
        pc = Counter(p)
        for i in range(LS-LP+1):
            if s[i] not in p:
                continue
            sc = Counter(s[i:i+LP])
            if sc == pc:
                result.append(i)
        return result
    
    def checkAnagram(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter(s2)
        if len(c1) != len(c2):
            return False
        for x, c in c1.items():
            if x not in c2:
                return False
            elif c != c2[x]:
                return False
        return True
    
    def checkAnagram2(self, s1: str, s2: str) -> bool:
        l1 = [x for x in s1]
        l2 = [x for x in s2]
        while l1:
            x = l1[0]
            if x not in l2:
                return False
            l1.remove(x)
            l2.remove(x)
        return True if not l2 else False

        