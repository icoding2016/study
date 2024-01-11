import numpy as np
import pandas 
import matplotlib
import pymysql
import requests
import bs4
import tk
import pytest

from itertools import permutations
import os
import sys
from dotenv import load_dotenv, find_dotenv

# cur_path = os.path.dirname(os.path.abspath(__file__))
# parent_path = os.path.join(*cur_path.split(os.sep)[:-1])
# sys.path.append(parent_path)
# print(sys.path)

load_dotenv(find_dotenv())
usr, pwd = os.getenv('username'), os.getenv('password')
print(usr, pwd)


## run a test
def perm(s:str, k:int=0, cur:list=None):
    if None == cur:
        cur = []
    if len(cur) >= k:
        yield ''.join(cur)
        return
    for i in range(len(s)):
        for y in perm(s[:i]+s[i+1:], k, cur+[s[i]]):
            yield y
        

def test_perm():
    data = [
        (('a', 1), permutations('a', r=1)),
        (('abc', 1), permutations('abc', r=1)),
        (('abc', 2), permutations('abc', r=2)),
        (('abc', 3), permutations('abc', r=3)),
    ]
    
    def comp_list(l1:list, l2:list) -> bool:
        return len(l1)==len(l2) and all([x in l2 for x in l1]) and all([x in l1 for x in l2])
    
    for d, e in data:
        ret = [x for x in perm(*d)]
        cmp = [''.join(x) for x in e]
        print(f"perm {d}: {'Pass' if comp_list(ret, cmp) else 'Fail'} {ret}")


    