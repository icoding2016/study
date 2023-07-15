from time import sleep

class MyIter():
    def __init__(self, data:list):
        self.data = data

    def add(self, data:list):
        self.data += data

    def __iter__(self):
        self._iter_idx = 0
        return self

    def __next__(self):
        if self._iter_idx >= len(self.data):
            raise StopIteration()
        value = self.data[self._iter_idx]
        self._iter_idx += 1
        return value
    
    def __contains__(self, key) -> bool:
        return key in self.data

mc = MyIter([1,2,3])
mc.add([4,5,6])
print(mc)
for d in mc:
    print(d)

print(3 in mc)
print(10 in mc)

for d in mc:
    print(d)