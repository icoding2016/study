# Combine two sets of sorted ranges into a unique set of non-overlapping ranges, returning an array of duplicates.
# e.g.
# l1=[1,3,5,5,8,10]
# l2=[2,3,3,6,9,10]
# >> [1, 2, 3, 5, 6, 8, 9, 10], [3, 5]


def combine(l1:list, l2:list)->(list, list):
    # s1 = set(l1)
    # s2 = set(l2)
    s1 = s2 = None
    if l1[0] < l2[0]:
        s1,s2 = l1,l2
    else:
        s1,s2 = l2,l1
    c = []
    d = []
    i=j=0
    x = None
    while i<len(s1) or j<len(s2):
        if i>=len(s1):
            x = s2[j]
            j += 1
        elif j>=len(s2):
            x = s1[i]
            i += 1
        else:
            if s1[i]<s2[j]:
                x = s1[i]
                i += 1
            elif s1[i]>s2[j]:
                x = s2[j]
                j += 1
            else:
                x = s1[i]
                i += 1
                j += 1
                
        if x in c: 
            if x not in d:
                d.append(x)
        else:
            c.append(x)
    return c, d


def test():
    l1=[1,3,5,5,8,10]
    l2=[2,3,3,6,9,10]
    print(combine(l1,l2))


test()