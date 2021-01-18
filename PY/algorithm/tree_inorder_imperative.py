# Imperative implememntation of binary tree inorder



class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = TreeNode(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = TreeNode(val)

    @staticmethod
    def generate(d:list)->"TreeNode":
        head = None
        for x in d:
            node = TreeNode(x)
            if not head:
                head = node
            else:
                head.insert(x)
        return head

    def show(self):
        for x in self.inorder_imperative():
            print(x, end=" ")
        print("")

    def inorder_imperative(self):
        node = self
        S = []
        visited = {}  # node:True

        while node:
            while node not in visited and node.left:
                S.append(node)
                visited[node] = True
                node = node.left
            #print(node.val)
            yield node.val
            if node.right:
                node = node.right
                continue
            # no left or right
            if S:
                node = S.pop()
            else:
                node = None


def test():
    t = TreeNode.generate([7,4,8,2,1,9,5,0,3,6])
    t.show()

test()




