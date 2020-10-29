# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
# 
# Say the Matrix element is m(i,j), the rotation means m(i,j) moves to m(width-j,i)
# The image data could be just an array:  A[i] i=1~ 4N*4N,  so X=(i/4)%4N, Y=int(i/4N)
#   the rotate means  (X,Y) --> (4N-Y, X) = (4N-int(X/4N),  i%4N)

N = 4

class InvalidInputException(Exception):
    pass

class InvalidOperation(Exception):
    pass

# Time Complexity:   O(N^2)     (N*N/2)
# Space Complexity:  O(1)
class Matrix(object):
    def __init__(self,width:int, hight:int,data:list):
        self.width = width
        self.hight = hight
        self.data = data

    def xy2offset(self, x, y):
        if x >= self.width or y >= self.hight:
            raise InvalidInputException
        return y*self.width+x

    def offset2xy(self, offset):
        if offset >= (self.width-1) * (self.hight-1):
            raise InvalidInputException
        x = offset % self.width
        y = int(offset / self.hight)
        return x,y

    def get_data(self, x, y):
        offset = self.xy2offset(x,y)
        return self.data[offset]

    def set_data(self, x, y, data):
        self.data[self.xy2offset(x,y)]=data
        
    def show(self):
        for y in range(self.hight):
            for x in range(self.width):
                print("{}".format(self.get_data(x,y)),end='  ')
            print('')

    def get_xy_rotate_clockwise(self, x, y):
        # validat x, y
        return self.hight - y - 1, x 

    def rotate_clockwise(self):
        for layer in range(int(self.width/2)):
            for i in range(layer, self.width-layer-1):
                p1 = (i, layer)
                data = self.get_data(i, layer)
                for round in range(4):
                    d1 = data
                    p2 = self.get_xy_rotate_clockwise(p1[0], p1[1])
                    d2 = self.get_data(p2[0], p2[1])
                    data = d2
                    self.set_data(p2[0], p2[1], d1)
                    p1 = p2
                #print('--');    self.show()




def test(w,h, A):
    #matrix_rotate(A)
    m = Matrix(w,h,A)
    m.show()
    m.rotate_clockwise()
    print('-'*60)
    m.show()



A1 = [
    11,12,13,14,
    21,22,23,24,
    31,32,33,34,
    41,42,43,44,
]


A2 = [
    [11,11,11,11], [12,12,12,12], [13,13,13,13], [14,14,14,14],
    [21,21,21,21], [22,22,22,22], [23,23,23,23], [24,24,24,24],
    [31,31,31,31], [32,32,32,32], [33,33,33,33], [34,34,34,34],
    [41,41,41,41], [42,42,42,42], [43,43,43,43], [44,44,44,44],
]

test(4,4,A1)
test(4,4,A2)