#

# T(N*N)  avarage
# S(1)
def bubble_sort(data:list) -> list:
    if not data:
        return data
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] > data[j]:
                data[i], data[j] =  data[j], data[i]
    return data



def test():
    d = [7,3,9,8,10,6,2,5,0,4,1]    
    print(bubble_sort(d))


test()
