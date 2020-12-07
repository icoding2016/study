# Letter Combinations of a Phone Number
# Medium
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
# Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#  2:"abc"
#  3:"def"
#  4:"ghi"
#  5:"jkl"
#  6:"mno"
#  7:"pqrs"
#  8:"tuv"
#  9:"wxyz"     
#
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 
# Example 2:
# Input: digits = ""
# Output: []
# 
# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]
# 
# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


from typing import List



class Solution:
    num_map = {
        '2':"abc",
        '3':"def",
        '4':"ghi",
        '5':"jkl",
        '6':"mno",
        '7':"pqrs",
        '8':"tuv",
        '9':"wxyz",     
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        #return self.letterComb(digits)
        #return [x for x in self.letterCombIter(digits)]
        return self.letterComb2(digits)

    # T(L^d)   L--letters per digit, d--number of digits. worst case O(4^d)
    # S(d)     recursion hight: d (num of digit) 
    #       or S(d^2) if count the temp arg* size((digits[1:], cur+letter, output))
    def letterComb(self, digits: str,  cur:str=None, output:list=None) -> List[str]:
        if None == output:
            output = []
        if None == cur:
            cur = ''
        if not digits:
            output.append(cur)
            return output
        letters = self.num_map[digits[0]]
        for letter in letters:
            _ = self.letterComb(digits[1:], cur+letter, output)
        return output

    # T(L^d)
    # S(d)  or S(d^2) if count the temp arg
    def letterCombIter(self, digits: str,  cur:str='') -> None:
        if not digits:
            yield cur
            return
        for letter in self.num_map[digits[0]]:
            for x in self.letterCombIter(digits[1:], cur+letter):
                yield x
        return

    # T(L^d)   -- for each d loop, O(L*size(result))  so for d1: L1;  d2: L1*L2;  d3: L1*L2*L3 => L^d
    def letterComb2(self, digits: str) -> list:
        if not digits:
            return []
        result = []
        for d in digits:
            letters = self.num_map[d]
            if not result:
                result = [l for l in letters]
            else:
                result = [p + l for l in letters for p in result]
        return result




def test_fixture(solution):
    testdata = [  # (input, expect),
        ([""], []),
        (["2"], ['a', 'b', 'c']),
        (["23"], ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        (["29"], ["aw","ax","ay","az","bw","bx","by","bz","cw","cx","cy","cz"]),
        (["239"], ["adw","adx","ady","adz","aew","aex","aey","aez","afw","afx","afy","afz","bdw","bdx","bdy","bdz","bew","bex","bey","bez","bfw","bfx","bfy","bfz","cdw","cdx","cdy","cdz","cew","cex","cey","cez","cfw","cfx","cfy","cfz"]),
    ]

    for i in range(len(testdata)):
        ret = solution.letterCombinations(*testdata[i][0])
        exp = sorted(testdata[i][1])
        print("{} -> \t{} \t\t{} expect {}".format(testdata[i][0], ret, 'pass' if sorted(ret)==exp else 'fail', exp))


def test():
    s = Solution()
    test_fixture(s)


test()    

