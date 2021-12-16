"""
Count the number of digit 1 in a given long int

The question is a bit ambiguous, not specifying the input, 
e.g. int or str?
     binary or decimal, etc?
     positive or positive&negative 


"""

from utils.testtools import test_fixture


class CountDigit():
    def __init__(self) -> None:
        pass

    def count1_binary(self, n: int):
        n = abs(n)
        count = 0
        while n:
            count += n & 1
            n = n >> 1
        return count

    def count1_decimal(self, n: int):
        count = 0
        while n:
            count += 1 if n%10==1 else 0
            n = n // 10
        return count


def test():
    data1 = [
        ((0,),0),
        ((3,),2),
        ((4,),1),
        ((11,),3),
        ((-3,),2),
        # ((,),),
    ]
    data2 = [
        ((0,),0),
        ((13,),1),
        ((479814913984134,),3),
        ((11111,),5),
        ((79704430,),0),
        # ((,),),
    ]
    cd = CountDigit()
    test_fixture(cd.count1_binary, data1)
    test_fixture(cd.count1_decimal, data2)


test()

