# Alinked list is a data structure that represents a sequence of nodes (A->B->C...)
# 
#
# typical operations /algorithms
#  - reverse, 
#  - sort(!)
#    Idea:  have a sortHead and sortTail pointer, to through the link, put smaller ahead of sortHead, bigger behind sortTail and others in between
#  - remove duplicates
#  - Return Kth to Last
#  - Delete middle node
#    delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, 
#    e.g.  a->b->c->d->e->f   -->  a->b->d->e->f 
#  - Sum
#    You have two numbers represented by a linked list, where each node contains a single
#    digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
#    function that adds the two numbers and returns the sum as a linked list.
#    EXAMPLE
#      Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
#      Output: 2 -> 1 -> 9. That is, 912.
#    FOLLOW UP *
#      Suppose the digits are stored in forward order. Repeat the above problem.
#      Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
#      Output: 9 -> 1 -> 2. That is, 912.
#      Idea:  1) reserve the link while travelling to the end, do 'adding'
#  - Partition(!): 
#     Write code to partition a linked list around a value x, such that all nodes less than x come
#     before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
#     to be after the elements less than x (see below). The partition element x can appear anywhere in the
#     "right partition"; it does not need to appear between the left and right partitions.
#     EXAMPLE
#      Input:  3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
#      Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
#     Idea: shead, bhead, cur-> move through the list, 
#  - Palindrome:
#    Implement a function to check if a linked list is a palindrome.  
#    Idea:  method 1) use stack to record the 1st half data, use fast/slow runner to locate the middle position
#           method 2) use recursive 
#  - Intersection:
#    Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
#    node. Note that the intersection is defined based on reference, not value. That is, if the kth
#    node of the first linked list is the exact same node (by reference) as the jth node of the second
#    linked list, then they are intersecting.
#  - Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.  
#      Input: A -> B -> C - > D -> E -> C [the same C as earlier]
#      Output: C
#    Idea: 1) stack 
#          2) fast/slow runner --  Much like two cars racing around a track at different steps, they must eventually meet.
#   
# Note !!
#  - Key Methods:
#    1) Fast/Slow Runner
#    2) Recursive 
#  - Something very easy to make mistake -- when updating a tail pointer, remember to set it's 'next' to None.
#    otherwise, it may impact the check loop.
#  


from typing import TypeVar
from typing import Sequence

T = TypeVar('T')

class LinkedNode(object):
    def __init__(self, data:T) -> None:
        self.data = data
        self.next = None

    def insert(self, data: T) -> 'LinkedNode':
        '''Insert the data in front of current node'''
        new_node = LinkedNode(data)
        new_node.next = self
        self = new_node
        return self
    
    def append(self, data:T) -> None:
        '''Append the data to the tail'''
        node = self
        while node:
            if not node.next:
                tail = LinkedNode(data)
                node.next = tail
                return
            node = node.next

    def remove(self, data:T) -> None:
        '''Remove the first matched data in the list from the beginning'''
        if self.data == data:
            next = self.next
            self.next = None
            self = next
            return
        prev = self
        cur = prev.next
        while cur:
            next = cur.next
            if cur.data == data:
                prev.next = cur.next
                cur.next = None
                return
            prev = cur
            cur = next

    def len(self) -> int:
        count = 0
        node = self
        while node:
            count += 1
            if not node.next:
                break
            node = node.next
        return count

    def get_node(self, data:T) -> 'LinkedNode':
        node = self
        while node:
            if node.data == data:
                return node
            node = node.next
        return None

    def get_tail(self) -> 'LinkedNode':
        node = self
        while node:
            if not node.next:
                return node
            node = node.next
        return None


    def show(self) -> None:
        '''show the linked list from current node'''
        node = self
        while node:
            print('{}'.format(node.data), end='')
            node = node.next
            if node:
                print(' -> ', end='')
        print('')

    def __str__(self) -> str:
        s = '{}: {}'.format(type(self), self.data)
        # node = self
        # while node:
        #     s = s + '{}'.format(node.data)
        #     if node.next:
        #         s = s + ' -> '
        #     node = node.next
        return s

    @staticmethod
    def create(d:Sequence[T]) -> 'LinkdedNode':
        head = None
        for x in d:
            if not head:
                head = LinkedNode(x)
            else:
                head.append(x)
        return head

    @staticmethod
    def reverse(head: 'LinkedNode') -> 'LinkedNode':
        '''Reverse a linked list, return the new head'''
        h1 = head
        c = h1.next
        h1.next = None
        while c:
            h2 = c.next
            c.next = h1
            h1 = c
            c = h2 
        return h1

    @staticmethod
    def join(head1:'LinkedNode', head2:'LinkedNode') -> 'LinkedNode':
        if not head1 or not head2:
            return head1
        node = head1
        last = head1
        while node:
            last = node
            node = node.next
        last.next = head2
        return head1

    @staticmethod
    def remove_dup(head: 'LinkedNode') -> 'LinkedNode':
        h1 = head
        #cur = head.next
        while h1:
            cur = h1.next
            pre = h1
            while cur:
                if h1.data == cur.data:
                    pre.next = cur.next
                    cur.next = None
                pre = cur
                cur = cur.next
            h1 = h1.next
        return head

    @staticmethod
    def remove_middle(head:'LinkedNode') -> None:
        if not head.next or not head.next.next:
            return
        h1 = head
        h2 = head.next.next
        while h2:
            pre = h1
            h1 = h1.next
            if not h2.next or not h2.next.next:  # end
                pre.next = pre.next.next
                h1.next = None
                return
            h2 = h2.next.next

    @staticmethod
    def partition(head:'LinkedNode', x:T) -> 'LinkedNode':
        '''partition those < x left to those >=x'''
        shead = None
        bhead = None
        s = b = None
        cur = head
        while cur:
            if cur.data < x:
                if not shead:
                    shead = cur
                else:
                    s.next = cur
                s = cur
                cur = cur.next
                continue
            else:   #   >= x
                if not b:
                    bhead = cur
                else:
                    b.next = cur
                b = cur
                cur = cur.next
                continue
        if b:
            b.next = None
        if s:
            s.next = bhead
            return shead
        else:
            return head

    @staticmethod
    def sort(head:'LinkedNode') -> 'LinkedNode':
        if not head:
            return None
        shead = stail = head    # sorted head / tail
        cur = head.next
        while cur:
            next = cur.next
            if cur.data < shead.data:
                cur.next = shead
                shead = cur
            elif cur.data > stail.data:
                stail.next = cur
                stail = cur
                stail.next = None
            else:  # in between
                p = shead
                pre = shead
                while p != stail.next:
                    if cur.data > p.data:
                        pre = p
                        p = p.next
                        continue
                    else:
                        pre.next = cur
                        cur.next = p
                        break
            cur = next
        stail.next = None
        return shead

    @staticmethod
    def is_palindrome(head:'LinkedNode') -> bool:
        '''palindrome, stack solution'''
        if not head or not head.next:
            return False
        if not head.next.next:
            if head.data == head.next.data:
                return True
            else:
                return False
        stack = []
        h1 = head
        h2 = head  #.next.next
        while h2:
            if not h2.next:
                break
            stack.append(h1.data)
            if not h2.next.next:
                break
            h1 = h1.next
            h2 = h2.next.next
        node = h1.next
        while node:
            if node.data != stack.pop():
                return False
            node = node.next
        return True

    @staticmethod
    def is_palindrome2(head:'LinkedNode') -> bool:
        '''palindrome, recursive solution'''
        def is_palindrome_recursive(head:'LinkedNode', length:int) -> bool:
            if length == 0:
                return True, head
            if length == 1:
                return True, head.next
            result, node = is_palindrome_recursive(head.next, length -2)
            if not result:
                return result, node.next
            return head.data == node.data, node.next

        length = head.len()
        result, _ = is_palindrome_recursive(head, length)
        return result


    @staticmethod
    def is_intersection(head1:'LinkedNode', head2:'LinkedNode') -> 'LinkedNode':
        if not head1 or not head2:
            return None
        records = {}  # dict is hash-table, better performance than list
        h1 = head1
        h2 = head2
        while h1:
            records[h1] = h1
            h1 = h1.next
        while h2:
            if h2 in records:
                return h2
            h2 = h2.next

    @staticmethod
    def loop_detection(head:'LinkedNode')-> 'LinkedNode':
        node = head
        stack = {}
        while node:
            if node in stack:
                print('Loop detected')
                return node                
            stack[node] = 1
            node = node.next
        return None


def test_linked_list():
    data = [3,5,2,7,1,6,4,8,10,9,0]
    data1 = [3,3,5,2,7,5,1,6,4,5,8,10,1,9,0,1]
    data2 = [0,1,2,3,4,5,6,7,8,9]
    data3 = [(5,5),(1,1),(2,2),(9,9),(6,6),(3,3),(7,7),(4,4),(0,0),(8,8)]

    head = None
    for d in data:
        if not head:
            head = LinkedNode(d)
        else:
            head.append(d)
            #head = head.insert(d)
    head.show()

    head = LinkedNode.create(data3)
    print(head)

    # reverse
    head = LinkedNode.reverse(head)
    head.show()

    # remove
    head.remove(6)
    head.show()

    # remove dup
    head = LinkedNode.create(data1)
    head = LinkedNode.remove_dup(head)
    head.show()

    # remove middle
    head = LinkedNode.create(data2)
    LinkedNode.remove_middle(head)
    head.show()
    data2.append(11)
    head = LinkedNode.create(data2)
    LinkedNode.remove_middle(head)
    head.show()

    # partition
    head = LinkedNode.create(data)
    head = LinkedNode.partition(head, 5)
    head.show()

    # sort
    head = LinkedNode.create(data)
    head.show()
    print('sort: ')
    head = LinkedNode.sort(head)
    head.show()

    # Palindrome
    palindrom_func = LinkedNode.is_palindrome2    # LinkedNode.is_palindrome
    ll = [1,2,3,4,3,2,1]
    head = LinkedNode.create(ll)
    print('check Palindrome for {}: '.format(ll), palindrom_func(head))
    ll = [1,2,3,3,2,1]
    head = LinkedNode.create(ll)
    print('check Palindrome for {}: '.format(ll), palindrom_func(head))
    ll = [1,1]
    head = LinkedNode.create(ll)
    print('check Palindrome for {}: '.format(ll), palindrom_func(head))
    ll = [1,2,1]
    head = LinkedNode.create(ll)
    print('check Palindrome for {}: '.format(ll), palindrom_func(head))
    ll = [1,2,3, 2]
    head = LinkedNode.create(ll)
    print('check Palindrome for {}: '.format(ll), palindrom_func(head))

    # in_intersection
    h0 = LinkedNode.create([0,1,2,3])
    h1 = LinkedNode.create([11,12,13])
    h2 = LinkedNode.create([21,22,23,24,25])
    h1 = LinkedNode.join(h1, h0)
    h2 = LinkedNode.join(h2, h0)
    node = LinkedNode.is_intersection(h1, h2)
    print('check intersection: ', node)

    # loop detection
    ll = [1,2,3,4,5,3]
    head = LinkedNode.create(ll)
    node = head.get_node(3)
    tail = head.get_tail()
    tail.next = node
    print('Detect loop at: {}'.format(LinkedNode.loop_detection(head)))



def test():
    test_linked_list()    


test()
