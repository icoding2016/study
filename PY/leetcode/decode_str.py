# Decode String
# Medium
# https://leetcode.com/problems/decode-string/submissions/ 
#
# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; 
# No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
# For example, there won't be input like 3a or 2[4].
#
# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
#
# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
#
# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
#
# Example 4:
# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"
#
# Constraints:
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300]
#
# 
# 
# Idea:
#   parse the string,
#   1) the direct sub_str without [], put into result directly 
#   2) for <num>[<substr>], use 2 stacks to handle (num and sub_str),
#      for the case of <substr0><num>[<substr1><num>[<substr2>]<substr3>]
#                                                             ^ 
#                                              ----decoded----  after processing the inner ], the previously pushed substr1 should 
#                                                               be popped and join the decoded part, then continue the 'substr' processing
#  


from utils.testtools import test_fixture


class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) < 4:
            return s
        #return self.decodeStr1(s)
        return self.decodeStr_good(s)

    def decodeStr1(self, s: str) -> str:
        NUMS = [str(i) for i in range(10)]
        result = ''
        nums = []  # stack,   '[' trigger push, ']' trigger pop
        strs = []  # stack,   '[' trigger push, ']' trigger pop
        stack_count = 0
        in_num = False
        numstr = ''
        substr = ''
        for c in s:
            if c in NUMS:
                numstr += c
                if substr:
                    if stack_count:
                        strs.append(substr)
                    else:
                        result += substr
                    substr = ''
                else:
                    if stack_count and not in_num:
                        strs.append('')
                in_num = True
            elif c == '[':
                nums.append(int(numstr))
                stack_count += 1
                numstr = ''
                substr = ''
                in_num = False
            elif c == ']':
                if substr:
                    curstr = substr * nums.pop()
                substr = ''
                stack_count -= 1
                if stack_count:
                    substr = strs.pop() + curstr
                else:
                    result += curstr
            else:
                substr += c
        if substr:
            result += substr         
        return result

    # https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack
    def decodeStr_good(self, s: str) -> str:
        result = ''
        nums = []  # stack,   '[' trigger push, ']' trigger pop
        strs = []  # stack,   '[' trigger push, ']' trigger pop
        cur_num = 0
        cur_str = ''
        for c in s:
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == '[':
                nums.append(cur_num)
                strs.append(cur_str)
                cur_num = 0
                cur_str = ''
            elif c == ']':
                num = nums.pop()
                pre_str = strs.pop()
                cur_str = pre_str + cur_str * num
            else:
                cur_str += c
        return cur_str


def test():
    data = [
        (("abc",), "abc"),
        (("3[ab]",), "ababab"),
        (("10[a]b",), "aaaaaaaaaab"),
        (("2[2[ab]]",), "abababab"),
        (("3[a10[bc]]",), "abcbcbcbcbcbcbcbcbcbcabcbcbcbcbcbcbcbcbcbcabcbcbcbcbcbcbcbcbcbc"),
        (("a2[2[b]c]n",),"abbcbbcn"),
        (("3[a]2[bc]",), "aaabcbc"),
        (("2[abc]3[cd]ef",), "abcabccdcdcdef"),
        (("3[a2[c]]",), "accaccacc"),
        (("3[2[c]]",), "cccccc"),
        (("abc3[cd]xyz",), "abccdcdcdxyz"),
        (("ab2[cd3[e]]f2[g]xyz",), "abcdeeecdeeefggxyz"),
        (("3[a]2[bc]ef3[2[ab2[xy]n]]ww",), "aaabcbcefabxyxynabxyxynabxyxynabxyxynabxyxynabxyxynww"),
        (("3[a10[bc]]2[d]e3[2[ab2[xy]n]]w",), "abcbcbcbcbcbcbcbcbcbcabcbcbcbcbcbcbcbcbcbcabcbcbcbcbcbcbcbcbcbcddeabxyxynabxyxynabxyxynabxyxynabxyxynabxyxynw"),
    ]
    S = Solution()
    test_fixture(S.decodeString, data)



test()

