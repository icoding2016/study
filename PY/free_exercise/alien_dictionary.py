# Verifying an Alien Dictionary
# https://leetcode.com/problems/verifying-an-alien-dictionary/
# 
# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. 
# The order of the alphabet is some permutation of lowercase letters.
# Given a sequence of words written in the alien language, and the order of the alphabet, 
# return true if and only if the given words are sorted lexicographicaly in this alien language.

# Example 1:
# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) 
# According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are English lowercase letters.

class InvalidInputException(Exception):
    pass


def solution(words:list[str], order:str) -> bool:
    dic = {order[i]:i for i in range(len(order))}
    for i in range(len(words) - 1):
        if cmp(words[i], words[i+1], dic) > 0:
            return False
        continue
    return True

def cmp_ch(a:str, b:str, d:dict) -> int:
    if len(a) > 1 or len(b) > 1:
        raise InvalidInputException('Input a or b should be a character, not a string')
    if d[a] > d[b]:
        return 1
    elif d[a] < d[b]:
        return -1
    else:
        return 0

def cmp(a:str, b:str, d:dict) -> int:
    for i in range(min(len(a), len(b))):
        c = cmp_ch(a[i], b[i], d) 
        if c > 0:
            return 1
        elif c < 0:
            return -1
        else:
            continue
    # same so far
    if len(a) == len(b):
        return 0
    if len(a) > len(b):
        return 1
    else:
        return -1


def test(words, dic):
    print("{},{}".format(words, dic),  end=' ')
    print(solution(words, dic))


test(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")    # Ture
test(["word","world","row"], "worldabcefghijkmnpqstuvxyz")  # False
test(["apple","app"], "abcdefghijklmnopqrstuvwxyz")         # False