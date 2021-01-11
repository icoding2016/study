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
                    


def test():
    d = [3,5,1,7,6,2,4,8,9]
    b = BNode.generate(d)
    #b.inorder()
    b.inorder_imperative()



test()
