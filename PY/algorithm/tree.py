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

    def walk(self, order='IN_ORDER'):
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

    def _walk_level(self, level: int, walk_log: dict, max_level: int):
        '''the depth first walk (in-order) with level information
           supporting breadth first walk

           walk_log: the dict recording the tree level nodes value {<level>:[<value list>]}
           max_level: used to record the max tree level (starting from 0) 
        '''
        if max_level < level:
            max_level = level

        if self.left:
            m1 = self.left._walk_level(level=level+1, walk_log=walk_log, max_level=max_level)
            max_level = m1 if m1 > max_level else max_level

        if level in walk_log.keys():
            walk_log[level].append(self.value)
        else:
            walk_log[level] = [self.value]

        if self.right:
            m2 = self.right._walk_level(level=level+1, walk_log=walk_log, max_level=max_level)
            max_level = m2 if m2 > max_level else max_level

        return max_level
        
    @staticmethod
    def breath_first_walk(root):
        '''Count & Remember the level of current node while walking through the tree
           Save the 'value' of current level to the list[level-id]
           Need to add a 'level' argument for depth_first_walk
        '''
        if not root:
            return {}   # empty result
        result = dict()  # { <level>:[list of values], ...}
        mxlvl = 0
        mxlvl = root._walk_level(level=0, walk_log=result, max_level=mxlvl)
        
        for lvl in range(mxlvl+1):
            print(lvl, result[lvl])



def test():
    values = [5,1,3,7,2,9,4,8,11,0,6,10]
    bt = BTree.generate(values)
    print('-'*30, "IN_ORDER")
    bt.walk()
    print('-'*30, "PRE_ORDER")
    bt.walk(order='PRE_ORDER')
    print('-'*30, "POST_ORDER")
    bt.walk(order='POST_ORDER')

    print('-'*30, "BREADTH_WALK")
    BTree.breath_first_walk(bt)

test()
