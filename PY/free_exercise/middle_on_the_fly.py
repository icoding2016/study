# real time data is coming in, and stored. 
# when a function ‘middle’ is called the middle element is retruned. 
# Also use suitable data structure to store the data
#
# Solution
#   - real time data, so need dynamic data structure, e.g. StatisticTree, heap, link-list, etc
#   - middle(),  seems a balanced StatisticTree is more efficient
#                to speed up the 'middle' finding, record the StatisticTree size for each node.
#   - if middle is frequently called, then cache it, update the value at insert()
# 
#   define middle as   N//2
# #


class StatisticTree(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.size = 1

    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = StatisticTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = StatisticTree(value)
        self.size += 1

    def find_middle(self, left=0, right=0):
        if not any([self.left, self.right]):
            return self.value
        if self.left:
            left += self.left.size
        if self.right:
            right += self.right.size
        if left == right or left+1 == right:
            return self.value
        elif left < right:
            return self.right.find_middle(left=left+1, right=0)
        else:
            return self.left.find_middle(left=0, right=right+1)

class MiddleOnTheFly(object):

    def __init__(self):
        # solution 1
        self.data = None   #StatisticTree()
        self.cached_middle = None

    def middle(self):
        return self.cached_middle

    def data_income(self, value):
        if self.data:
            self.data.insert(value)
        else:
            self.data = StatisticTree(value)
        self.cached_middle = self.data.find_middle()



def test():
    M = MiddleOnTheFly()
    data = [i for i in range(1,21,2)] + [i for i in range(20,2,-2)]
    for i in data:
        M.data_income(i)
        print(M.middle(), ', ')


test()

