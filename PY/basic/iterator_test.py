class FRange(object):
    def __init__(self, start, stop=None, step=None):
        if stop is None:
            self.i = 0
            self.stop = start
            self.step = 1
        elif step is None:
            self.i = start
            self.stop = stop
            self.step = 1
        else:
            self.i = start
            self.stop = stop
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.stop:
            raise StopIteration
        i = self.i
        self.i += self.step
        return i


def test_frange(args):
    return list(FRange(*args))

def test():
    fr1 = test_frange([5])
    fr2 = test_frange([1.2,4.2])
    fr3 = test_frange([1.3, 8.5, 1.0])

    print(list(fr1))
    print(list(fr2))
    print(list(fr3))


test()


