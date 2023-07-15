"""
What types of object can be used as dict key?
  - The atomic immutable types are all hashable
  - A frozen set is always hashable(its elements must be hashable by definition)
  - A tuple is hashable only if all its elements are hashable
  - User-defined types are hashable by default because their hash value is their id()

hashable:
  num (int/float/..), bool, str, bytes, frozenset, tuple (with immutable objects), customized class instance

not-hashable:
  set, tuple (with mutable objects), list, dict


"""


s = set([1,2,3])
fs = frozenset([1,2,3])
ti = (1, 2, 'immutable_obj')
tm = ([1,2], {1:1, 2:2})
li = [1,2,3]
lm = [[1,2,], [4,5],]
class C(object): pass
c = C()

d = {
    # s:"set",                      # unhashable type: 'set'
    fs:"frozonset",
    ti:"tuple of immutable object",
    # tm:"tuple of mutable object",   # unhashable type: 'list'
    # li:"list of immutable object", # unhashable type: 'list'
    # lm:"list of mutable object",   # unhashable type: 'list'
    c: "class instance"
}

print(d)






