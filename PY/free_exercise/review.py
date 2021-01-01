# to review & exercise the basic ds & algorithms
# DS: list, linked list, queue, stack, heap, tree, graph
# Algorithms: permutation, combination, n choose k, shortest path (), tsp, topology sort, knapsack, sorting, 
# Methods:  recursion, 2 pointers, greedy, divide & conque, top down, bottom up, dp
# 
# 
# 
# #

class LinkedNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self) -> str:
        s = ''
        n = self
        while n:
            s += str(n.val)
            if n.next:
                s += '->'
            n = n.next
        return s

    @staticmethod
    def create(data)->'LinkedNode':
        head = None
        pre = None
        for n in data:
            node = LinkedNode(n)
            if not head:
                head = node
            else:
                pre.next = node
            pre = node
        return head

    @staticmethod
    def reverse(head:'LinkedNode') ->'LinkedNode':
        if not head:
            return head
        p1 = head
        pre = None
        nxt = None
        while p1:
            p2 = p1.next
            nxt = p2.next if p2.next else None
            p2.next = p1
            p1.next = pre
            pre = p2
            p1 = nxt
        return pre
        
    # has issue
    @staticmethod
    def sort(head: 'LinkedNode')->'LinkedNode':
        if not head:
            return None
        sp = head
        p1 = head.next
        while p1:
            p2 = p1.next
            sp2 = sp
            pre = None
            while sp2 and sp2.val < p1.val:
                pre = sp2
                sp2 = sp2.next
            if not sp2: 
                pre.next = p1
            elif not pre:  # sp2 big
                p1.next = sp
                sp = p1
            else:
                spnext = pre.next
                pre.next = p1
                p1.next = spnext
            p1 = p2
        return sp
    
    # not verified
    def kth2last(self, K:int)->'LinkedNode':
        p1=p2=self
        for i in range(K):
            if p2:
                p2 = p2.next
            else:
                return None
        while p2:
            p2 = p2.next
            p1 = p1.next
        return p1

    # 
    def isPalindrome(self)->bool:
        if not self:
            return False
        if not self.next:
            return True
        s = []
        p1 = p2 = self
        rp = None
        while p2:
            if p2.next:
                s.append(p1.val)
                if  p2.next.next:
                    p1 = p1.next
                    p2 = p2.next.next
                else:
                    rp = p1.next
                    break
            else:
                rp = p1.next
                break
        while s:
            if rp.val != s.pop():
                return False
            rp = rp.next
        return True                
                




def test_LinkedNode():
    data = [n for n in range(10)]
    head = LinkedNode.create(data)
    print(head)
    print('reverse')
    r = LinkedNode.reverse(head)
    print(r)

    data2 = [3,5,2,7,1,4,6,0]
    head = LinkedNode(data2)
    print('sort')
    print(head)
    print(' -> ', LinkedNode.sort(head))

    print('palindrome')
    d = [1,2,3,2,1]
    head = LinkedNode.create(d)
    print(d, head.isPalindrome())
    d = [1,2,3,3,2,1]
    head = LinkedNode.create(d)
    print(d, head.isPalindrome())
    d = [1,2,3,4,2,1]
    head = LinkedNode.create(d)
    print(d, head.isPalindrome())


def test():
    test_LinkedNode()


test()    



