# Bi-directional Tree (A tree with parent pointer)

from typing import TypeVar

T = TypeVar('T')

class BDTree(object):
    def __init__(self, data:T, parent:'BDTree' = None) -> None:
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def insert(self, data:T) -> None:
        if data < self.data:
            if not self.left:
                node = BDTree(data)
                self.left = node
                node.parent = self
            else:
                self.left.insert(data)

        else:
            if not self.right:
                node = BDTree(data)
                self.right = node
                node.parent = self
            else:
                self.right.insert(data)

    def __str__(self) -> str:
        s = '[\n'
        level_data = BDTree.get_level_data(self)
        for lvl in level_data:
            s = s + '['
            for d in lvl:
                s = s + '{},'.format(d)
            s = s + ']\n'
        return s + ']\n'

    def get_node(self, data:T) -> 'BDTree':
        if data == self.data:
            return self
        if data < self.data:
            if self.left:
                return self.left.get_node(data)
            return None
        else:
            if self.right:
                return self.right.get_node(data)
            return None

    @staticmethod
    def generate(datalist:list[T]) -> 'BDTree':
        node = None
        for x in datalist:
            if not node:
                node = BDTree(x)
            else:
                node.insert(x)
        return node

    @staticmethod
    def get_level_data(root:'BDTree', level:int = 0, output:list[list[T]] = []):
        if not root:
            return output
        if level >= len(output):
            output.append([])
        output[level].append(root.data)
        if root.left:
            BDTree.get_level_data(root.left, level + 1, output)
        if root.right:
            BDTree.get_level_data(root.right, level + 1, output)
        return output