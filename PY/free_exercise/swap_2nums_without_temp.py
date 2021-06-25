"""
Swapping the numbers without using a temp variable.
In python we can simply do    x,y=y,x
But what if the language does not support this operation?
Find a method to swap the 2 numbers without using x,y=y,x

Idea:
  x, y   (gap y-x)
  so if x = y-x then  y-x= original x,   => x=y-x; y=y-x   (that set y to original x)
  now x=(orignal y-x), and y=(original x)  => x=y+x


"""



def swap(x, y):
    print(f'swap {x}, {y} => ', end=' ')
    x = y - x
    y = y - x
    x = y + x
    print(f'{x}, {y}')


def test():
    swap(1,2)    


test()    