"""

285. Inorder Successor in BST
Medium
https://leetcode.com/problems/inorder-successor-in-bst
https://leetcode.ca/all/285.html


Given a binary search tree and a node in it,
find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

 

Example 1:

Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1's in-order successor node is 2. 
Note that both p and the return value is of TreeNode type.

Example 2:

Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.

 

Note:
    If the given node has no in-order successor in the tree, return null.
    It's guaranteed that the values of the tree are unique.


"""


from collections import deque


class BTNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST():
    def __init__(self):
        self.root = None

    @staticmethod
    def generate(data:list) -> 'BST':
        """generte the tree form the input data (BFS order)"""
        if not data:
            return None
        root = BTNode(data[0])
        dq = deque([root, ])
        data = deque(data[1:])
        while dq and data:
            node = dq.popleft()
            lv = data.popleft()
            if lv != None:
                newnode = BTNode(lv)
                node.left = newnode
                dq.append(newnode)
            if data:
                rv = data.popleft()
                if rv != None:
                    newnode = BTNode(rv)
                    node.right = newnode
                    dq.append(newnode)
        bst = BST()
        bst.root = root
        return bst

    @staticmethod
    def bst_dfs(root:BTNode):
        if not root:
            # yield None
            return
        for x in BST.bst_dfs(root.left):
            yield x
        yield root.val
        for x in BST.bst_dfs(root.right):
            yield x

    def dfs(self):
        for x in BST.bst_dfs(self.root):
            yield x

    @staticmethod
    def bfs(root:BTNode):
        dq = deque([root, ])
        while dq:
            node = dq.popleft()
            if not node:
                continue
            yield node.val
            dq.append(node.left)
            dq.append(node.right)
    
    @staticmethod
    def bfs_data(root:BTNode) -> list:
        return [d for d in BST.bfs(root)]

    @staticmethod
    def level_data(root:BTNode) -> dict:
        def helper(node:BTNode, level:int, data:dict):
            if level not in data:
                data[level] = [node.val if node else None, ]
            else:
                data[level].append(node.val if node else None)
            if not node:
                return
            helper(node.left, level+1, data)
            helper(node.right, level+1, data)
        data = {}
        helper(root, 0, data)
        return data

    def __repr__(self):
        s = ""
        data = BST.level_data(self.root)
        levels = sorted(data.keys()) 
        for lvl in levels:
            for v in data[lvl]:
                s += f"  {v}  "
            s += '\n'
        return s

    def inorder_successor(self, val:int) -> int:
        found = False
        for x in self.dfs():
            if found:
                return x
            if x == val:
                found = True
        return None




def test_bst():
    data = [5,3,6,2,4,None,None,1]
    t = BST.generate(data)
    print(BST.bfs_data(t.root))
    print(t)
    print([v for v in BST.bst_dfs(t.root)])
    print(f"inorder successor of 3: {t.inorder_successor(3)}")
    print(f"inorder successor of 6: {t.inorder_successor(6)}")


test_bst()





