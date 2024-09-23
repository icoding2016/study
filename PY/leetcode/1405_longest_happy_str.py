"""
1405. Longest Happy String
Medium
https://leetcode.com/problems/longest-happy-string/

A string s is called happy if it satisfies the following conditions:

    s only contains the letters 'a', 'b', and 'c'.
    s does not contain any of "aaa", "bbb", or "ccc" as a substring.
    s contains at most a occurrences of the letter 'a'.
    s contains at most b occurrences of the letter 'b'.
    s contains at most c occurrences of the letter 'c'.

Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.


Example 1:
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Example 2:
Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.


Constraints:
    0 <= a, b, c <= 100
    a + b + c > 0

"""






class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        return self.recursive(a, b, c)
    
    def solution(self, a: int, b: int, c: int) -> str:
        letters = {'a':a, 'b':b, 'c':c}
        # l1 = {k:v for k, v in l1.items() if v}
        # ordered = sorted(l1, key=lambda x:l1[x], reverse=True)
        # total = sum(l1.values())
        # letters = {c:l1[c] for c in ordered}
        # l1, l2, l3 = ordered
        while any(list(letters.values())):
            ordered = sorted(letters, key=lambda x:letters[x], reverse=True)
            letters = {c:letters[c] for c in ordered if letters[c]}

        


    def recursive(self, a: int, b: int, c: int) -> str:
        l1 = {'a':a, 'b':b, 'c':c}
        ordered = sorted(l1, key=lambda x:l1[x], reverse=True)
        total = sum(l1.values())
        letters = {c:l1[c] for c in ordered}
        l1, l2, l3 = ordered
        fc = letters[l1]
        rc = total - fc
        end_len = total
        if fc >= rc * 2 + 2:
            end_len = rc * 3 + 2
            result = [l1] * end_len
            print(''.join(result))
            count = 0
            for i in range(2, end_len, 3):
                if count < letters[l2]:
                    result[i] = l2
                    count += 1
                else:
                    result[i] = l3
                    count += 1
            return ''.join(result)
        # print(letters)
        longest = ""
        ll = 0
        for x in self.buildstr(letters, ''):
            if len(x) >= end_len:
                return x
            if len(x) > ll:
                longest = x
                ll = len(x)
        return longest
        
    def buildstr(self, letters:dict, s:str):
        letters = {c:v for c, v in letters.items() if v>0}
        print(letters, s)
        if not any([letters.values()]):
            yield s
            return
        if len(letters) == 1:
            c = list(letters.keys())[0]
            if len(s)>1 and s[-2:]==f'{c}{c}':
                yield s
                return
        for c, v in letters.items():
            if not v:
                continue
            if ((s and s[-1] != c) or
               (len(s) < 2) or
               (len(s)>1 and s[-2:] != f'{c}{c}')):
                l2 = letters.copy()
                l2.update({c:v-1})
                for x in self.buildstr(l2, f'{s}{c}'):
                    yield x
            else:
                continue
        yield s



def test_fixture(solution):
    testdata = [  # (input, expect),
        ((1, 1, 7,), 'ccaccbcc'),
        ((4, 42, 7,), 'bbcbbcbbcbbcbbcbbcbbcbbabbabbabbabb'),
        # ((),),
    ]

    for i in range(len(testdata)):
        ret = solution.longestDiverseString(*testdata[i][0])
        exp = testdata[i][1]
        print("{} -> \t{} \t\t{} expect {}".format(testdata[i][0], ret, 'pass' if ret==exp else 'fail', exp))


def test():
    s = Solution()
    test_fixture(s)


test()    