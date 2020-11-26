# sorted(iterable, *, key=None, reverse=False)


L = ['b','d', 'c','a']
D = {L[i]:i for i in range(len(L))}
L2 = [(L[i],i) for i in range(len(L))]


S1 = sorted(D, key=lambda x:D[x])
print(S1)
print(sorted([x for x in range(10)], reverse=True))   # reverse

S2 = sorted(D, key=lambda x:x)
print(S2)

S3 = sorted(L2, key=lambda x:x[0])
print(S3)
print(sorted(L2, key=lambda x:x[1]))


tl = [('a', 10), ('b',8), ('c',5)]
print(sorted(tl, key=lambda x:x[1]))         # key
print(sorted(tl, key=lambda x:x[0]))

# print(sorted(tl, cmp=lambda x,y:cmp(x[1],y[1])))    # in Python3, cmp is no longer suported
# ll = [[3,7,3],[2,4,6],[0,9,5],[7,2,1]]
# print(sorted(ll, cmp=lambda x,y:(x[-1]<y[-1])))







