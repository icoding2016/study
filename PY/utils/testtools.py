from io import StringIO
import sys
import timeit
from typing import Callable


def test_fixture(f:callable, test_data:list[tuple], comp:callable = None, hide_input:bool = False, hide_output:bool = False):
    """test fixture.
    Args:
        test_data, in form of:
            [
                ((arg1, arg2, ..), expectation),
                ((arg1, arg2, ..), expectation),
                ...
            ]
    """
    def _comp(r, e):
        return r == e     # default implementation

    if not comp:
        comp = _comp

    t = 0
    print(f'test function: {f}')
    print(f"    RESULT {'INPUT':^30} {'RETURE':^30} {'EXPECTATION':^30}")
    for i, testcase in enumerate(test_data):
        in_data = testcase[0]
        expect = testcase[1]
        starttime = timeit.default_timer()
        ret = f(*in_data)
        t += timeit.default_timer() - starttime
        result = 'PASS' if comp(ret,expect) else 'FAIL'
        # print(f"{i:<3}: {result}  {str(in_data):^20} {ret:^20} {expect:^20}")
        in_arg = f"{str(in_data):^30} " if not hide_input else f"{'  ':^30}"
        ret_exp = f"{str(ret):^30} {str(expect):^30}" if not hide_output else ""
        print(f"{i:<3}: {result} {in_arg}{ret_exp}")
    print(f'Run time: {t}')


def timing(f:callable):
    def wrapper(*args, **kwargs):
        starttime = timeit.default_timer()
        ret = f(*args, **kwargs)
        print(f'Run time: {timeit.default_timer() - starttime}')
        return ret
    return wrapper


stdin_old = sys.stdin
def psudo_stdin_set(handler:StringIO):
    global stdin_old
    stdin_old = sys.stdin
    if handler:
        sys.stdin = handler

def psudo_stdin_restore() -> None:
    global stdin_old
    sys.stdin.close()
    sys.stdin = stdin_old

def psudo_stdout_set(handler:StringIO):
    if handler:
        sys.stdout = handler

def psudo_stdout_restore() -> None:
    sys.stdout.close()
    sys.stdout = sys.__stdout__

def psudo_io(i:StringIO=None, o:StringIO=None):
    psudo_stdin_set(i)
    psudo_stdout_set(o)

def psudo_io_restore():
    psudo_stdin_restore()
    psudo_stdout_restore()


# def psio(data) -> StringIO:
#     output = StringIO()
#     total = len(data)
#     output.write(f"{total}")
#     for args, exp in data:
#         output.write(' '.join(args))
#     return output

_HACKRANK_TEST_DATA = None
_HACKRANK_TEST_EXP = None
def hackrank_test_data(data, exp) -> None:
    global _HACKRANK_TEST_DATA     
    global _HACKRANK_TEST_EXP
    _HACKRANK_TEST_DATA = data
    _HACKRANK_TEST_EXP = exp

def hackrank_test(func:Callable):
    def wrapper(*args, **kargs):
        psin = StringIO(_HACKRANK_TEST_DATA)
        psout = StringIO('')
        psudo_io(psin, psout)
        func(*args, **kargs)   ## >> stdout
        psudo_stdin_restore()
        output = psout.getvalue().strip()
        if output == _HACKRANK_TEST_EXP.strip():
            print('PASS')
        else:
            print('FAIL')
    return wrapper


