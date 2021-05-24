"""
Valid Palindrome III
hard
https://leetcode.com/problems/valid-palindrome-iii

Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.

 

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
 

Constraints:

1 <= s.length <= 1000
s has only lowercase English letters.
1 <= k <= s.length
"""


from utils.testtools import test_fixture


class Solution:
    def validPalindrome(self, s: str, k:int) -> bool:
        return self.validPalindrome_r(s, k)


    # T(N*k)    N (first fix) + N (2nd fix) ...
    def validPalindrome_r(self, s: str, k: int, fix:int=0) -> bool:
        if fix > k:
            return False
        if len(s) == 1 and fix <= k:
            return True
        if len(s) == 2 and fix <= k and s[0]==s[1]:
            return True
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                if fix > k-1:
                    return False
                if self.validPalindrome_r(s[i+1:len(s)-i], k, fix+1):
                    return True
                if self.validPalindrome_r(s[i:len(s)-i-1], k, fix+1):
                    return True
                return False
        return True



def test():
    data = [
        (("a",0), True),
        (("aa",0), True),
        (("ab",1), True),
        (("abca",1), True),
        (("abc",1), False),
        (("abc",2), True),
        (("aba",0), True),
        (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",1), True),
        (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabb",1), False),
        (("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabb",2), True),
        (("aaaaacaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabb",2), False),
        (("aaaaacaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabb",3), True),
        # ((,), ),
        # ((,), ),
    ]
    s = Solution()
    test_fixture(s.validPalindrome, data)


test()



