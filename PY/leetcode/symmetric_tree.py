"""
101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/submissions/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?

"""


from typing import List
from utils.testtools import test_fixture



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod    
    def generate(data: List[int]) -> 'TreeNode':
        if not data:
            return None
        head = TreeNode(data[0])
        nodes = [head,]
        i = 1
        while nodes:
            node = nodes.pop(0)
            if data[i] != None:
                node.left = TreeNode(data[i])
                nodes.append(node.left)
            else:
                node.left = None
            i+=1
            if i >= len(data):
                break
            if data[i] != None:
                node.right = TreeNode(data[i])
                nodes.append(node.right)
            else:
                node.right = None
            i+=1
            if i>=len(data):
                break
        return head
            

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return False
        # return Solution.check_symmetric_trees(root.left, root.right)
        return self.check_symmetric(root)

    # Recursive solution
    # T(2^H)    H = hight of the tree (logN)
    @staticmethod
    def check_symmetric_trees(t1:TreeNode, t2:TreeNode) -> bool:
        if not t1 and not t2:
            return True
        if (t1 and not t2) or (t2 and not t1):
            return False
        if t1.val != t2.val:
            return False
        return Solution.check_symmetric_trees(t1.left, t2.right) and Solution.check_symmetric_trees(t1.right, t2.left)

    #
    def check_symmetric(self, root:TreeNode) -> bool:
        if not root:
            return False
        stack =[[root.left, root.right]]
        while stack:
            left, right = stack.pop()
            if left == right:  # including None
                continue
            if (left and not right) or (not left and right):
                return False
            if left.val != right.val:
                return False
            stack.append([left.left, right.right])
            stack.append([left.right, right.left])
        return True



def test():
    data = [
        ((TreeNode.generate([1,2,2,3,4,4,3]),), True),
        ((TreeNode.generate([1,2,2,3,None,None,3,None,4,4,None]),), True),
        ((TreeNode.generate([1,2,2,3,4,3,4]),), False),
    ]
    s = Solution()
    test_fixture(s.isSymmetric, data)


test()

