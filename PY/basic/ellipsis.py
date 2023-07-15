# Usage of Ellipsis (...)
# 
# 1. Type Hinting (allow Any)
# 2. Used as 'pass' statement inside functions
# 3. Used as a default argument value
# 4. Giving access to a specified range of elements, just omitting out the serial indices
# 5. Slicing higher-dimensional data structures. 
#  

# >>> type(Ellipsis)
# <class 'ellipsis'>
# >>> dir(Ellipsis)
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
# 


import typing as t


def foo(x: ...) -> None:
    # x can be 'Any' type
    ...     # pass

# similar to 
def foo2(x: t.Any) -> None:
    pass


def bar(x = ...):
    return x
print(bar)    # output: "<function bar at 0x00000220F71BCE50>"
print(bar())  # output: "Ellipsis"

foo(x='any type')


array = [[[1111,1112],[1121,1122]], [[1211,1212],[1221,1222]]]

#print(array[..., 0])
print(array[:,:,0])



