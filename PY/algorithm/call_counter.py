

_t_counter = 0
_cur_func = None

def call_counter(func:callable):
    def wrapper(* args):
        global _cur_func
        global _t_counter
        if _cur_func != func:
            global _t_counter
            _t_counter = 0    # init counter
            _cur_func = func
        _t_counter += 1
        result = func(*args)
        #print('{} run {} times'.format(func, t_counter))
        return result
    return wrapper

def _get_last_call_counter():
    global _t_counter
    global _cur_func
    return '{} called {} times.'.format(_cur_func.__name__, _t_counter)

def show_call_counter():
    global _t_counter
    global _cur_func
    print(_get_last_call_counter())
    _t_counter = 0
    _cur_func = None


####### test #######

@call_counter
def _call_counter_tester():
    #print('_call_counter_tester called')
    pass

@call_counter
def _call_counter_tester2():
    #print('_call_counter_tester2 called')
    pass
    
def _test_call_counter():
    for i in range(10):
        _call_counter_tester()
    show_call_counter()
    for i in range(6):
        _call_counter_tester2()
    show_call_counter()


def _test():
    _test_call_counter()


