'''
kwargs:  sequence doen't matter, since the keyward is given
args (no kw): identified by 'position'
there shouldn't be any positional argument behind kwarg   --> SyntaxError: positional argument follows keyword argument
'''


def func1(a, b="default b", c="default c", **kwargs):
    print("func1: a={}, b={}, c={}, d={}".format(a, b, c, kwargs))

def func2(x, y="y", **kwargs):
    return func1(x, b=y, c="a new c", **kwargs)


# a function is an object being evaluated on its definition; 
# default parameters are kind of "member data" and therefore their state may change from one call to the other
#  -- exactly as in any other object.
# https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument
def func3(ll:list=[]) -> list:
    ll.append('a')
    print(id(ll))
    return ll

def test_arg(a=None):
    if not a:
        a = [1]
        print('create a {}'.format(id(a)))
    a.append(a[len(a)-1]+1)
    if len(a) < 5:
        test_arg(a)
        test_arg(a)
    return a

if __name__ == "__main__":
    func2("1st")
    func2("1st", "2nd")
    func2("1st", "2nd", kwarg1="3rd")
    func2("1st", "2nd", kwarg1="3rd", kwarg2="4th")
    func2("1st", kwarg1="3rd", kwarg2="4th", y="2nd")
    #func2(y="2nd-y", "1st")   # SyntaxError: positional argument follows keyword argument
    '''
    func1: a=1st, b=y, c=a new c, d={}
    func1: a=1st, b=2nd, c=a new c, d={}
    func1: a=1st, b=2nd, c=a new c, d={'kwarg1': '3rd'}
    func1: a=1st, b=2nd, c=a new c, d={'kwarg1': '3rd', 'kwarg2': '4th'}
    func1: a=1st, b=2nd, c=a new c, d={'kwarg1': '3rd', 'kwarg2': '4th'}

    '''

    print('id([])',id([]))
    print(func3())
    print(func3())    
    print(func3())    
    print('id([])',id([]))
    # id([]) 2275774816064
    # 2275774792064
    # ['a']
    # 2275774792064
    # ['a', 'a']
    # 2275774792064
    # ['a', 'a', 'a']
    # id([]) 2275774750016    

    r = test_arg()
    print(r)
    print(id(r))
    



