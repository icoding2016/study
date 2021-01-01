# giving a list of sorted data, create a balance binary search tree

from collections import defaultdict


class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def walk_levels(self, level:int=0, output:dict=None) -> dict:
        if None == output:
            output = defaultdict(list)
        output[level].append(self.data)
        if self.left:
            self.left.walk_levels(level+1, output)
        if self.right:
            self.right.walk_levels(level+1, output)
        return output 

    def show(self):
        level_data = self.walk_levels()
        w = len(level_data[len(level_data)-1])
        for i in range(len(level_data)):
            print('{}-> {}'.format(i,' '*(int(w)-i)), end='')
            for n in level_data[i]:
                print(' {} '.format(n), end='')
            print('')


def create_balance_tree(data:list) -> TreeNode:
    if not data:
        return None
    if len(data) == 1:
        return TreeNode(data[0])
    mid = int((len(data)-1)/2)
    node = TreeNode(data[mid])
    node.left = create_balance_tree(data[0:mid])
    node.right = create_balance_tree(data[mid+1:])
    return node


def test():
    data = [x for x in range(11)]
    bt = create_balance_tree(data)
    bt.show()


test()

