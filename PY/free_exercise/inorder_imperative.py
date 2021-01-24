# print binary tree
# compare recursive and imperative


from collections import deque


class BNode(object):
    def __init__(self, val)->None:
        self.val = val
        self.left = None
        self.right = None
    
    def insert(self, val)->None:
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BNode(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BNode(val)
    
    @staticmethod
    def generate(data)->"BNode":
        head = None
        for x in data:
            if not head:
                head = BNode(x)
            else:
                head.insert(x)
        return head

    def inorder(self):
        self.inorder_imperative()
        #self.inorder_recursive()

    def inorder_recursive(self)->None:
        if self.left:
            self.left.inorder()
        print(self.val)
        if self.right:
            self.right.inorder()

    def inorder_imperative(self)->None:
        s = []  #stack
        n = self
        visited = {}
        while n:
            if n.left and n.left not in visited:
                s.append(n)
                n = n.left
                continue      
            else: 
                if n not in visited:
                    print(n.val)
                    visited[n] = True
                if n.right and n.right not in visited:
                    n = n.right
                    continue
            if s:
                n = s.pop()   
            else:
                break         
                    
    def level_walk(self, lvl)->None:
        print(self._level_walk(lvl))


    def _level_walk(self, lvl, output=None)->list:
        if None == output:
            output = []
        if lvl == 0:
            output.append(self.val)
            return output
        if lvl > 0:
            if self.left:
                self.left._level_walk(lvl-1, output)
            if self.right:
                self.right._level_walk(lvl-1, output)
        return output


def test():
    d = [3,5,1,7,6,2,4,8,9]
    b = BNode.generate(d)
    #b.inorder()
    b.inorder_imperative()
    print("lvl walk")
    b.level_walk(0)
    b.level_walk(1)
    b.level_walk(2)


test()
