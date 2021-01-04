# x << y
# Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
# x >> y
# Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
# x & y
# Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
# x | y
# Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
# ~ x
# Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
# x ^ y
# Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.
#
#
# Questions:
# Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and j. 
#   Write a method to insert M into N such that M starts at bit j and ends at bit i. You
#   can assume that the bits j through i have enough space to fit all of M. That is, if
#   M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
# example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
# EXAMPLE
#   Input: N 10000000000, M
#   Output: N = 10001001100
# Hints: 
# 
#5.2 Binary to String: Given a real number between O and 1 (e.g., 0.72) that is passed in as a double, print
# the binary representation. If the number cannot be represented accurately in binary with at most 32
# characters, print "ERROR:'
# Hints: 
#  
# 5.3 Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
# find the length of the longest sequence of ls you could create.
# EXAMPLE
#   Input: 1775
#   Output: 8 (or: 11011101111)
# Hints: 
#   Method1: (Brutal Force)
#     Go through the bits and record the continuous block 000, or 111   [(value,count),..]
#     ContinuousBlock Patterns:  11 represent 11...1,  00 represent 00...0
#         11, 00, 1100, 0011, 001100 (skip the 1st 0, then same as 11011 or 110011), 11011, 110011
#     for > 2 patterns, find max (either longest 11 for 110011 pattern or longest 11+11 for 11011 pattern)
#  
# 5.4 Next Number: Given a positive integer, print the next smallest and the next largest number that
# have the same number of 1 bits in their binary representation.
# Hints:
#  
# 5.5 Debugger: Explain what the following code does: ( ( n & ( n-1)) == 0).
# Hints:
# 
# 
# 5.6 Conversion: Write a function to determine the number of bits you would need to flip to convert
# integer A to integer B.
# EXAMPLE
# Input: 29 (or: 11101), 15 (or: 01111)
# Output: 2
# Hints: 
#


from ctypes import c_uint8, c_uint32, c_uint64, c_int32, c_double 

class InvalidInputException(Exception):
    pass


def get_bit(num:int, bit:c_uint8) -> int:
    if bit < 1:
        raise InvalidInputException("bit should >= 1")
    return 1 if num & (1<<bit-1) else 0

def set_bit(num:int, bit:c_uint8) -> int:
    if bit < 1:
        raise InvalidInputException("bit should >= 1")
    return num | (1<<bit-1)

def clear_bit(num:int, bit:c_uint8) -> int:
    if bit < 1:
        raise InvalidInputException("bit should >= 1")
    return num & ~(1<<bit-1)

def update_bit(num:int, bit:c_uint8, value:c_uint8) -> int:
    if bit < 1:
        raise InvalidInputException("bit should >= 1")
    if value not in [0,1]:
        raise InvalidInputException("value should be 0 or 1")
    if value:
        return set_bit(num, bit)
    else:
        return clear_bit(num, bit) 


def insertion(N:c_uint32, M:c_uint32, i:c_uint8, j:c_uint8) -> c_uint32:
    if i > j or i > 32 or i < 1 or j > 32 or j < 1:
        raise InvalidInputException('Invalid input')
    for bit in range(1, j-i+2):
        b = get_bit(M, bit)
        N = update_bit(N, i+bit-1, b)
    return N

def test_insertion(N:c_uint32, M:c_uint32, i:c_uint8, j:c_uint8) -> None:
    result = insertion(N,M,i,j)
    print("insert {:b} into {:b} at {}-{} =>{:b}".format(M,N,i,j, result))


# double has 64 bits, in Python that is 'float'
# 1 msb - sign, 11
def binary2str(num:float) -> str:
    # skip
    return ''


# Time Complexity:  O(b)  where b is the count of bit
# Space Complexity: O(b)  where b is the count of bit
def flip_bit_2_win(num:int) -> int:
    INT_SIZE = 64    # assume the int size is 64b
    class ContBlock(object):
        def __init__(self, value:int) -> None:
            if value not in [0,1]:
                raise InvalidInputException()
            self.value = value
            self.count = 1

        def add(self) -> int:
            self.count += 1
            return self.count
           
        def copy(self) -> 'ContBlock':
            cb = ContBlock(self.value)
            cb.count = self.count
            return cb

    cbs = []   # continuous blocks
    cb = None  # current cb
    for i in range(INT_SIZE):
        b = (num & (1 << i)) >> i
        if not cb:
            cb = ContBlock(b)
            continue
        if cb.value == b:
            cb.add()
        else:   # value changed
            cbs.append(cb)
            cb = ContBlock(b)
        if i >= INT_SIZE - 1:  # last bit
            cbs.append(cb)
    
    print('[',end='');  
    for x in cbs:  print("{}:{}, ".format(x.value, x.count),end=''); 
    print(']')

    if len(cbs) == 1:
        if cbs[0].value:
            return INT_SIZE
        else:
            return 1
    if len(cbs) == 2:
        c = cbs[0].count if cbs[0].value else cbs[1].count
        return c+1

    longest = 0
    pre_ones = None  # count of last '1' block
    for x in cbs:
        if x.value == 0 and not pre_ones:  # skip the 1st '0' block
            continue
        if x.value == 0: 
            if x.count == 1:   # possible merge
                continue
            else:  # 0 block len > 1, no merging
                pre_ones = None
        else:  # x.value == 1
            if not pre_ones:   
                if x.count > longest:
                    longest = x.count
                pre_ones = x.count
            else:
                mc = x.count + pre_ones
                if mc > longest:
                    longest = mc
                pre_ones = x.count
    return longest + 1




def test():
    print(get_bit(3, 1))
    print(get_bit(3, 2))
    print(get_bit(3, 4))

    print(set_bit(0, 1))
    print(set_bit(0, 2))
    print(set_bit(0, 3))

    print('{:b}'.format(clear_bit(7,1)))
    print('{:b}'.format(clear_bit(7,2)))
    print('{:b}'.format(clear_bit(7,3)))

    # insertion
    print('Insertion')
    test_insertion(0b10000000000, 0b10011, 2,6)

    # flip_bit_2_win
    print("flip_bit_2_win")
    num = 0
    print("{:b}-> {}".format(num, flip_bit_2_win(num)))
    num = -1
    print("{:b}-> {}".format(num, flip_bit_2_win(num)))
    num = 0b11111
    print("{:b}-> {}".format(num, flip_bit_2_win(num)))
    num = ~0b1111111
    print("{:b}-> {}".format(num, flip_bit_2_win(num)))
    num = 0b11011101111
    print("{:b}-> {}".format(num, flip_bit_2_win(num)))
    num = 0b110111001111
    print("{:b}-> {}".format(num, flip_bit_2_win(num)))
    num = (~0b11111111011001111)
    print("{:b}-> {}".format(num, flip_bit_2_win(num)))

test()    