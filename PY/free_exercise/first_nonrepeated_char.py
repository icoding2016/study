"""
Find the 1st non-repeated character in a string.

Given a string. Write a function to find the first nonrepeated character in that string. 

example: suppose you are given the string “interview”. 
The first nonrepeated character in that string is ‘n’, because ‘i’ appears twice in the string. 
And the first nonrepeated character for “racecar” is ‘e’ – which is the first and only nonrepeated character. 
Explain the efficiency of your algorithm.

"""


from utils.testtools import test_fixture


# T(N)
def find_first_non_repeat(s:str) -> str:
    counter = dict()
    for c in s:
        if c not in counter:
            counter[c] = 1
        else:
            counter[c] += 1
    for c, v in counter.items():
        if v == 1:
            return c
    return None


def test():
    data = [
        (('interview',), 'n'),
        (('racecar',), 'e'),
        (('aaaaaaa',), None),
        (('aaaaaaba',), 'b'),
        (('ababababab',), None),
        (('a',), 'a'),
    ]
    test_fixture(find_first_non_repeat, data)


test()
