class BTreeNode():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Class BTreeNode <{id(self)}>: ({self.key}, {self.value})"

data = eval("BTreeNode")(1,'a')
print(data)
