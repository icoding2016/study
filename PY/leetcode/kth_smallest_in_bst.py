# Kth Smallest Element in a BST
# Medium
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
#  
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Example 1:
# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
#  
# Example 2:
# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
#  
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? 
# How would you optimize the kthSmallest routine?
#
# Constraints:
# The number of elements of the BST is between 1 to 10^4.
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.


# Supporting class of Tree Node
from typing import Iterable
class BTree:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def generate(values, sorted=True):
        '''Generate a binary tree from the input values
           values:  an iterable object containing the values of the tree nodes
           return the root node of the tree
        '''
        if not isinstance(values, Iterable):
            print("input values not iterable.")
            return 
        node = BTree(value=None)
        if sorted:
            for x in values:
                node.insert(x)
            return node
        else:
            for x in values:
                node.insert_random(x)
            return node

    def insert(self, value):
        if not self.value:
            self.value = value
            return
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BTree(value = value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BTree(value = value)

    @staticmethod
    def print_tree(root:'BTree') -> None:
        data = BTree.get_tree_level_data(root)
        for i in range(len(data)):
            print(data[i])


# T(logN+K)  -- logN to reach the min, then K more steps to reach the Kth
# S(logN)    -- Tree depth (Stack)
class Solution:
    def kthSmallest(self, root: BTree, k: int) -> int:
        return self._kthSmallest(root, k)

    def _kthSmallest(self, root: BTree, k: int) -> int:
        for i, v in enumerate(self.tree_dfs(root)):
            if i == k-1:
                return v

    def tree_dfs(self, root:BTree)->int:
        if root.left:
            for x in self.tree_dfs(root.left):
                yield x
        yield root.value
        if root.right:
            for x in self.tree_dfs(root.right):
                yield x

    def kthLargest(self, root: BTree, k: int) -> int:
        return self._kthLargest(root, k)

    def _kthLargest(self, root: BTree, k: int) -> int:
        for i, v in enumerate(self.tree_dfs_r(root)):
            if i == k-1:
                return v

    def tree_dfs_r(self, root:BTree)->int:
        if root.right:
            for x in self.tree_dfs_r(root.right):
                yield x
        yield root.value
        if root.left:
            for x in self.tree_dfs_r(root.left):
                yield x



    # Follow the procedure of DFS and count k
    # has issue (count logic ?)
    #  
    def _kthSmallest1(self, root: BTree, k: int) -> int:
        node = root
        S = []
        visited = []
        
        count = 0
        while count <= k:
            if node.left not in visited:
                while node.left:
                    S.append(node)
                    node = node.left
                count += 1
            if count >= k:
                return node.value
            if node.right and node.right not in visited:
                S.append(node)
                node = node.right
                visited.append(node)
                #count += 1
                continue
            else:
                if node not in visited:
                    visited.append(node)
                    count += 1
                node = S.pop()
        return None



def test():
    values = [5,1,3,7,2,9,4,8,11,0,6,10]
    bt = BTree.generate(values)

    s = Solution()
    print('get kth min')
    for k in range(1, len(values)+1):
        v = s.kthSmallest(bt, k)
        print("===={}th min: {}".format(k, v))
    print('get kth max')
    for k in range(1, len(values)+1):
        v = s.kthLargest(bt, k)
        print("===={}th max: {}".format(k, v))

    values2 = [3,1,4,2]
    bt2 = BTree.generate(values2)

    s2 = Solution()
    print('get kth min')
    for k in range(1, len(values2)+1):
        v = s2.kthSmallest(bt2, k)
        print("===={}th min: {}".format(k, v))
    print('get kth max')
    for k in range(1, len(values2)+1):
        v = s2.kthLargest(bt2, k)
        print("===={}th max: {}".format(k, v))
    


test()
