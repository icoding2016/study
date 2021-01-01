# Remove Nth Node From End of List
# Medium
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#   
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Follow up: Could you do this in one pass?
#
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# 
# Example 2:
# Input: head = [1], n = 1
# Output: []
# 
# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
#
# Constraints:
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
# code:
#   https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def List(head:'ListNode')->list:
        if not head:
            return []
        def iterList(head):
            node = head
            while node:
                yield node.val
                node = node.next
        return [x for x in iterList(head)]

    @staticmethod
    def generate(data:list)->'ListNode':
        head = None
        cur = None
        for d in data:
            node = ListNode(d) 
            if not head:
                head = node
            else:
                cur.next = node
            cur = node
        return head


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        return self.removeNthFromEnd1(head, n)

    # T(N)
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        if not head.next:    # constraints:  sz>=1, 1<=n<=sz
            return []
        p1 = p2 = head
        c = 0
        while p2:
            if not p2.next:   # end
                if c < n:
                    return head.next 
                p1.next = p1.next.next if p1.next else None
                return head
            p2 = p2.next
            if c >= n:
                p1 = p1.next
            c += 1


def test_fixture(solution):
    testdata = [  # (input, expect),
        (([1,2,3,4,5], 1), [1,2,3,4]),
        (([1,2,3,4,5], 2), [1,2,3,5]),
        (([1,2,3,4,5], 5), [2,3,4,5]),
        (([1], 1), []),
        (([1,2], 1), [1]),
        (([1,2], 2), [2]),
    ]

    for i in range(len(testdata)):
        ret = solution.removeNthFromEnd(ListNode.generate(testdata[i][0][0]), testdata[i][0][1])
        exp = testdata[i][1]
        ll = ListNode.List(ret)
        print("{} -> \t{} \t\t{} expect {}".format(testdata[i][0], ll, 'pass' if ll==exp else 'fail', exp))


def test():
    s = Solution()
    test_fixture(s)


test()    



