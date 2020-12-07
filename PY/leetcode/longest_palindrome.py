# Longest Palindrome
# Easy
# Given a string s which consists of lowercase or uppercase letters, 
# return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
#
# Example 1:
# Input: s = "abccccdd"
# Output: 7 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# Example 2:
# Input: s = "a"
# Output: 1
# 
# Example 3:
# Input: s = "bb"
# Output: 2
#
# Constraints:
# 1 <= s.length <= 2000
# s consits of lower-case and/or upper-case English letters only.

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        total = 0
        single = False
        for ch, c in counter.items():
            if c%2 == 1:
                single = True
                total += c-1
            else:
                total += c
        total += 1 if single else 0
        return total        


def test_fixture(solution):
    testdata = [  # (input, expect),
        ("a", 1),
        ("abccccdd", 7),
        ("bb", 2),
        ("bba",3),
        ("bbaaa", 5), 
        ("abbcdeeef", 5),
    ]

    for i in range(len(testdata)):
        ret = solution.longestPalindrome(testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t\t{} expect {}".format((testdata[i][0],testdata[i][1]), ret, 'pass' if ret==exp else 'fail', exp))


def test():
    s = Solution()
    test_fixture(s)


test()    

