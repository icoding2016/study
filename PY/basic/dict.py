"""
dict()  
support subscription [],  pop(),   &, | operations.

"""

from collections import Counter

d = {1:1, 2:2}

d[3]= 3
print(d)

del d[2]        # remove element from dict()
print(d)


print(d.pop(3)) # pop element from dict()
print(d)

# max(dict..)
d = {'a':3, 'b':2, 'c':1}
m = max(d, key=lambda x:d[x])       # max(dict_obj, key=...)
print(m)    # a
m = max([d[x] for x in d])
print(m)    # 3


# sort dict
D = {1:2, 4:2, 2:1, 3:1}
sd_k = {n:D[n] for n in sorted(D)}
sd_v = {n:D[n] for n in sorted(D,key=lambda x:D[x])}
print('sort by keys: ', sd_k)
print('sort by values: ', sd_v)



l1 = [1,1, 2,3,4,4,4,5]
l2 = [1,3,4,4,6,7]

c1 = Counter(l1)
c2 = Counter(l2)
print(c1&c2)
print(c1|c2)


def common(l1:list,l2:list):
    count = Counter(l1)
    count1 = Counter(l2)
    common = 0
    for c in count:
        if c in count1:
            common += count1[c]
    return common

def common2(l1:list,l2:list):
    c=Counter(l1) & Counter(l2)
    return sum([v for v in c.values()])

def testCommon(l1,l2):
    c1 = common(l1,l2)
    c2 = common2(l1,l2)
    print(c1)
    print(c2)
    return c1==c2

print(testCommon(l1,l2))
