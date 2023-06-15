"""
Array in python is a 'list'
"""



a = [i for i in range(10)]
print(a)

# reverse
ra = a.copy()
ra.reverse()
print(ra)

ra2 = a[::-1]
print(ra2)

# rotate
for i in range(len(a)):
    a = a[1:]
    a.append(a[0])
    print(a)