# Design a tree which can contain any number of children. 
# Implement create(parentid, childid) and find(nodeid). 
# Constraints: No duplicate key, tree depth cannot exceed certain threshold d
#
# 
#    Node
#     | id
#     | children={nodeid:Node,}
#
#  How to distribute & locate a node?  -- ID
#  e.g. ID: str   len<d
#  so create a hash(id) for scatter the children nodes.   key=hash(id)  children[key]  or 
# 
#   


class MyNode(object):
    def __init__(self, data:int):
        pass

    def add(self, data:int)
        key1 = hash_lvl1(data)
        if key1 in self.children:
            self.children[key1].add(data)
        else:
            self.children[key1] = 
