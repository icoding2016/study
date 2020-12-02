# 5. Longest Palindromic Substring
# Medium
# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
# 
# Example 3:
# Input: s = "a"
# Output: "a"
# 
# Example 4:
# Input: s = "ac"
# Output: "a"
#
# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),
# 
# 
# Solution: brutal force
#   pick a 'middle' (1~n-2), check left/right for the longest palindrome & len, record
# 
# 
# 
# 


# brutal force
# T(N*N)
class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        longest = ''
        for cur in range(0, len(s)-1):
            left = cur
            for right in [left+1, left+2]:  # abba or baxab
                while left>=0 and right<len(s):
                    if s[left]==s[right]:
                        left -= 1
                        right += 1
                    else:
                        break
                cur_len = right - left -2
                if cur_len > max_len:
                    max_len = cur_len
                    longest = s[left+1:right] 
                left = cur           
        if max_len == 0:
            return s[0]
        return longest





def test_fixture(solution):
    input = [
        'cbbd',
        'a',
        'ac',
        'babad',
        'aabcdcbef',
        'abcbaaeeffeeh',
        'aaaaaaa',
    ]
    expect = [
        'bb',
        'a',
        'a',
        'bab',
        'bcdcb',
        'eeffee',
        'aaaaaaa',
    ]

    for i in range(len(input)):
        ret = solution.longestPalindrome(input[i])
        print("{} -> {} {}".format(input[i], ret, 'pass' if ret==expect[i] else 'fail'))


def test():
    s = Solution()
    test_fixture(s)


test()    



