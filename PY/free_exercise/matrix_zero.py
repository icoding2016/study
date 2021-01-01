# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, 
# its entire row and column are set to 0.
# 

class InvalidInputException(Exception):
    pass


class Matrix(object):
    def __init__(self, M, N, data):
        self.M = M
        self.N = N
        self.data = data

    def xy2offset(self, x, y):
        if x >= self.M or y >= self.N:
            raise InvalidInputException("Invalid input")
        return self.M * y + x

    def get_value(self, x, y):
        offset = self.xy2offset(x,y)
        return self.data[offset]

    def set_value(self, x, y, value):
        offset = self.xy2offset(x,y)
        self.data[offset] = value

    def set_cross_zero(self, x, y):
        '''Set the row/column to zero
        '''
        if x >= self.M or y >= self.N:
            raise InvalidInputException("Invalid input")
        for i in range(self.M):
            self.set_value(i, y, 0)
        for i in range(self.N):
            self.set_value(x, i, 0)

    # Time Complexity:    O(M*N)
    # Space Complexity:   O(M+N)
    def set_zero(self):
        '''If the element in the matrix is 0, set its row/column zero
        '''
        # Go through the matrix, record the row / columns that need to set zero
        m = []
        n = []
        for i in range(self.M):
            for j in range(self.N):
                if self.get_value(i,j) == 0:
                    m.append(i)
                    n.append(j)
        for i in m:
            for j in range(self.N):
                self.data[self.xy2offset(i,j)] = 0
        for j in n:
            for i in range(self.M):
                self.data[self.xy2offset(i,j)] = 0

    def show(self):
        for i in range(self.N):
            for j in range(self.M):
                print("{:<6}".format(self.get_value(i,j)), end='  ')
            print('')


A1 = [
    11,12,13,14,
    21,0,23,24,
    31,32,33,34,
    41,42,43,44,
]

def test():
    m = Matrix(4,4,A1)
    m.show();  print('-'*50)
    m.set_zero()
    m.show();  print('-'*50)


test()