# Reverse Nodes in k-Group
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# Follow up:
# Could you solve the problem in O(1) extra memory space?
# You may not alter the values in the list's nodes, only nodes itself may be changed.
#
# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
#  
# Example 2:
# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
#
# Example 3:
# Input: head = [1,2,3,4,5], k = 1
# Output: [1,2,3,4,5]
#
# Example 4:
# Input: head = [1], k = 1
# Output: [1]
#
# Constraints:
# The number of nodes in the list is in the range sz.
# 1 <= sz <= 5000
# 0 <= Node.val <= 1000
# 1 <= k <= sz



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



# Solution 1:  Use stack to do the reverse
# 
def reverse_in_k(head:list, k:int)->list:
    if k == 1:
        return head
    p = head
    pre = None
    post = None
    while p:
        stk = []
        n = 0
        start = p
        while n < k:
            stk.append(p.data)
            n += 1
            p = p.next
            if not p and n < k:
                if pre:
                    pre.next = start
                    return head
                else:
                    return start
            if not p and n == k:
                post = None
            elif p and n == k:
                post = p
        while stk:
            if pre:
                pre.next = LinkedNode(stk.pop())
                pre = pre.next
            else:
                pre = LinkedNode(stk.pop())
                head = pre
        p = post
    return head


# Solution 2: 
# Todo



def test_func(f, k):
    print(f.__name__, 'k=', k)
    def run_test(data, f, k):
        ln = LinkedNode.create(data)
        if ln:   ln.show()
        ln2 = f(ln, k)
        if ln2:  ln2.show()
    run_test([1,2,3,4,5,6], f, k)
    run_test([], f, k)
    run_test([1], f, k)
    run_test([1,2], f, k)
    run_test([1,2,3], f, k)
    run_test([1,2,3,4], f, k)
    run_test([1,2,3,4,5], f, k)



def test():
    test_func(reverse_in_k, 1)
    test_func(reverse_in_k, 2)
    test_func(reverse_in_k, 3)


test()
