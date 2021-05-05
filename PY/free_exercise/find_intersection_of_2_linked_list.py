# Find intersection node of 2 linked lists 
# Easy


class LinkedNode(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    @classmethod
    def generate(cls, data:list) -> 'LinkedNode':
        head = None
        cur = None
        for d in data:
            if not cur:
                head = LinkedNode(d)
                cur = head
            else:
                cur.next = LinkedNode(d)
                cur = cur.next
        return head

    def tail(self) -> 'LinkedNode':
        cur = self
        while cur:
            if not cur.next:
                return cur
            cur = cur.next

    def find(self, value) -> 'LinkedNode':
        cur = self
        while cur:
            if cur.value == value:
                return cur
            cur = cur.next
        return None

    @classmethod
    def show(cls, head: 'LinkedNode') -> None:
        cur = head
        while cur:
            print(cur.value, end='')
            cur = cur.next
            if cur:
                print(', ', end='')
        print('')

    def __str__(self) -> str:
        s = ''
        cur = self
        while cur:
            s += str(cur.value)
            cur = cur.next
            if cur:
                s += ', '
        return s


# T(M+N)   M=len(l1), N=len(l2)
# S(M+N)
def find_intersect_node(l1: LinkedNode, l2: LinkedNode) -> LinkedNode:
    p1 = l1
    p2 = l2
    path1 = dict()
    path2 = dict()
    while p1 or p2:
        if p2 and p2 in path1:
            return p2
        if p1 and p1 in path2:
            return p1
        if p1:
            path1[p1] = True
            p1 = p1.next
        if p2:
            path2[p2] = True
            p2 = p2.next
    return None

def test():
    l1 = LinkedNode.generate([i for i in range(10)])
    l2 = LinkedNode.generate([i for i in range(20,25)])
    l2.tail().next = l1.find(7)

    print(f'l1: {l1}')
    print(f'l2: {l2}')
    isn = find_intersect_node(l1, l2)
    print(f'intersection: {isn.value if isn else None}')
    
    
test()
