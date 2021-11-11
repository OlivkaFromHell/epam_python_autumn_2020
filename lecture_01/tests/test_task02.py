import pytest
from hw.task02 import check_fibonacci

data_positive = [
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597,
     2584, 4181, 6765],
    [21, 34, 55, 89, 144],
    [1597, 2584, 4181],
]

data_negative = [
    [21, 35, 55, 89, 144],
    [21, 34, 56, 89, 144],
    [0, 1, 1, 5],
    [10, 20, 30, 50, 80, 130, 210],
    [-30, -50, -100, -101, -102],
    [0, -1, -1, -2, -3, -5],
    [-1, -1, -2, -3, -5],
]


@pytest.mark.parametrize("test_input", [*data_positive])
def test_positive_case(test_input):
    """Testing that correct list gives True"""
    assert check_fibonacci(test_input)


@pytest.mark.parametrize("test_input", [*data_negative])
def test_negative_case(test_input):
    """Testing that wrong list gives False"""
    assert not check_fibonacci(test_input)


def test_case_len_less_3():
    """Testing that list with length less than 3 gives False"""
    data_to_process = [0, 1]
    assert not check_fibonacci(data_to_process)
