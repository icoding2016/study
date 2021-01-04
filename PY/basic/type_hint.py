# Type Hints
#   Use Type annotation  
# https://www.python.org/dev/peps/pep-0484/
#

from typing import Iterable, Tuple
from typing import TypeVar
from typing import Callable
from typing import Sequence
from typing import Text
from typing import Generic
from typing import Union


def func1(s:str) -> None:
    print(s)

def func2(i:int) -> Union[int,bool]:
    return i if i > 0 else False

# Type Alias
# It is recommend capitalizing alias names, since they represent user-defined types, 
# which (like user-defined classes) are typically spelled that way.
Url = str
def func_aliase(url:Url) -> None:
    print(url)

Input = Union[list,dict]
def func(i:Input):
    print(i)
func([1,2,3])

# TypeVar
#   -- to re-define new types
T = TypeVar('T', int, float, complex)   # Type Variable
Vector = Iterable[Tuple[T,T]]           # Type Alias

def inproduct(v: Vector[T]) -> T:
    return sum(x*y for x,y in v)

def test_inproduct():
    print(inproduct([(1,2),(2,3)]))
    print(inproduct([(1.5,2),(2.0,3)]))


# Callable
# Frameworks expecting callback functions of specific signatures might be type hinted using 
# Callable[[Arg1Type, Arg2Type], ReturnType].
# It is possible to declare the return type of a callable without specifying the 
# call signature by substituting a literal ellipsis (three dots) for the list of arguments:
def func_callable(compare_func: Callable[[int, int], bool], a:int, b:int) -> None:
    result = compare_func(a,b)
    print('{} >= {}:{}'.format(a,b,result))

def is_greater_equal(a:int, b:int) -> bool:
    return a >= b

def func_callable_dot(a_func:Callable[..., bool]) -> Callable[..., bool]:
    print('A callable function:', a_func, end=' ')
    return a_func

def test_callable():
    func_callable(is_greater_equal, 3,1)
    func_callable(is_greater_equal, 0,1)
    f = func_callable_dot(is_greater_equal)
    print(f(1,2))


# Generics
# Generics can be parameterized by using a new factory available in typing called TypeVar
T = TypeVar('T')    # Declare type variable T
AnyStr = TypeVar('AnyStr', Text, bytes)
def func_generic(seq:Sequence[T], index:int) -> T:
    if index < len(seq):
        v = seq[index]
        return v
    return None

def func_generic_str(a:AnyStr, b:AnyStr) -> AnyStr:
    return a + b

class Tree(object):
    def __init__(self, data: T) -> None:
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data: T) -> None:
        if self.data < data:
            if self.right:
                self.right.insert(data)
            else:
                node = Tree(data)
                self.right = node
        else:
            if self.left:
                self.left.insert(data)
            else:
                node = Tree(data)
                self.left = node

       

    @staticmethod
    def generate(data:Sequence[T]) -> 'Tree':   #  use string literals, to delay evaluation of the type
        # generate a tree from the given data
        root = None
        for d in data:
            if not root:
                root = Tree(d)
            else:
                root.insert(d)
        return root


def func(d:dict[int,list[tuple]])->None:
    for k, v in d.items():
        print(k, v)

    
def test_generic():
    l = [(1,2),(3,4),(5,6)]
    print(func_generic(l, 1))
    print(func_generic({1:1,2:2,3:3}, 1))
    print(func_generic('abcde',1))
    print(func_generic_str(b'binary-stirng1.', b'binary-string2'))
    print(func_generic_str(u'unicode-stirng1.', u'unicode-string2'))
    root = Tree.generate([5,4,1,2,3,8,7,0,9,6])

    func({1:[(11,12),(21,22)]})
    


# User-defined generic types
# A generic type can have any number of type variables, and type variables may be constrained. This is valid:
# Each type variable argument to Generic must be distinct.
X = TypeVar('X')
Y = TypeVar('Y')
class Pair(Generic[X, Y]):          # class Pair(Generic[X,X])  #invalid
    pass 

def test():
    test_inproduct() 
    test_callable()
    test_generic()


test()    
