
def test_fixture(f:callable, test_data:list[tuple], comp:callable = None):
    def _comp(r, e):
        return r == e     # default implementation

    if not comp:
        comp = _comp

    print(f"    RESULT {'INPUT':^20} {'RETURE':^20} {'EXPECTATION':^20}")
    for i, testcase in enumerate(test_data):
        in_data = testcase[0]
        expect = testcase[1]
        ret = f(*in_data)
        result = 'PASS' if comp(ret,expect) else 'FAIL'
        print(f"{i:<3}: {result}  {str(in_data):^20} {ret:^20} {expect:^20}")

