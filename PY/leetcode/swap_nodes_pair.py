#Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes. Only nodes itself may be changed.
#
# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#
# Example 2:
# Input: head = []
# Output: []
#
# Example 3:
# Input: head = [1]
# Output: [1]
#
# Constraints:
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100


class LinkedNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    @staticmethod
    def create(data:list) -> 'LinkedNode':
        head = None
        pre = None
        for x in data:
            n = LinkedNode(x)
            if not head:
                head = n
            else:
                pre.next = n
            pre = n
        return head

    def show(self):
        p = self
        while p:
            print(p.data, end='')
            if p.next:
                print('->',end='')
            p = p.next
        print('')


# T(N)
def swap_in_pair(head:LinkedNode)->LinkedNode:
    if not head or not head.next:
        return head
    
    pre = None
    post = None
    p1 = head
    while p1:
        # one node    
        p2 = p1.next   
        if not p2:
            pre.next = p1
            break
        
        # 2 nodes
        post = p2.next
        p2.next = p1
        p1.next = None
        if pre:
            pre.next = p2
        else:
            head = p2
        pre = p1        
        p1 = post
    return head



def test_func(f):
    print(f.__name__)
    def run_test(data, f):
        ln = LinkedNode.create(data)
        if ln:   ln.show()
        ln2 = f(ln)
        if ln2:  ln2.show()
    run_test([1,2,3,4,5,6], f)
    run_test([], f)
    run_test([1], f)
    run_test([1,2], f)
    run_test([1,2,3], f)
    run_test([1,2,3,4], f)
    run_test([1,2,3,4,5], f)



def test():
    test_func(swap_in_pair)


test()
