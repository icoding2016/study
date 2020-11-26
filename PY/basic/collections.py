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



q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.pop()
print(q)
q.pop()
print(q)


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for c, i in s:
    d[c].append(i)
print(d)
