"""
re

.search() ⇒ find something anywhere in the string and return a match object.
.match() ⇒ find something at the beginning of the string and return a match object.
.findall() ⇒ find all the occurances. (by defalt in the single line; re.M enable multi line)

"""

import re



test_str="""something starting at the beginning line,
something starting at the second line,
and something in the middle of the 3rd line.
"""

def test_match_search(s:str, p:str):
    pat = re.compile(p)
    result = pat.search(s)
    print(f"search: {result}")
    result = pat.match(s)
    print(f"match: {result}")
    result = pat.findall(s)
    print(f"findall: {result}")

    patm = re.compile(p, re.M)
    result = patm.search(s)
    print(f"search re.M: {result}")
    result = patm.match(s)
    print(f"match, re.M: {result}")
    result = patm.findall(s)
    print(f"findall, re.M: {result}")

    print('-'*30)


def test():
    p1 = r"some\w*ing"
    p2 = r"^some\w*ing"

    test_match_search(test_str, p1)
    test_match_search(test_str, p2)


test()    