# Depth First Traversal: inorder, preorder, postorder
#   (a)Inorder (Left, Root, Right)
#   (b)Preorder (Root, Left, Right)
#   (c)Postorder (Left, Right, Root)
# Breadth First (Level Order) Traversal:
# 


import random
from typing import Iterable
from typing import TypeVar

T = TypeVar('T')

class BTree(object):
    ORDER = ["IN_ORDER", "PRE_ORDER", "POST_ORDER"]

    #def __init__(self, value: int, left: BTree =None, right: BTree = None):   # compiler error 'BTree is not defined'
    def __init__(self, value:T = None) -> None:
        self.value = value
        self.left = None
        self.right = None

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

    def insert_random(self, value):
        if not self.value:
            self.value = value
            return
        r = random.random()*10
        node = self.left if r < 5 else self.right
        if r < 5:
            if not self.left:
                self.left = BTree(value)
                return
            else:
                self.left.insert_random(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BTree(value = value)

    def find_node(self, data:T) -> 'BTree':
        if self.value == data:
            return self
        node = None
        if self.left:
            node = self.left.find_node(data)
            if node:
                return node
        if self.right:
            node =self.right.find_node(data)
        return node

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
                             O(N)   (N=Node count).   N=2^L or L=LogN
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
    def get_tree_level_data(root:'BTree', level:int = 0, data:dict = {}) -> list:
        if not root:
            return data

        if level in data:
            data[level].append(root.value)
        else:
            data[level] = [root.value]

        if root.left:
            BTree.get_tree_level_data(root.left, level + 1, data)
        if root.right:
            BTree.get_tree_level_data(root.right, level + 1, data)
        return data

    @staticmethod
    def print_tree(root:'BTree') -> None:
        data = BTree.get_tree_level_data(root)
        for i in range(len(data)):
            print(data[i])
        

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

    @staticmethod
    def compare_tree_topo(root1, root2):
        '''To compare 2 trees structure
           return True if structure matchs, otherwise False
        '''
        # walk the tree and record 'walk pattern' ('l'-left,'r'-right,'b'-back)
        left = 'L'
        right = 'R'
        back = 'B'
        trail1 = root1.walk_trail()
        trail2 = root2.walk_trail()
        print(trail1)
        print(trail2)
        return trail1 == trail2
        

    def walk_trail(self, trail: list = None):
        if trail is None:
            trail = []
        
        if self.left:
            trail.append('L')
            self.left.walk_trail(trail)
        if self.right:
            trail.append('R')
            self.right.walk_trail(trail)
        trail.append('B')
        return trail

    def get_random_node(self) -> 'BTree':
        ''' this is not a good solution, 'hight'-steps doesn't randomize well when the tre is not balanced '''
        steps = random.randint(1, BTree.hight(self))
        node = self
        while steps and node:
            if steps <= 1:
                return node
            if random.randint(0,1):
                if node.right:
                    node = node.right
                else:
                    return node
            else:
                if node.left:
                    node = node.left
                else:
                    return node
            steps -= 1
        return self

    def kth_min_node(self, k:int)->'BTree':
        return self._kth_min_node(k)

    def _kth_min_node(self, k:int, count:dict=None)->'BTree':
        if k<1:
            return None
        if None == count:
            count = {0:0}
 
        if self.left:
            print(count[0], self.value, "go left")
            n = self.left._kth_min_node(k, count)
            if n:
                return n
        else:
            count[0] += 1
        if count[0] >= k:
            return self
        if self.right:
            print(count[0], self.value, "go right")
            n = self.right._kth_min_node(k, count)
            if n:
                return n
        else:
            print(count[0], self.value, "go up")
            return None


    # To find the kth largest node
    def kth_max_node(self, k:int)->'BTree':
        return self._kth_max_node(k)

    # reach the most 'right' -- the max node, mark  k-1
    # repeat k times to reach the most right.
    def _kth_max_node(self, k:int, result:'BTree'=None)->'BTree':
        if k < 1:
            return None
        if k==1:
            return self if result else None
        
        if not self.right:
            if k == 1:
                result = self
                return self     # found kth max
            # fall back
            if self.left:
                result = self.left._kth_max_node(k-1, result)
            else:
                return result     # k-1 required

        else:
            return self.right._kth_max_node(k, result)


        # if not self.left and not self.right:
        #     if k == 1:
        #         return self
        #     return None     # k-1
        # if self.right:
        #     n = self.right._kth_max_node(k)
        #     if n:
        #         return n
        #     else:
        #         k -= 1
        # else:
        #     if k == 1:
        #         return self

        # if self.left:
        #     return self.left._kth_max_node(k-1)

        # return None


        # if not self.right:
        #     if k==1:
        #         return self
        #     if self.left:
        #         return self.left._kth_max_node(k-1)
        # else:
        #     return self.right._kth_max_node(k)


def test_walk_trail():
    data1 = [1,3,2,4,7,5,6,8]
    data2 = [11,13,12,13,17,15,16,18]
    data3 = [1,3,2,4,8,5,6,7]
    tree1 = BTree.generate(data1)
    tree2 = BTree.generate(data2)
    tree3 = BTree.generate(data3)
    result = BTree.compare_tree_topo(tree1, tree2)
    print('tree1 & tree2:','match' if result else 'not match')
    result = BTree.compare_tree_topo(tree1, tree3)
    print('tree1 & tree3:','match' if result else 'not match')


def test():
    values = [5,1,3,7,2,9,4,8,11,0,6,10]
    bt = BTree.generate(values)
    print("find node 7", bt.find_node(7))
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

    test_walk_trail()

    # get_random_node
    print('get_random_node')
    for i in range(10):
        print(bt.get_random_node().value, end=',')
    print('')

    print('get kth min')
    for k in range(1, len(values)+1):
        n = bt.kth_min_node(k)
        v = n.value if n else None
        print("===={}th min: {}".format(k, v))
    print('get kth max')
    for k in range(1, len(values)+1):
        n = bt.kth_max_node(k)
        v = n.value if n else None
        #print("{}th max: {}".format(k, v))


test()
