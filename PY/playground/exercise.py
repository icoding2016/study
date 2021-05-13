from typing import Iterable
from utils.testtools import test_fixture, timing
import math

class LoopError(Exception):
    pass


def graph_dfs(cur:int, graph:dict, path:list=None, visited:dict=None) -> None:
    if None == path:
        path = []
    if None == visited:
        visited = dict()
    if cur in path:
        raise LoopError
    for neighbor in graph[cur]:
        if neighbor not in path and neighbor not in visited:
            for x in graph_dfs(neighbor, graph, path + [cur], visited):
                yield x
    visited[cur] = True
    yield cur


def test_graph_dfs():
    graph = {
        1:[],
        2:[1],
        3:[1,2],
        4:[3, 1],
        5:[4,2,3],
        6:[3,4,2,1],
    }
    start = 4
    print(f'start {start}: {[v for v in graph_dfs(start, graph)]}')
    start = 5
    print(f'start {start}: {[v for v in graph_dfs(start, graph)]}')
    start = 6
    print(f'start {start}: {[v for v in graph_dfs(start, graph)]}')
    start = 1
    print(f'start {start}: {[v for v in graph_dfs(start, graph)]}')


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

    def inorder(self) -> None:
        if self.left:
            for x in self.left.inorder():
                yield x
        yield self.value
        if self.right:
            for x in self.right.inorder():
                yield x

    def dfs(self):
        if self.left:
            for x in self.left.dfs():
                yield x
        if self.right:
            for x in self.right.dfs():
                yield x
        yield self.value

    def bfs(self):
        buf = [self]
        while buf:
            cur = buf[0]
            if cur.left:
                buf.append(cur.left)
            if cur.right:
                buf.append(cur.right)
            yield cur.value
            del buf[0]



def test_btree():
    data = [7,4,2,9,1,5,8,3,6,10,0]
    tree = BTree.generate(data)
    print(tree)
    
    print('-- inorder --')
    print([x for x in tree.inorder()])

    print('-- dfs --')
    print([x for x in tree.dfs()])

    print('-- bfs --')
    print([x for x in tree.bfs()])


class LinkedNode(object):
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    @classmethod
    def generate_raw(cls, data:list) -> 'LinkedNode':
        """Generate the linked list from the data per it's original order"""
        cur = head = None
        for d in data:
            node = LinkedNode(d)
            if not head:
                head = node
                cur = node
            else:
                cur.next = node
                cur = node
        return head

    @classmethod
    def generate_ascending(cls, data:list) -> 'LinkedNode':
        """Generate the linked list from the data in ascending order.
        Returns:    head
        """
        head = None
        for d in data:
            if not head:
                head = LinkedNode(d)
            else:
                head = head.insert(d)
        return head

    def tail(self) -> 'LinkedNode':
        cur = self
        while cur.next:
            cur = cur.next
        return cur

    def insert(self, value) -> None:
        """Insert a new value to the list, assume the list is sorted (ascending order)"""
        cur = head = self
        pre = None
        node = LinkedNode(value)
        while cur:
            if value > cur.value:
                pre = cur
                cur = cur.next
                if not cur:
                    pre.next = node
                    break
            elif value == cur.value:
                node.next = cur.next
                cur.next = node
                break
            else:
                if not pre:
                    node.next = head
                    head = node
                else:
                    pre.next = node
                    node.next = cur
                break
        return head

    @classmethod
    def sort(cls, head:'LinkedNode') -> 'LinkedNode':
        if not head:
            return head
        pre = head
        cur = head.next        
        while cur:
            if cur.value >= pre.value:
                pre = cur
                cur = cur.next
                continue
            else:
                pre.next = None
                head = head.insert(cur.value)
                pre = head.tail()
                cur = cur.next
                pre.next = cur
        return head

    def reverse(self) -> 'LinkedNode':
        pre = head = self
        cur = self.next
        next = None
        while cur:
            next = cur.next
            cur.next = pre
            if pre == self:
                pre.next = None  # tail
            head = cur
            pre = cur
            cur = next
        return head

    def __str__(self):
        s = f"{str(self.__class__).split('.')[-1][:-2]}: "
        cur = self
        while cur:
            s += f'{cur.value}'
            cur = cur.next
            if cur:
                s += '->'
        return s

def find_intersection_of_linked_nodes(l1:LinkedNode, l2:LinkedNode) -> LinkedNode:
    """Find intersection node in 2 linked lists."""
    rec1 = dict()
    rec2 = dict()
    p1 = l1
    p2 = l2
    while p1 or p2:
        if p1:
            if p1 in rec2:
                return p1
            else:
                rec1[p1] = True
                p1 = p1.next
        if p2:
            if p2 in rec1:
                return p2
            else:
                rec2[p2] = True
                p2 = p2.next
    return None

def test_find_intersection_of_linked_nodes():
    l1 = LinkedNode.generate_raw([5,7,2,9,4,1,6,8,3])
    l2 = LinkedNode.generate_raw([15,13,12,19,11,14,17,16,18])
    l3 = LinkedNode.generate_raw([24,26,21,23,22,25])
    l1.tail().next = l3
    l2.tail().next = l3
    print('test find_intersection_of_linked_nodes:')
    print(f'l1: {l1}')
    print(f'l2: {l2}')
    node = find_intersection_of_linked_nodes(l1,l2)
    print(f'intersection: {node} ({node.value})')

def merge_sorted_linked_list(l1:LinkedNode, l2:LinkedNode) -> LinkedNode:
    cur = head = None
    while l1 or l2:
        if l1 and not l2:
            if cur:
                cur.next = l1
            else:
                head = l1
            break
        elif l2 and not l1:
            if cur:
                cur.next = l2
            else:
                head = l2
            break
        lsmall = l1 if l1.value < l2.value else l2
        if l1.value < l2.value:
            l1 = l1.next
        else:
            l2 = l2.next
        if cur:
            cur.next = lsmall
            cur = cur.next
        else:
            cur = head = lsmall
    return head

def test_merge_sorted_linked_list():
    data = [
        ((LinkedNode.generate_ascending([7,5,9,3,1]), LinkedNode.generate_ascending([6,4,8,2,10,0])),LinkedNode.generate_ascending([i for i in range(11)])),
        ((LinkedNode.generate_ascending([6,7,10,8,9]), LinkedNode.generate_ascending([3,4,1,5,2,0])), LinkedNode.generate_ascending([i for i in range(11)])),
        ((LinkedNode.generate_ascending([5,3,1]), LinkedNode.generate_ascending([6,2,5,4])), LinkedNode.generate_ascending([5,6,2,5,3,1,4])),
        ((LinkedNode.generate_ascending([7,5,9,3,1]), None), LinkedNode.generate_ascending([7,5,9,3,1])),
        ((None, LinkedNode.generate_ascending([7,5,9,3,1])), LinkedNode.generate_ascending([7,5,9,3,1])),
        ((None, None), None)
    ]
    def eql_ln(l1, l2):
        p1 = l1
        p2 = l2
        while p1 or p2:
            if (p1 and not p2) or (p2 and not p1):
                return False
            if p1.value != p2.value:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
    test_fixture(merge_sorted_linked_list, data, comp=eql_ln, hide_input=True)

def test_linked_list():
    data = [7,4,2,3,9,8,5,1,6]
    print('generate_raw')
    ll = LinkedNode.generate_raw(data)
    print(ll)
    print('sort')
    lls = LinkedNode.sort(ll)
    print(lls)
    print('reverse')
    llr = LinkedNode.reverse(lls)
    print(llr)
    print('generate_ascending')
    ll1 = LinkedNode.generate_ascending(data)
    print(ll1)


def reserse_substr(s1:str, s2:str) -> str:
    """Find if s2 is a substring in s1, if yes, reverse it in s1
    Return: processed s1, or s1 if s2 not found.
    """
    if len(s1) < len(s2):
        return s1
    elif len(s1) == len(s2):
        if s1==s2[::-1]:
            return s2
        else:
            return s1
    newstr = ''
    i = 0
    while i < len(s1):
        if i < len(s1)-len(s2) and s1[i:i+len(s2)] == s2:
            newstr += s2[::-1]
            i += len(s2)
        else:
            newstr += s1[i]
            i += 1
    return newstr


def test_reverse_substr():
    s1 = 'the original string containing substrings for string reversing test.'
    s2 = 'ing'
    s = reserse_substr(s1, s2)
    print(s1)
    print(s)


def zigzag_str(s:str, Z:int) -> str:
    """Zigzag traverse s, with Z rows."""
    if Z <= 1:
        return s
    rows = [[] for i in range(Z)]
    G = 2*Z-2
    for i in range(len(s)):
        j = i%G
        if j < Z:
            rows[j].append(s[i])
        else:
            rows[2*Z-j-2].append(s[i])
    ret = ''
    for row in rows:
        ret += ''.join(row)
    return ret

def zigzag_str2(s:str, Z:int) -> str:
    """Zigzag traverse s, with Z rows."""
    if Z <= 1:
        return s
    rows = [[] for i in range(Z)]
    r = 0
    fwd = True
    for i in range(len(s)):
        rows[r].append(s[i])
        if fwd:
            if r == Z-1:
                fwd = False
        else:
            if r == 0:
                fwd = True
        r += 1 if fwd else -1
    ret = ''
    for row in rows:
        ret += ''.join(row)
    return ret


def test_zigzag_str():
    s = 'abcdefghijklmn'
    data = [
        ((s, 1), 'abcdefghijklmn'),
        ((s, 2), 'acegikmbdfhjln'),
        ((s, 3), 'aeimbdfhjlncgk'),
        ((s, 4), 'agmbfhlnceikdj'),
    ]
    test_fixture(zigzag_str, data)
    test_fixture(zigzag_str2, data, hide_input=True)


def test():
    #test_graph_dfs()
    #test_perfect_number()
    #test_timing()
    test_btree()
    test_linked_list()
    test_find_intersection_of_linked_nodes()
    test_merge_sorted_linked_list()
    # test_reverse_substr()
    # test_zigzag_str()
    

test()










