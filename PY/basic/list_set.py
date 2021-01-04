# list[start:stop:step]
# list support '+' but not support '-'
# set support '-', but not support '+'
# list() is not harshable, so we can add [] into a list  [].append([])
#                      but we cannot add [] into set,
# So the rule is, immutable object can be added to set/dict, but mutable cannot
#   -- set/dict can only add harshable object, 'immutable' objects are harshable, so can be added to set, dict.
# when comparing list with '==', order matters
# when comparing set with '==', order doesn't matters


# list1[start:stop] creates a new list
l=[1,2,3,4,5,6,7,8]
l1=l[:2]
l2=l[0:6:2]
print(id(l))
print(id(l1))
print(l2)

print([x for x in l if x not in l1])

print('list +/-')
l1=[1,2,3,4,5]
l2=[1,2,3,6,7]
print(l1+l2)
# print(l1-l2)   # error, list doesn't support minus

print('set +/-')
s1=set(l1)
s2=set(l2)
# print(s1+s2)    # error, set doesn't support addition
print(s1-s2)
print(s1.union(s2))  # although no '-' opr, set support union to return a 'superset', it doesn't change s1 or s2
print(set.union(s1,s2))   # union is a static function in set, 

#for i in range(len(s1)):    print(s1[i])          # error: 'set' object does not support indexing 

print('s1 pop:', s1.pop())
print(s1)
s1.add(1)
print(s1)

s2=s1.copy()          # yes
print(s2)
s2=s1.copy().add(6)   # no, that is None
print(s2)

print(s1.add(11))    # notice, s1.add() changed s1 but return nothing (None)
print(s1)

l1=[1,2,3]
l2=[3,2,1]
print(l1==l2)        # False -- for list, order matters
print(l1==sorted(l2)) # True -- after changing the order, it becomes equal
l3=l1.copy()
print(l1==l3)         # True -- the compare is based on value, not object instance
print(l1 is l3)       # False -- comparing object instance

s1={1,2,3}
s2={3,2,1}
s3={(0,1),(2,2),(3,7)}
s4={(3,7),(0,1),(2,2)}
print(s1==s2)        # True -- for set, order doesn't matter
print(s3==s4)        # True

s1.add(4)
print('set add:',s1)
# s1.add([4,5])      # error, unhashable type: 'list'
s1.remove(3)
print('set remove:',s1)

b1=[[]]*5            # Note: this is not the right way of initiallzation 
b1[0].append(1)
print(b1)
for i in range(len(b1)):
    print(id(b1[i]))

b2 = [[] for i in range(5)]
b2[0].append(2)
print(b2)
for b in b2:
    print(id(b))

lt = [(11,12,13),(21,22,23),(31,32,33)]
for a,b,c in lt:
    print(a,b,c)

ll = [[11,12,13],[21,22,23],[31,32,33]]
for a,b,c in ll:
    print(a,b,c)

ll = [[1,2]]
print([2,1] in ll)
print(sorted([2,1]) in ll)