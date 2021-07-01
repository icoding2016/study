"""
Find the max of two numbers without using any of the comparison operators like if-else.

Rephrasing the question -- so that we don’t use conditional (if) statements

Idea:
   say a, b.    
   a-b is positive if a>b, else negative
   so (a-b)/abs(a-b) = 1   if a > b, 
                       -1  if a < b
   put a, b into a list [a,b] and turn 1, -1 into index 0, 1     
   then  index = int((1-(a-b)/abs(a-b))/2)


"""


def max_of(a, b):
    li = [a, b]
    idx = int((1 - (a-b)/abs(a-b))//2)
    return li[idx]


def test():
    print(max_of(1,2))
    print(max_of(2,1))

test()