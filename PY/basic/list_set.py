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

l1=[1,2,3,4,5]
l2=[1,2,3]
print(l1+l2)
# print(l1-l2)   # error, list doesn't support minus

s1=set(l1)
s2=set(l2)
# print(s1+s2)    # error, set doesn't support addition
print(s1-s2)

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

s1={1,2,3}
s2={3,2,1}
s3={(0,1),(2,2),(3,7)}
s4={(3,7),(0,1),(2,2)}
print(s1==s2)        # True -- for set, order doesn't matter
print(s3==s4)        # True

s1.add(4)
# s1.add([4,5])      # error, unhashable type: 'list'

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

