import timeit


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
