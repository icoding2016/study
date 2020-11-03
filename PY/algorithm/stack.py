# 
# Questions:
# 3.1 Three in One: Describe how you could use a single array to implement three stacks.
# Hints:
#   
# 3.2 Stack Min: How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.
# Hints:  
#   The challenge is how to update mini at pop()
#   Have to keep another stack for mini value. when pop(), check if the popped value is the stack_mini top.
#   Also need a counter for each value in stack_mini in case there are duplicate values
#    
#
# 3.3 Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.
# 
# 
# 3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
# Hints:
#   1 stack for push(), 1 for pop()..    
#   when pop, pore the data in stack 1 to stack 2 (revered) then pop the top one
#   when push, pore the data back to stack1 if they are in stack 2, then push
# 
# 3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
# Hints:
#   Use stack2 as the 'sorted stack'&buffer, and a temporary variable to hold current max value.
# 
# 3.6 Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
# out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
# that type). They cannot select which specific animal they would like. Create the data structures to
# maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
# and dequeueCat. You may use the built-in Linked list data structure.


from typing import Text
from typing import TypeVar
from typing import Type

T = TypeVar('T')

class InvalidInputException(Exception):
    pass


class ThreeInOne(object):
    def __init__(self) -> None:
        self.valid_stackid = [1,2,3]
        self.array = []  #[None, None, None]
        self.array_size = 0
        self.stack_top = {1:-3, 2:-2, 3:-1}
        self.stack_bottom = {1:-3, 2:-2, 3:-1}
        self.mini = None
        
    def extend_array(self) -> None:
        self.array.extend([None]*3)
        self.array_size += 3

    def push(self, stack_id:int, data:T) -> None:
        if stack_id not in self.valid_stackid:
            raise InvalidInputException('Invalid stack id')
        if self.array_size - 1 < self.stack_top[stack_id] + 3:
            self.extend_array()
        self.stack_top[stack_id] += 3
        self.array[self.stack_top[stack_id]] = data
        print('stack {} push {} at {}'.format(stack_id, data, self.stack_top[stack_id]))

        if not self.mini:
            self.mini = data
        else:
            self.mini = data if data < self.mini else self.mini

    def pop(self, stack_id:int) -> T:
        if stack_id not in self.valid_stackid:
            raise InvalidInputException('Invalid stack id')
        if self.stack_top[stack_id] - 3 < self.stack_bottom[stack_id]:
            print('stack {} already empty'.format(stack_id))
            return None
        self.stack_top[stack_id] -= 3
        data = self.array[self.stack_top[stack_id]]
        print('stack {} pop {} at {}'.format(stack_id, data, self.stack_top[stack_id]))
        return data

    def show(self, stack_id:int = None) -> None:
        if not stack_id:
            ids = self.valid_stackid.copy()
        elif stack_id in self.valid_stackid:
            ids = [stack_id, ]
        else:
            raise InvalidInputException('Invalid stack id')

        print('Stack(s) top -> bottom')
        for id in ids:
            top = self.stack_top[id]
            bottom = self.stack_bottom[id]
            print('stack {}: ['.format(id), end='')
            while top >= bottom:  
                print(self.array[top], end=',')
                top -= 3
            print(']')
        

class Stack(object):
    _EXTEND_SIZE = 5

    def __init__(self) -> None:
        self.stack = []
        self.size = 0
        self.top =  -1
        self.bottom = -1
        # for mini
        self.minis = []   # [[value, count], ...]

    def _extend_stack(self):
        self.stack.extend([None] * Stack._EXTEND_SIZE)
        self.size += Stack._EXTEND_SIZE

    def push(self, data:T) -> None:
        if self.size - 1 < self.top + 1:
            self._extend_stack()
        self.top += 1
        self.stack[self.top] = data

        # for mini feature:
        if not self.cur_mini():
            self.add_mini(data)
        elif data <= self.cur_mini():
            self.add_mini(data)

    def pop(self) -> T:
        if self.top <= self.bottom:  # bottom
            return None
        data = self.stack[self.top]
        self.top -= 1

        # for mini feature
        if data == self.cur_mini():
            self.remove_mini()

        return data

    def peek(self) -> T:
        if self.is_empty():
            return None
        else:
            return self.stack[self.top]

    def is_empty(self) -> T:
        if self.top <= self.bottom:
            return True
        return False


    def __str__(self) -> Text:
        s = '{} ['.format(type(self))
        for i in range(self.bottom + 1, self.top + 1):
            s = s + '{}'.format(self.stack[i])
            if i < self.top:
                s = s + ', '
        s = s + ']'
        return s


    def show(self) -> None:
        print('Bottom --> Top')
        print('[', end='')
        for i in range(self.bottom + 1, self.top + 1):
            print(self.stack[i], end='')
            if i < self.top:
                print(', ',end='')
        print(']')


    def cur_mini(self) -> T:
        if self.minis:
            return self.minis[len(self.minis)-1][0]
        else:
            return None

    def add_mini(self, data:T) -> None:
        if not self.minis:
            self.minis.append([data, 1])    
            return
        if self.minis[len(self.minis)-1][0] == data:
            self.minis[len(self.minis)-1][1] += 1
        elif self.minis[len(self.minis)-1][0] > data:
            self.minis.append([data, 1])
        else:  # smallger than cur mini, shouldn't add, skip
            return

    def remove_mini(self) -> T:
        if not self.minis:
            return None
        data = self.minis[len(self.minis)-1][0]
        if self.minis[len(self.minis)-1][1] > 1:
            self.minis[len(self.minis)-1][1] -= 1
        else:
            self.minis.pop()
        return data

    # Time Complexity:     O(N^2)  N+(N-1)+(N-2)..+1=O(N^2)
    # Space Complexity:    O(N)
    @staticmethod
    def sort(stack:'Stack', stack2:'Stack' = None) -> None:
        if not stack2:
            stack2 = Stack()
        
        if stack.is_empty():
            while not stack2.is_empty():
                stack.push(stack2.pop())
            return
            
        # get smallest in current stack and push to stack2
        small = None
        count = 0
        while not stack.is_empty():
            if not small:
                small = stack.pop()
            elif stack.peek() >= small:  # buff it
                stack2.push(stack.pop())
                count += 1
            else:
                stack2.push(small)
                small = stack.pop()
                count += 1
        for i in range(count):
            stack.push(stack2.pop())
        stack2.push(small)
        #print(stack, ' | ', stack2)

        Stack.sort(stack, stack2)        


class SetOfStacks(object):
    STACK_CAPACITY = 5
    def __init__(self):
        self.stacks = [[], ]
        self.top = [-1]     # index = stack#
        self.bottom = [-1]
        self.cur_stack = 0

    def push(self, data:T) -> None:
        if len(self.stacks[self.cur_stack]) >= SetOfStacks.STACK_CAPACITY:    # allocated new stack
            self.stacks.append([])
            self.top.append(-1)
            self.bottom.append(-1)
            self.cur_stack += 1
            #print('new stack')
        self.stacks[self.cur_stack].append(data)
        self.top[self.cur_stack] += 1
        #print(self.cur_stack, self.stacks)

    # todo ...


    def __str__(self) -> None:
        s = "[\n"
        for stack in self.stacks:
            s = s + '['
            for x in stack:
                s = s + '{}  '.format(x)
            s += ']\n'
        s = s + "]\n"
        return s


class QueueViaStack(object):
    pass    



def test():
    # ThreeInOne
    S = ThreeInOne()
    d1 = [11,12,13,14,15]
    d2 = [21,22]
    d3 = [31,32,33,34,35,36]
    for x in d1:
        S.push(1, x)
    for x in d2:
        S.push(2, x)
    for x in d3:
        S.push(3, x)

    S.show()
    S.pop(1)
    S.pop(2); S.pop(2); S.pop(2)
    S.pop(3)
    S.show()

    # Stack
    S = Stack()
    d = [1,2,3,4,5]
    for x in d:
        S.push(x)
    S.show()

    # mini
    S = Stack()
    d = [11,5,2,3,2,4,1,5,7]
    for x in d:
        S.push(x)
        print(S, '  cur mini:', S.cur_mini())
    data = S.pop()
    while data:
        print('pop {},  cur mini:{}'.format(data, S.cur_mini()))
        data = S.pop()

    # SetOfStacks
    print('SetOfStacks')
    S = SetOfStacks()
    d = [i for i in range(22)]
    for x in d:
        S.push(x)
    print(S)

    # sort_stack
    print('Stack Sort')
    S = Stack()
    for x in [6,10,5,3,2,4,8,1,5,9,7]:
        S.push(x)
    print(S)
    Stack.sort(S)
    print(S)


test()            
