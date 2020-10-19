# Depth First Traversal: inorder, preorder, postorder
#   (a)Inorder (Left, Root, Right)
#   (b)Preorder (Root, Left, Right)
#   (c)Postorder (Left, Right, Root)
# Breadth First (Level Order) Traversal:
# 

from typing import Iterable

class BTree(object):
    ORDER = ["IN_ORDER", "PRE_ORDER", "POST_ORDER"]
    #def __init__(self, value: int, left: BTree =None, right: BTree = None):   # compiler error 'BTree is not defined'
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def generate(values):
        '''Generate a binary tree from the input values
           values:  an iterable object containing the values of the tree nodes
           return the root node of the tree
        '''
        if not isinstance(values, Iterable):
            print("input values not iterable.")
            return 
        node = BTree(value=None)
        for x in values:
            node.insert(x)
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

    def show(self):
        print(self.value)
        print(self.left)        
        print(self.right)

    def walk(self, order = 'IN_ORDER'):
        if not order in self.ORDER:
            print("Invalid order, need to be in {}".format(self.ORDER))
            return
        if order == "IN_ORDER":
            self._walk_in_order()
        elif order == "PRE_ORDER":
            self._walk_pre_order()
        else:
            self._walk_post_order()
        return

    def _walk_in_order(self):
        if self.left:
            self.left._walk_in_order()
        print("{} ".format(self.value))
        if self.right:
            self.right._walk_in_order()

    def _walk_pre_order(self):
        print("{} ".format(self.value))
        if self.left:
            self.left._walk_pre_order()
        if self.right:
            self.right._walk_pre_order()

    def _walk_post_order(self):
        if self.left:
            self.left._walk_post_order()
        if self.right:
            self.right._walk_post_order()
        print("{} ".format(self.value))


def test():
    values = [3,5,1,7,2,9,4,8,11,0,6,10]
    bt = BTree.generate(values)
    print('-'*30, "IN_ORDER")
    bt.walk()
    print('-'*30, "PRE_ORDER")
    bt.walk(order='PRE_ORDER')
    print('-'*30, "POST_ORDER")
    bt.walk(order='POST_ORDER')


test()
