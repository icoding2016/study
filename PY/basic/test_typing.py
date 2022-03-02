
from typing import Iterable

print(isinstance(list(), Iterable))
print(isinstance(set(), Iterable))
print(isinstance(str(), Iterable))
print(isinstance(int(), Iterable))

s = str('a string')
if isinstance(s, Iterable):
    for x in s:
        print(x, end=',')

