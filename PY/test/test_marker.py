import pytest


def test_1():
    print("run test 1")


@pytest.mark.skip_1
@pytest.mark.parametrize('a1, a2', [('a11', 'a21'), ('a12', 'a22')])
def test_2(a1, a2):
    print(f"test 2 with args: {a1} {a2}")
    failure_cases = [
        ('a12', 'a22')
    ]
    if (a1, a2) in failure_cases:
        assert False
    assert True

@pytest.mark.optional
@pytest.mark.parametrize('a1, a2', [('a11', 'a21'), ('a12', 'a22')])
def test_3(a1, a2):
    print(f"test 3 with args: {a1} {a2}")




