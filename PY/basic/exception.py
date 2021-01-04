


class InvalidInputException(Exception):
    pass

def divide(x,y):
    if y == 0:
        raise InvalidInputException("Invalid input, divide by zero.")
    return x/y


def test():
    print(divide(6,3))
    print(divide(3,0))


test()

