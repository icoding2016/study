from collections import Counter
from collections import OrderedDict
from collections import deque
from collections import namedtuple
from collections import defaultdict

import collections
print(dir(collections))


nt = namedtuple('NewTuple', ('name', 'value'))
nt.name = 'a name'
nt.value = 100

C = Counter([1,2,3,2,1,0,4,3,3])
print(C)
print(isinstance(C, dict))       # True, Counter is a 'dict'
for x, c in C.items():
    print(x, c)



print('deque')
dq = deque()
for i in range(5,10):
    dq.append(i)
print(dq)
print('deque append, extend:', end='')
dq.append(11)
dq.extend([12,13,14])
print(dq)
dq.pop()
print('pop:', dq)
print('deque appendleft, extendleft:', end='')
dq.appendleft(4)
dq.extendleft([3,2,1])
print(dq)
print('deque popleft:', end='')
dq.popleft()
dq.popleft()
print(dq)
print('deque insert:', end='')
dq.insert(3, 100)
dq.insert(5, 101)
print(dq)
print('deque remove:', end='')
dq.remove(101)
print(dq)


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for c, i in s:
    d[c].append(i)
print(d)



