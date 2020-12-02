# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);
#
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# 
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#  
# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"
#
# Constraints:
# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000
#
#
# Ideas 1)
#    pattern: row=n (start from 0), row(i) = ?
#  
# Idea 2)
#    Not by calculation, simple follow the zigzag rule to process the string, use flag to control direction
# 
# 
# #  



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return []
        if numRows == 1:
            return s
        rows = ['' for i in range(numRows)]

        rows[0] += s[0]
        row = 0
        for i in range(1, len(s)):
            direction = ((i-1) // (numRows-1))%2    # even: 0 -- down, odd 1 -- up,
            if direction == 0:  # down
                row += 1
            else:
                row -= 1
            rows[row] += s[i]
        return ''.join(rows)


def test_fixture(solution):
    input = [
        ("PAYPALISHIRING", 3),
        ("PAYPALISHIRING", 4),
        ("PAYPALISHIRING", 1),
        ("ABC", 2),
        ("ABC", 3),
        ("ABCD", 2),
        ("ABCD", 3),
        ("A", 1),
    ]
    expect = [
        "PAHNAPLSIIGYIR",
        "PINALSIGYAHRPI",
        "PAYPALISHIRING",
        "ACB",
        "ABC",
        "ACBD",
        "ABDC",
        "A",
    ]

    for i in range(len(input)):
        ret = solution.convert(input[i][0], input[i][1])
        print("{} -> {} {}".format((input[i][0], input[i][1]), ret, 'pass' if ret==expect[i] else 'fail'))


def test():
    sol = Solution()
    test_fixture(sol)


test()

