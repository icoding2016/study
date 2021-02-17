# find the numbers where the digits of a number is odd from given 1000 to 3000 
# e.g 2000, 2246, 2804 




def odd_digit():
    available = [0,2,4,6,8]
    for h in available:
        for t in available:
            for o in available:
                digits = [2,h,t,o]
                yield ''.join([str(x) for x in digits])


def test():
    for x in odd_digit():
        print(x, end=',')
    print('')

test()
