"""
91. Decode Ways
Medium
https://leetcode.com/problems/decode-ways/description/

A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.
 

Example 1:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").

"""


class Solution:
    def numDecodings(self, s: str) -> int:
        # self.map = [chr(ord("A") + i) for i in range(26)]
        return self.dp(s)

    def numDecodings_r(self, s: str) -> int:
        total = 0
        for x in self.decode(s):
            total += 1 if x else 0
        return total

    # T: O(2^N)
    # S: O(logN)
    def decode(self, s):
        if not s:
            yield True
            return
        if s[0] == "0":
            yield False
            return
        if len(s) == 1:
            yield True
            return
        elif int(s[:2]) <= 26:
            for x in self.decode(s[1:]):
                yield x
            for x in self.decode(s[2:]):
                yield x
        else:
            for x in self.decode(s[1:]):
                yield x

    # T: O(N)
    # S: O(N)
    def dp(self, s):
        if s[0] == "0":
            return 0
        dp = [0] * (len(s))
        dp[0] = 1
        if len(s) >= 2:
            n = int(s[:2])
            if s[0] not in ["1", "2"] and s[1] == "0":
                return 0
            dp[1] = 2 if (n <= 26 and s[1] != "0") else 1
        for i in range(2, len(s)):
            # print(i, s[i], dp)
            if s[i] == "0":
                if s[i - 1] not in ["1", "2"]:
                    return 0
                dp[i] = dp[i - 2]
                continue
            dp[i] += dp[i - 1]
            if s[i - 1] == "0":
                continue
            if int(s[i - 1 : i + 1]) <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s) - 1]


test_data = [
    # 1 digit, 2 digit, >2 digit,
    # invalid: 0 start, contains > 26 only case, eg 30;  or 0x only case, eg 803
    # some typical combinations:  10,20, 26;  continues >2 num, eg. 3548
    ("0", 0),
    ("1", 1),
    ("9", 1),
    ("19", 2),
    ("26", 2),
    ("28", 1),
    ("20", 1),
    ("03", 0),
    ("123", 3),
    ("312", 2),
    ("3042", 0),
    ("31410", 2),
    ("394820571308201243210", 0),
    # ("",),
    # ("",),
]


def test():
    solution = Solution()
    print("DP solution")
    for d, ep in test_data:
        ret = solution.numDecodings(d)
        print(f"{d} -> {ret} (expect {ep}): {'Pass' if ep==ret else 'Fail'}")

    print("Recursive solution")
    for d, ep in test_data:
        ret = solution.numDecodings_r(d)
        print(f"{d} -> {ret} (expect {ep}): {'Pass' if ep==ret else 'Fail'}")


test()
