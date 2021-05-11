from typing import Iterable
from utils.testtools import test_fixture, timing
import math

class LoopError(Exception):
    pass


def dfs(cur:int, graph:dict, path:list=None, visited:dict=None) -> None:
    if None == path:
        path = []
    if None == visited:
        visited = dict()
    if cur in path:
        raise LoopError
    for neighbor in graph[cur]:
        if neighbor not in path and neighbor not in visited:
            for x in dfs(neighbor, graph, path + [cur], visited):
                yield x
    visited[cur] = True
    yield cur


def test_dfs():
    graph = {
        1:[],
        2:[1],
        3:[1,2],
        4:[3, 1],
        5:[4,2,3],
        6:[3,4,2,1],
    }
    start = 4
    print(f'start {start}: {[v for v in dfs(start, graph)]}')
    start = 5
    print(f'start {start}: {[v for v in dfs(start, graph)]}')
    start = 6
    print(f'start {start}: {[v for v in dfs(start, graph)]}')
    start = 1
    print(f'start {start}: {[v for v in dfs(start, graph)]}')

# O(N)   N=num/2
def perfect_num(num: int) -> bool:
    # divisors = []
    s = 0
    for i in range(1, num//2+1):
        if num%i == 0:
            #divisors.append(i)
            s += i
    return s == num

# O(D)   D = num of divisors / 2
def perfect_num2(num: int) -> bool:
    divisors = dict()
    s = 0
    for x in range(1, num//2+1):
        if num%x == 0:
            y = int(num/x)
            if x in divisors:
                break
            else:
                s += x
                divisors[x] = True
                if y != x and y != num:
                    s += y
                    divisors[y] = True
    # print(divisors)
    return s == num

def perfect_num3(num: int) -> bool:
    divisors = dict()
    s = 0
    for x in range(1, int(math.sqrt(num))+1):
        if num%x == 0:
            y = int(num/x)
            if x in divisors:
                break
            else:
                s += x
                divisors[x] = True
                if y != x and y != num:
                    s += y
                    divisors[y] = True
    # print(divisors)
    return s == num

def test_perfect_number():
    data = [
        ((28,), True),
        ((6,), True),
        ((496,), True),
        ((8128,), True),
        ((2,), False),
        ((8,), False),
        ((28853,), False),
    ]
    test_fixture(perfect_num3, data)

@timing
def test_timing():
    s = 0
    for i in range(10000000):
        s += i
    return s


class BTree():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value) -> None:
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BTree(value)

    @classmethod
    def generate(cls, data:Iterable) -> 'BTree':
        head = None
        for d in data:
            if head:
                head.insert(d)
            else:
                head = BTree(d)
        return head

    def __str__(self):
        s = ''
        lvl = 0
        q = [(self,lvl),]
        while q:
            node, l = q[0]
            if node.left:
                q.append((node.left, l+1))
            if node.right:
                q.append((node.right, l+1))
            if l > lvl:
                s += '\n'
                lvl = l
            s += f'{node.value}, '
            del q[0]
        return s



def test_btree():
    data = [7,4,2,9,1,5,8,3,6,10,0]
    tree = BTree.generate(data)
    print(tree)


def test():
    #test_dfs()
    #test_perfect_number()
    #test_timing()
    test_btree()

    

test()










