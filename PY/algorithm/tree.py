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

    def _walk_level(self, level: int, walk_log: dict):
        '''the depth first walk (in-order) with level information
           supporting breadth first walk

           walk_log: the dict recording the tree level nodes value {<level>:[<value list>]}
        '''
        if self.left:
            self.left._walk_level(level=level+1, walk_log=walk_log)

        if level in walk_log.keys():
            walk_log[level].append(self.value)
        else:
            walk_log[level] = [self.value]

        if self.right:
            self.right._walk_level(level=level+1, walk_log=walk_log)

    def print_level(self, level: int):
        if level <= 0:
            print(self.value, end=' ')
            return
        if self.left:
            self.left.print_level(level=level-1)
        if self.right:
            self.right.print_level(level=level-1)

    @staticmethod
    def hight(tree):
        ''' Count the tree hight
            Time Complexity: O(2^L) (L=level) -- 1+2+4+..+2^(L-1)=2^L-1
                             O(N)  (L=Node count).   N=2^L or L=LogN
            Space Complexity: O(N)?
        '''
        if not tree.left and not tree.right:
            return 1
            
        l_hight = 0
        r_hight = 0
        if tree.left:
            l_hight = BTree.hight(tree.left) + 1
        if tree.right:
            r_hight = BTree.hight(tree.right) + 1

        return l_hight if l_hight > r_hight else r_hight
        

    @staticmethod
    def breath_first_walk(root):
        '''Count & Remember the level of current node while walking through the tree
           Save the 'value' of current level to the list[level-id]
           Need to add a 'level' argument for depth_first_walk
        '''
        if not root:
            return {}   # empty result
        result = dict()  # { <level>:[list of values], ...}
        root._walk_level(level=0, walk_log=result)
        
        for lvl in range(BTree.hight(root)):
            print("level {}: {}".format(lvl, result[lvl]))



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
    print('hight', BTree.hight(bt))
    BTree.breath_first_walk(bt)

    print('-'*30, "Print level")
    bt.print_level(0); print("")
    bt.print_level(1); print("")
    bt.print_level(2); print("")

test()
