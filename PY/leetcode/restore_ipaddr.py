# Restore IP Addresses
# Medium
# Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. 
# You can return them in any order.
# A valid IP address consists of exactly four integers, each integer is between 0 and 255, 
# separated by single dots and cannot have leading zeros. 
# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and 
# "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 
# 
# Example 1:
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# 
# Example 2:
# Input: s = "0000"
# Output: ["0.0.0.0"]
# 
# Example 3:
# Input: s = "1111"
# Output: ["1.1.1.1"]
# 
# Example 4:
# Input: s = "010010"
# Output: ["0.10.0.10","0.100.1.0"]
# 
# Example 5:
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        N = len(s)
        if N < 3 or N > 12:
            return []
        return [x for x in self.ipSection(s)]

    # T(3^4)   each ip section has 3 routings
    # S(1)   -- stack depth 4,  O(4)*O(12) -> O(1) const
    def ipSection(self, remain:str, sections:list[str]=None)->None:
        if None == sections:
            sections = []
        if not remain:
            if len(sections) == 4:
                yield '.'.join(sections)
            return
        elif remain and len(sections) >= 4:
            return
        for i in range(1, min(3, len(remain))+1):
            if remain[0] == '0':
                sections.append('0')
                for x in self.ipSection(remain[1:], sections):
                    yield x
                return
            if int(remain[:i]) > 255:
                continue
            for x in self.ipSection(remain[i:], sections + [remain[:i]]):
                yield x
        return





def test_fixture(solution):
    testdata = [  # (input, expect),
        ("", []),
        ("123", []),
        ("1234567890123", []),
        ("111999",['1.1.199.9','1.1.19.99', '1.11.99.9', '1.11.9.99', '1.119.9.9','11.1.9.99', '11.1.99.9', '11.19.9.9','111.9.9.9']),
        ("25525511135", ["255.255.11.135","255.255.111.35"]), 
        ("0000", ["0.0.0.0"]),
        ("1111", ["1.1.1.1"]),
        ("010010", ["0.10.0.10","0.100.1.0"]),
        ("101023", ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]),
    ]

    for i in range(len(testdata)):
        ret = solution.restoreIpAddresses(testdata[i][0])
        exp = testdata[i][1]
        ret.sort()
        exp.sort()
        print("{} \n-> \t{} \t\t{}\nexpect {}".format((testdata[i][0],testdata[i][1]), ret, 'pass' if ret==exp else 'fail', exp))


def test():
    s = Solution()
    test_fixture(s)


test()    
