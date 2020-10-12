# Find the shortest distance among 2 given keys in a list.
#

L=[3, 165, 90, 1, 88, 72, 33, 49, 3, 88, 111, 90]
D=dict()

def solution(L, x, y):
    # build dict 
    for i in range(len(L)):
        k = L[i]
        if k in D:
            D[k].append(i)
        else:
            D[k] = [i]
    #for k,v in D.items():    print(k,v)

    getDistance(D, x, y)


def getDistance(d, a,b):
    if a not in d:
        return None
    if b not in d:
        return None
    
    gap = None
    for i in d[a]:
        for j in d[b]:
            g = abs(i-j)
            if not gap or g < gap:
                gap = g
    print('-'*80)
    print(gap)   


if __name__ == "__main__":
    solution(L, 3, 88)
    solution(L, 90, 88)

