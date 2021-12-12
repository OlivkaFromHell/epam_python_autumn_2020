import pytest
from hw.hw3 import combinations


@pytest.mark.parametrize('arg1,arg2,result', [
    ([1, 2], [3, 4], [[1, 3], [1, 4], [2, 3], [2, 4]]),
    ([1, 2], [3], [[1, 3], [2, 3]]),
    ([1], [2, 3, 4], [[1, 2], [1, 3], [1, 4]]),
])
def test_positive_case_2_args(arg1, arg2, result):
    assert combinations(arg1, arg2) == result


@pytest.mark.parametrize('arg1,arg2,arg3,result', [
    ([1, 2], [3, 4], [1], [[1, 3, 1], [1, 4, 1], [2, 3, 1], [2, 4, 1]]),
    ([1], [2], [3], [[1, 2, 3]]),
    ([1], [2, 3], [4, 5, 6], [[1, 2, 4], [1, 2, 5], [1, 2, 6], [1, 3, 4], [1, 3, 5], [1, 3, 6]]),
])
def test_positive_case_3_args(arg1, arg2, arg3, result):
    assert combinations(arg1, arg2, arg3) == result


@pytest.mark.parametrize('arg1,arg2,result', [
    ([1], [3, 4], [[1, 3]]),
    ([1, 2], [3], []),
])
def test_negative_case(arg1, arg2, result):
    assert combinations(arg1, arg2) != result
