# all(iterable)     True if all of the elements in the iterable are True, otherwise False
#                   note: when the iterable is empty, return True 
# any(iterable)     True if any of the elements in the iterable is True, otherwise False
#                   note: when the iterable is empty, return False 



s1 = 'abc'
s2 = ''
l1 = [1,2]
l2 = []
b1 = True
b2 = False



print(all([1,'ab',[3,2],True]))
print(all([1,'ab',[],True]))
print(all([]))

print(any([0,'',[],False]))
print(any([1,'',[],False]))
print(any([]))




