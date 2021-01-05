# Group Anagrams
# Medium 
# https://leetcode.com/problems/group-anagrams/
# 
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.
# 
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 
# Example 2:
# Input: strs = [""]
# Output: [[""]]
#
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
#
# Constraints:
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.
# 
# 
# Solution:
#   It's not mentioned if there are duplicate in strs 
# 
# 
#  #

from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return self.groupAnagrams1(strs)

    # T(N*LlogL)       L=max(len(s))
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            anagrams[key].append(s)
            # if s not in anagrams[key]:
            #     anagrams[key].append(s)
        return anagrams.values()
        



def test_fixture(solution):
    testdata = [  # (input, expect),
        (([""], ), [[""]]),
        ((["a"], ), [["a"]]),
        ((["eat","tea","tan","ate","nat","bat"], ), [["bat"],["nat","tan"],["ate","eat","tea"]]),
        ((["eat","tea","tan","ate","nat","bat",""],), [[""],["bat"],["nat","tan"],["ate","eat","tea"]]), 
    ]

    for i in range(len(testdata)):
        ret = solution.groupAnagrams(*testdata[i][0])
        exp = testdata[i][1]
        #print("{} -> \t{} \t expect {}".format(testdata[i][0], ret, exp))
        print("{}".format('pass' if comp_list_list(ret,exp) else 'fail'))

def comp_list_list(l1:list[list], l2:list[list])->bool:
    if len(l1) != len(l2):
        return False       
    ls1 = [set(x) for x in l1]
    ls2 = [set(x) for x in l2]
    if len(ls1) != len(ls2):
        return False       
    while len(ls1):
        s = ls1[0]
        if s in ls2:
            ls1.remove(s)
            ls2.remove(s)
        else:
            return False
    if not ls1 and not ls2:
        return True
    else:
        return False


def test():
    s = Solution()
    test_fixture(s)


test()    


