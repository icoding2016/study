"""
380. Insert Delete GetRandom O(1)
Medium
https://leetcode.com/problems/insert-delete-getrandom-o1/description/


Implement the RandomizedSet class:
    RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.
 

Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.


Constraints:
    -231 <= val <= 231 - 1
    At most 2 * 105 calls will be made to insert, remove, and getRandom.
    There will be at least one element in the data structure when getRandom is called.


Solution idea:
  the key is O(1)
  add/del: easy to achieve O(1) with dict, but cannot get random in O(1)
  getRandom:  need to maintain a 'current' pointer, and loop around the data

  So: double linked list (achieve random) + dict (for O(1) get/del/get_random)


"""


class RandomizedSet:

    def __init__(self):
        self.index = dict()
        self.data = DLL()
        self.cur = None

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        node = DLLNode(val)
        self.index[val] = node
        self.data.insert(node)
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        node = self.index[val]
        self.data.remove(node)
        del self.index[val]
        return True        

    def getRandom(self) -> int:
        node = self.data.get_next()
        return node.val
        

class DLLNode():
    def __init__(self, val):
        self.val = val
        self.pre = self.nxt = None

class DLL():
    def __init__(self):
        self.head = None
        self.tail = None
        self.cur = None

    def insert(self, node:DLLNode):
        if not self.head:
            self.head = node
            self.tail = node
            self.cur = node
        else:
            node.pre = self.tail
            self.tail.nxt = node
            self.tail = node
        # print('insert: ', self)

    def remove(self, node:DLLNode):
        # print('remove: ', self)
        if self.head == node:
            self.head = node.nxt
        if self.tail == node:
            self.tail = self.tail.pre
        if node.pre:
            node.pre.nxt = node.nxt
        if self.cur == node:
            if node.nxt:
                self.cur = node.nxt
            else:
                self.cur = self.head
        del node
        # print(' ==> ', self)

    def get_next(self) -> DLLNode:
        # print('get_next: ', self)
        if not self.cur:
            self.cur = self.head
        node = self.cur
        if self.cur:
            if self.cur == self.tail:
                self.cur = self.head
            else:
                self.cur = self.cur.nxt
        return node

    def __repr__(self) -> str:
        node = self.head
        output = ''
        output += (f'head: {self.head}\n'
                   f'tail: {self.tail}\n'
                   f'cur: {self.cur}\n')
        while node:
            if output:
                output += ' -> '
            output += str(node.val)
            node = node.nxt
        return output


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
    

    

