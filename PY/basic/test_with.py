

class A(object):
    def __init__(self):
        print('A init.')

    def __enter__(self):
        print('A entering')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('A exit.. do cleanup.')


def test():
    with A() as a:
        print('within with statement.')
    print('outside with statement')


test()

