# Valid Palindrome II
# Easy
# https://leetcode.com/problems/valid-palindrome-ii/

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:
# Input: s = "aba"
# Output: true

# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.

# Example 3:
# Input: s = "abc"
# Output: false

# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.


from utils.testtools import test_fixture


class Solution:
    def validPalindrome(self, s: str) -> bool:
        # return self.validPalindrome_1(s)
        return self.validPalindrome_2(s)


    # Time Limit Exceeded.
    # T(N*N)
    def validPalindrome_1(self, s: str) -> bool:
        if self.checkPalindrome(s):
            return True
        for i in range(len(s)):
            if self.checkPalindrome(s[:i]+s[i+1:]):
                return True
        return False

    def checkPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        if len(s) == 2:
            return s[0]==s[1]
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                return False
        return True

    # T(N)    N + N (first fix) + N (2nd fix)
    def validPalindrome_2(self, s: str, fix:int=0) -> bool:
        if fix > 1:
            return False
        if len(s) == 1 and fix <= 1:
            return True
        if len(s) == 2 and fix <= 1 and s[0]==s[1]:
            return True
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                if fix > 0:
                    return False
                if self.validPalindrome_2(s[i+1:len(s)-i], fix+1):
                    return True
                if self.validPalindrome_2(s[i:len(s)-i-1], fix+1):
                    return True
                return False
        return True



def test():
    data = [
        (("a",), True),
        (("aa",), True),
        (("ab",), True),
        (("abca",), True),
        (("abc",), False),
        (("aba",), True),
        (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",), True),
        (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabb",), False),
        (("yd",), True),
        # ((,), ),
        # ((,), ),
    ]
    s = Solution()
    test_fixture(s.validPalindrome, data)


test()

