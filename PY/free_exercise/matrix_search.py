# Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in ascending order, 
# write a method to find an element.(Cracking the Coding Interview 10.9)
#
#  


# Search by row
# T(M+N)
def matrix_search(matrix:list[list], num:int) -> (int,int):
    if not len(matrix):
        return None
    M = len(matrix)
    N = len(matrix[0])
    y = M - 1
    for i in range(M):
        if matrix[i][0] > num:
            if i == 0:
                return None
            y = i-1
            break
    for x in range(N):
        if matrix[y][x] == num:
            return (x,y)
    return None

# binary search..    awkward implementation
# T(logN+logM)
#
def matrix_search2(matrix:list[list], num:int) -> (int,int):
    if not len(matrix):
        return None
    M = len(matrix)
    N = len(matrix[0])
    y = M - 1
    start = 0; end=M-1
    while end > start:
        cur = start + int((end-start)/2)
        if num < matrix[cur][0]:
            end = int(cur)
        elif num > matrix[cur][0]:
            if int(cur+1) < M and num < matrix[cur+1][0]:
                y = cur
                break
            else:
                if start ==  cur:
                    break
                start = cur
        else:  # == 
            return (0, cur)
    
    start = 0
    end = N
    while end > start:
        cur = start + int((end-start)/2)
        if num == matrix[y][cur]:
            return (cur, y)
        elif num < matrix[y][cur]:
            end = cur
        else:
            if start == cur:
                if num == matrix[y][end]:
                    return (end, y)
                else:
                    return None
            start = cur
    return None

# binary search
# T(logN + logM)
def matrix_search3(matrix:list[list], num:int) -> (int,int):
    if not len(matrix):
        return None
    M = len(matrix)
    N = len(matrix[0])

    start = 0; end = M-1
    y = M - 1
    while end >= start:
        cur = (start + end)//2
        if num == matrix[cur][0]:
            return (0, cur)
        elif num < matrix[cur][0]:
            end = cur - 1
        else:
            if cur + 1 < M and num < matrix[cur+1][0]:
                y = cur
                break
            start = cur + 1
    start = 0; end = N-1
    while start <= end:
        cur = (start+end)//2
        if num == matrix[y][cur]:
            return (cur, y)
        elif num < matrix[y][cur]:
            end = cur - 1
        else:
            start = cur + 1
    return None

def test():
    matrix = [
        [10, 12, 13, 14, 15],
        [20, 23, 25, 27, 29],
        [30, 31, 33, 36, 38],
        [40, 44, 45, 47, 49],
    ]

    func = matrix_search3

    n = 31
    print('{} is at {}'.format(n, func(matrix, n)))
    n = 49
    print('{} is at {}'.format(n, func(matrix, n)))
    n = 10
    print('{} is at {}'.format(n, func(matrix, n)))
    n = 30
    print('{} is at {}'.format(n, func(matrix, n)))
    n = 29
    print('{} is at {}'.format(n, func(matrix, n)))
    n = 32
    print('{} is at {}'.format(n, func(matrix, n)))
    n = 5
    print('{} is at {}'.format(n, func(matrix, n)))


test()