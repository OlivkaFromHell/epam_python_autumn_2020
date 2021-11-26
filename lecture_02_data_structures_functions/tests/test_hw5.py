import string

import pytest
from hw.hw5 import custom_range


@pytest.mark.parametrize("arr,start,stop,result", [
    ([1, 2, 3, 4, 5, 6], 1, 3, [1, 2]),
    ([1, 2, 3, 4, 5, 6], 3, 5, [3, 4]),
    ([4, 5, 1], 4, 1, [4, 5]),
    ([10, 2, 3, 5, 1], 2, 5, [2, 3]),
    ([10, 2, 3, 5, 1], 2, 1, [2, 3, 5]),
    (string.ascii_lowercase, 'a', 'd', ['a', 'b', 'c']),
    (string.ascii_lowercase, 'g', 'p', ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']),
    ((1, 3, 4, 6, 7, 2), 3, 2, [3, 4, 6, 7]),
    ((1, 3, 4, 6, 7, 2), 7, 1, []),
    ((1, 3, 4, 6, 7, 2), 3, 4, [3]),
])
def test_no_step_case(arr, start, stop, result):
    """Checks that functions works correctly"""
    assert custom_range(arr, start, stop) == result


@pytest.mark.parametrize("arr,start,result", [
    ([1, 2, 3, 4, 5, 6], 3, [1, 2]),
    ([1, 2, 3, 4, 5, 6], 5, [1, 2, 3, 4]),
    ([4, 5, 1], 4, []),
    ([10, 2, 3, 5, 1], 2, [10]),
    ([10, 2, 3, 5, 1], 1, [10, 2, 3, 5]),
    (string.ascii_lowercase, 'a', []),
    (string.ascii_lowercase, 'g', ['a', 'b', 'c', 'd', 'e', 'f']),
    (string.ascii_lowercase, 'b', ['a']),
    ((1, 3, 4, 6, 7, 2), 7, [1, 3, 4, 6]),
])
def test_no_stop_case(arr, start, result):
    """Checks that functions works correctly"""
    assert custom_range(arr, start) == result


@pytest.mark.parametrize("arr,start,stop,step,result", [
    ([1, 2, 3, 4, 5, 6], 1, 6, 2, [1, 3, 5]),
    ([1, 2, 3, 4, 5, 6], 1, 5, 2, [1, 3]),
    ([4, 5, 1], 4, 1, 3, [4]),
    ([10, 2, 3, 5, 1], 10, 1, 3, [10, 5]),
    ([10, 2, 3, 5, 1], 1, 10, -2, [1, 3]),
    (string.ascii_lowercase, 'a', 'd', 2, ['a', 'c']),
    (string.ascii_lowercase, 'p', 'g', -2, ['p', 'n', 'l', 'j', 'h']),
    ((1, 3, 4, 6, 7, 2), 2, 3, -2, [2, 6]),
    ((1, 3, 4, 6, 7, 2), 7, 6, -5, [7]),
    ((1, 3, 4, 6, 7, 2), 4, 7, -2, []),
])
def test_step_case(arr, start, stop, step, result):
    """Checks that functions works with list and givel step size"""
    assert custom_range(arr, start, stop, step) == result


def test_negative_case():
    """return [] if start element doesn't exist in array"""
    assert custom_range([1, 2, 3], -1) == []
