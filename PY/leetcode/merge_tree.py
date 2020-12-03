#  Merge Two Binary Trees
# Easy
# Given two binary trees and imagine that when you put one of them to cover the other, 
# some nodes of the two trees are overlapped while the others are not.
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, 
# then sum node values up as the new value of the merged node. Otherwise, 
# the NOT null node will be used as the node of new tree.
# 
# Example 1:
# Input: 
# 	Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7
# Note: The merging process must start from the root nodes of both trees.



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def create(data:list) -> 'TreeNode':
        N = len(data)
        if not data:
            return None
        if N == 1:
            return TreeNode(data[0])
        mid = N//2
        left = TreeNode.create(data[:mid])
        right = TreeNode.create(data[mid+1:])
        return TreeNode(data[mid], left, right)

    def show_dfs(self) -> None:
        if self.left:
            self.left.show_dfs()
        print(' ', self.val, end='')
        if self.right:
            self.right.show_dfs()

    def dfs(self) -> None:
        if self.left:
            for x in self.left.dfs():
                yield x
        yield self.val if self.val else None
        if self.right:
            for x in self.right.dfs():
                yield x


class Solution:
    # T(max(n1,n2))
    # S(max(hight1, hight2))
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None       
        val1 = t1.val if t1 else 0
        val2 = t2.val if t2 else 0
        val = int(val1 if val1 else 0) + int(val2 if val2 else 0)
        left = self.mergeTrees(t1.left if t1 else None, t2.left if t2 else None)
        right = self.mergeTrees(t1.right if t1 else None, t2.right if t2 else None)
        # print('tr1:{} ;  tr2:{}'.format(  \
        #     (t1.val, t1.left.val if t1.left else None, t1.right.val if t1.right else None) if t1 else None, \
        #     (t2.val, t2.left.val if t2.left else None, t2.right.val if t2.right else None) if t2 else None))
        return TreeNode(val, left, right)



def test_fixture(solution):
    testdata = [  # (input, expect),
        ([5,3,None,1,None,2,None], [None,1,4,2,None,3,7], [5,4,4,3,None,5,7]), 
    ]

    for i in range(len(testdata)):
        tree1 = TreeNode.create(testdata[i][0])
        tree2 = TreeNode.create(testdata[i][1])
        print('tree1: ', [n for n in tree1.dfs()])
        print('tree2: ', [n for n in tree2.dfs()])
        ret = [n for n in solution.mergeTrees(tree1, tree2).dfs()]
        # print('new tree: ', ret)
        print("{} \n-> {} \t\t{} expect {}".format((testdata[i][0],testdata[i][1]), ret, 'pass' if ret==testdata[i][2] else 'fail', testdata[i][2]))


def test():
    s = Solution()
    test_fixture(s)


test()    


