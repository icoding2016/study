'''
StoneWall
Cover "Manhattan skyline" using the minimum number of rectangles.


You are going to build a stone wall. 
The wall should be straight and N meters long, and its thickness should be constant; 
however, it should have different heights in different places. 
The height of the wall is specified by an array H of N positive integers. 
H[I] is the height of the wall from I to I+1 meters to the right of its left end. 
In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.

The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). 
Your task is to compute the minimum number of blocks needed to build the wall.

Write a function:

def solution(H)

that, given an array H of N positive integers specifying the height of the wall, 
returns the minimum number of blocks needed to build it.

For example, given array H containing N = 9 integers:

  H[0] = 8    H[1] = 8    H[2] = 5
  H[3] = 7    H[4] = 9    H[5] = 8
  H[6] = 7    H[7] = 4    H[8] = 8
the function should return 7. The figure shows one possible arrangement of seven blocks.



Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array H is an integer within the range [1..1,000,000,000].
'''

'''
NOTE:

  Thought:
    - Hight Rise: to open a new block           (stack)
    - High Fall: to close a/some opened blocks in stack (which was opened in bigger hight)


'''


from utils import Debug


# time complexity: 
def S(H):
    N = len(H)
    
    if N == 1:
        return 1

    count = 0
    stack = []
    for i in range(N):
        if not stack:
            stack.append(H[i])
            count += 1     # new block
        else:
            if H[i] > H[i-1]:
                stack.append(H[i])
                count += 1
            elif H[i] == H[i-1]:   # current block
                continue
            else:   # H[i] < H[i-1]  # close
                while True:
                    if not stack:           # <----- take care of the logic here
                        stack.append(H[i])  # no stack or closed all open block in stack, still need to open current (low block)
                        count += 1
                        break
                    if stack[-1] > H[i]:   #close
                        stack.pop()
                        continue
                    elif stack[-1] == H[i]:  # continue stacked block
                        break
                    else:  # open new
                        stack.append(H[i])
                        count += 1
                        break
    return count
    



def solution(A):
    return S(A)

if __name__ == "__main__":

    sample = [ 
        [8,8,5,7,9,8,7,4,8],        # 7
        [1],                        # 1
        [1,2,3,4,5],                # 5
        [5,4,3,2,1],                # 5
        [2,1,2],                    # 3
        [1,2,1],                    # 2
        [1,3,4,2,3,4,2,5,1],        # 7
    ]

    for A in sample:
        print('-'*60)
        r = solution(A)
        print("{} -> {}".format(A, r))

