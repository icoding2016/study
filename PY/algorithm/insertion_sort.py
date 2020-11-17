#Insertion sort
# 
# Time: O(N^2)
#   loop N, for each data[i], loop i, so total  1+2+...+(N-1) = N(N-1)/2 => O(N*N)
def insertion_sort(data:list) -> list:
    if len(data) <= 1:
        return data
    
    for i in range(1, len(data)):
        if data[i] >= data[i-1]:
            continue
        cur = data[i]
        j = i-1
        while data[j] > cur and j >=0:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = cur           
    return data


def test():
    data = [3,7,5,2,4,9,0,1,6,8]
    print(insertion_sort(data))

test()