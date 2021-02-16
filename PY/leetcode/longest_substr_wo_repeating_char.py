# Longest Substring Without Repeating Characters
# Medium
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.
 
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example 4:
# Input: s = ""
# Output: 0

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # return self.longestSubstr_bf(s)
        return self.longestSubstr_dp(s)

    # T(N*N)
    def longestSubstr_bf(self, s: str) -> int:
        if not s:
            return 0
        N = len(s)
        ml = 0
        cur = ''
        cur_ij = None
        for i, v in enumerate(s):
            li = 1
            for j in range(i+1,N):
                if s[j] not in s[i:j]:
                    li += 1
                else:
                    break
            if li > ml:
                ml = li
                cur_ij = (i,j-1)
        return ml
                    
    # say cur record the substr without dup up to now
    # dp[i]=(maxlen_i, (start, end))
    # dp[i+1]= a) (maxlen_i+1, (start, i+1))      if end==i and s[i+1] not in s[start,end+1]
    #          b) (maxlen_i, (start, end))        if end==i and s[i+1] in s[start,end+1], and maxlen_i > 1
    #          c) (1, (i+1, i+1)) -> cur,mx=cur   if end==i and s[i+1]==s[i], and maxlen_i <= 1
    #          d) (maxlen_i, (start, end))        if end<i and s[i]!=s[i+1], and maxlen_i > cur[0]+1,  update cur
    #          e) (maxlen_i, (start, end))        if end<i and s[i]==s[i+1], update cur(1,(i+1,i+1))
    #          f) (cur[0]+1, (cur-s, cur-e))      if end<i and s[i]!=s[i+1], and maxlen_i <= cur[0]+1,  update cur, max
    # T(N*N)    loop-N, inside the loop, worst case N for for the case .rfind() or s[i] in s[ms:me+1]
    def longestSubstr_dp(self, s: str) -> int:
        if not s:
            return 0
        dp = [(1, (0,0))]     # (maxlen, (start, end))
        cur = mx = dp[0]
        for i in range(1, len(s)):
            mx = dp[i-1]
            ms = mx[1][0]
            me = mx[1][1]
            if me+1 == i:
                if s[i] not in s[ms:me+1]:
                    mx = (mx[0]+1, (ms, i))
                    cur = mx
                else:
                    ik = s[:me+1].rfind(s[i])
                    cur = (i-ik, (ik+1, i))
                    if mx[0] <= cur[0]:
                        mx = cur               
            elif s[i] not in s[cur[1][0]:cur[1][1]+1]:
                cur = (cur[0]+1, (cur[1][0], i))
                if cur[0] >= mx[0]:
                    mx = cur 
            else:
                ik = s[:cur[1][1]+1].rfind(s[i])
                cur = (i-ik, (ik+1, i))
                if mx[0] <= cur[0]:
                    mx = cur
            dp.append(mx)
        return max([t[0] for t in dp])

def test_fixture(s):
    testdata = [  # (input, expect),
        (("abcabcbb",),  3),
        (("bbbbbb",),  1),
        (("pwwkew",),  3),
        (("",),  0),
        (("abcabcbbjjkadadfkgjlafa;ljjgia;fooqutaaadtyuiolvjk;laf",), 12)
    ]

    for i in range(len(testdata)):
        ret = s.lengthOfLongestSubstring(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t expect {}".format(testdata[i][0], ret, exp), end='\t')
        print("{}".format('pass' if ret==exp else 'fail'))


import timeit
def test():
    s = Solution()
    test_fixture(s)

test()



