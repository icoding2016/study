
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
sd_k = {n:D[n] for n in sorted(D}
sd_v = {n:D[n] for n in sorted(D,key=lambda x:D[x])}
print('sort by keys: ', sd_k)
print('sort by values: ', sd_v)
