# Serialize and deserialize general binary tree
# The tree is not ordered
# 
# Serialization is the process of translating a data structure or object state into a format 
# that can be stored (for example, in a file or memory data buffer) or transmitted (for example, 
# over a computer network) and reconstructed later (possibly in a different computer environment).
# 
# Idea,
#   serialiaze: generate list[tree.value] per dfs/bfs, then serialize the list.
#   deserialize: deserialze the list, then create_from_data the try by dfs/bfs
#   so     Tree <--> list[value] <--> serialize/deserialize
#   To turn the tree into a create_from_dataable list, 'None' node is needed to mark the leaf
# 
# 
#  


from enum import Enum
from typing import TypeVar
import json


T = TypeVar('T')


class Tree(object):
    class TRAVERSAL_TYPE(Enum):
        IN_ORDER = 1
        PRE_ORDER = 2
        POST_ORDER = 3

    def __init__(self, value:T):
        self.value = value
        self.left = None
        self.right = None

    @classmethod
    def deserialize(cls, data:str) -> 'Tree':
        head = None
        tree_noes = json.loads(data)
        head = Tree.generate(tree_noes, type=Tree.TRAVERSAL_TYPE.PRE_ORDER)
        return head

    @classmethod
    def serialize(cls, tree:'Tree') -> str:
        tree_noes = [v for v in tree.dfs(Tree.TRAVERSAL_TYPE.PRE_ORDER)]     # a list hold the tree values
        return json.dumps(tree_noes)

    @classmethod
    def generate(cls, data:list[T], type:'Tree.TRAVERSAL_TYPE'='Tree.TRAVERSAL_TYPE.PRE_ORDER') -> 'Tree':
        if not data:
            return None
        head = Tree(data.pop(0))
        head.create_from_data(data)
        return head
        
    def create_from_data(self, data:list[T], type:'Tree.TRAVERSAL_TYPE'='Tree.TRAVERSAL_TYPE.PRE_ORDER') -> 'Tree':
        if not data:
            return
        # assert len(data) > 1, 'Error: size of 0 < data < 1, which is incorrect'
        value = data.pop(0)
        self.left = Tree(value) if value!=None else None
        # print(f'create: left {self.left.value if self.left else None}')
        if self.left:
            self.left.create_from_data(data, type)
        if not data:
            self.right = None
            return
        value = data.pop(0)
        self.right = Tree(value) if value!=None else None
        # print(f'create: right {self.right.value if self.right else None}')
        if self.right:
            self.right.create_from_data(data, type)


    def dfs(self, type:'Tree.TRAVERSAL_TYPE'='Tree.TRAVERSAL_TYPE.PRE_ORDER') -> None:
        if type == Tree.TRAVERSAL_TYPE.IN_ORDER:
            for value in self.dfs_inorder(tye):
                yield value
        elif type == Tree.TRAVERSAL_TYPE.PRE_ORDER:
            for value in self.dfs_preorder():
                yield value
        elif type == Tree.TRAVERSAL_TYPE.POST_ORDER:
            for value in self.dfs_postorder():
                yield value

    def dfs_inorder(self) -> None:
        if self.left:
            for v in self.left.dfs_inorder():
                yield v
        else:
            yield None
        yield self.value
        if self.right:
            for v in self.right.dfs_inorder():
                yield v
        else:
            yield None

    def dfs_preorder(self) -> None:
        yield self.value
        if self.left:
            for v in self.left.dfs_preorder():
                yield v
        else:
            yield None
        if self.right:
            for v in self.right.dfs_preorder():
                yield v
        else:
            yield None

    def dfs_postorder(self) -> None:
        if self.left:
            for v in self.left.dfs_postorder():
                yield v
        else:
            yield None
        if self.right:
            for v in self.right.dfs_postorder():
                yield v
        else:
            yield None
        yield self.value

    def __str__(self) -> str:
        s = ''
        nodes = [(self, 0)]
        lvl = 0
        while nodes:
            cur_node, node_lvl = nodes.pop(0)
            if node_lvl > lvl:
                s += '\n'
                lvl = node_lvl
            s += f'{cur_node.value if cur_node else None}, '
            if cur_node:
                nodes.append((cur_node.left, node_lvl+1))
                nodes.append((cur_node.right, node_lvl+1))
        return s


def test():
    data_dfs = [6,4,3,None,None,10,7,None,None, None,1,None,5,None,2,None,None]

    t1 = Tree.generate(data_dfs, type=Tree.TRAVERSAL_TYPE.PRE_ORDER)
    print(f'generate \n{t1}')
    s_serialize = Tree.serialize(t1)
    print(f'serialize: {s_serialize}')

    t1_restore = Tree.deserialize(s_serialize)
    print(f'deserialize: {t1_restore}')




test()






