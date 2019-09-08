'''
kwargs:  sequence doen't matter, since the keyward is given
args (no kw): identified by 'position'
there shouldn't be any positional argument behind kwarg   --> SyntaxError: positional argument follows keyword argument
'''


def func1(a, b="default b", c="default c", **kwargs):
    print("func1: a={}, b={}, c={}, d={}".format(a, b, c, kwargs))

def func2(x, y="y", **kwargs):
    return func1(x, b=y, c="a new c", **kwargs)


if __name__ == "__main__":
    func2("1st")
    func2("1st", "2nd")
    func2("1st", "2nd", kwarg1="3rd")
    func2("1st", "2nd", kwarg1="3rd", kwarg2="4th")
    func2("1st", kwarg1="3rd", kwarg2="4th", y="2nd")
    func2(y="2nd-y", "1st")
    '''
    func1: a=1st, b=y, c=a new c, d={}
    func1: a=1st, b=2nd, c=a new c, d={}
    func1: a=1st, b=2nd, c=a new c, d={'kwarg1': '3rd'}
    func1: a=1st, b=2nd, c=a new c, d={'kwarg1': '3rd', 'kwarg2': '4th'}
    func1: a=1st, b=2nd, c=a new c, d={'kwarg1': '3rd', 'kwarg2': '4th'}

    '''



