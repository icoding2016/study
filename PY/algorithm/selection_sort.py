

# T(N*N)
# S(1)
def selection_sort(data:list)->list:
    if not data:
        return data
    for i in range(len(data)-1):
        mi = i
        for j in range(i+1, len(data)):
            if data[mi] > data[j]:
                mi = j
            j += 1
        if mi != i:
            data[i], data[mi] = data[mi], data[i]
    return data        


def test():
    d = [7,3,9,8,10,6,2,5,0,4,1]    
    print(selection_sort(d))


test()
