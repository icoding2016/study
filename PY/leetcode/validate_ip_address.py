"""
468. Validate IP Address
Medium
https://leetcode.com/problems/validate-ip-address/

Given a string IP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 
  0 <= xi <= 255 and xi cannot contain leading zeros. 
  For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", 
  while "192.168.1.00" and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:
  1 <= xi.length <= 4
  xi is a hexadecimal string which may contain digits, lower-case English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
  Leading zeros are allowed in xi.
  For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, 
  while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

 

Example 1:
Input: IP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:
Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:
Input: IP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.

Example 4:
Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334:"
Output: "Neither"

Example 5:
Input: IP = "1e1.4.5.6"
Output: "Neither"
 
Constraints:
IP consists only of English letters, digits and the characters '.' and ':'.

"""

from utils.testtools import test_fixture


class Solution:
    def validIPAddress(self, IP: str) -> str:
        if not IP:
            return 'Neither'
        sections = []
        section = ''
        v4flag = v6flag = False        
        for i, c in enumerate(IP):
            if c == '.':
                if v6flag:
                    return 'Neither'
                if i == len(IP)-1:
                    return 'Neither'
                v4flag = True
                sections.append(section)
                section = ''
            elif c == ':':
                if v4flag:
                    return 'Neither'
                if i == len(IP)-1:
                    return 'Neither'
                v6flag = True
                sections.append(section)
                section = ''
            elif c.isdigit():
                section += c
            elif self.validHexBit(c):
                if v4flag:
                    return 'Neither'
                v6flag = True
                section += c
            else:
                return 'Neither'
            if i == len(IP)-1:
                if section:
                    sections.append(section)
        if v4flag:
            if len(sections) != 4:
                return 'Neither'
            for s in sections:
                if not s or (s[0]=='0' and len(s)>1):
                    return 'Neither' 
                d = int(s)
                if d > 255:
                    return 'Neither'
            return 'IPv4'
        elif v6flag:
            if len(sections) != 8:
                return 'Neither'
            for s in sections:
                if len(s) < 1 or len(s)>4:
                    return 'Neither'
            return 'IPv6'
        return 'Neither'
            
    def validHexBit(self, c:str) -> bool:
        assert len(c)==1, 'input cannot > 1 char'
        valid_bits = [str(d) for d in range(0,10)] + \
                     [chr(c) for c in range(ord('a'), ord('f')+1)] + \
                     [chr(c) for c in range(ord('A'), ord('F')+1)]
        return c in valid_bits


def test():
    data = [

    ]
"""
test cases:
"172.16.254.1"
"0.1.234.42"
"111.32.255.223"
"111:32.255.223"
"0.0.0.0"
"1.00.43.0"
"10.3.134."
".1.3.4"
"1.4.264.88"
"34.4.d3.9"
"43..94.134"
"2001:0db8:85a3:0000:0000:8a2e:0370:7334"
"2001:db8:85a3:0:0:8A2E:0370:7334"
"F001:db8:85a3:0:0:8A2E:0370:BBBB"
"2001:0db8:85a3::8A2E:037j:7334"
"2001:db8:85a3:000:0:8A2E:0370:7334"
"02001:0db8:85a3:0000:0000:8a2e:0370:7334"
"2001:db8:85a3::0:8A2E:0370:7334"
"2001:db8:85a3:000H:0:8A2E:0370:7334"
"2001:db8::0:0:8A2E:0370:7334"
":db8:85a3:0:0:8A2E:0370:7334"
"2001:db8:85a3:0:0:8A2E:0370:7334:"
"2001:db8:85a3:0:0:8A2E:0370::"
"2001:db8:85a3:0:0:8A2E:7334"
"2001:db8:85a3:0:0:8A2E.7334"
"2001:db800:85a3:0:0:8A2E:7334"
""    
"""

