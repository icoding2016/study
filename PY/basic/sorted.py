# sorted(iterable, *, key=None, reverse=False)


L = ['b','d', 'c','a']
D = {L[i]:i for i in range(len(L))}
L2 = [(L[i],i) for i in range(len(L))]


S1 = sorted(D, key=lambda x:D[x])
print(S1)

S2 = sorted(D, key=lambda x:x)
print(S2)

S3 = sorted(L2, key=lambda x:x[0])
print(S3)






