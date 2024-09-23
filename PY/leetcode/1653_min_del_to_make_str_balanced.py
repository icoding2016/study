"""
1653. Minimum Deletions to Make String Balanced
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
Medium

You are given a string s consisting only of characters 'a' and 'b'​​​​.
You can delete any number of characters in s to make s balanced.
 s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
Return the minimum number of deletions needed to make s balanced.


Example 1:
Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

Example 2:
Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.


Constraints:
    1 <= s.length <= 105
    s[i] is 'a' or 'b'​​.

"""


from utils.testtools import test_fixture


class Solution:
    def minimumDeletions(self, s: str) -> int:
        N = len(s)
        ba = [[0,0] for _ in range(N)]    # (leftb, righta)
        leftb, righta = 0, 0
        for i in range(N):
            ba[i][0] = leftb
            ba[N-i-1][1] = righta
            if s[i] == 'b':
                leftb += 1
            if s[N-i-1] == 'a':
                righta += 1
            # print(ba)
        min_num = N
        for i in range(N):
            num = sum(ba[i])
            if num < min_num:
                min_num = num
        return min_num


def test():
    data = [
        (("aababbab",), 2),
        (("bbaaaaabb",), 2),
        (("bababababababababababbab",), 11),
    ]
    s = Solution()
    test_fixture(s.minimumDeletions, data)


test()


