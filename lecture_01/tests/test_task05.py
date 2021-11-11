import pytest
from hw.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize("nums,k,result",
                         [([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
                          ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 24),
                          ([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 45),
                          ([1, 2, 3, 4, 5, 6, 7, 8, 9], 100, 45),
                          ([1, 3, -1, -3, 5, -3, 6, 7], 3, 13),
                          ([1, 3, -1, -3, 5, -3, 6, 7], 1, 7),
                          ([i for i in range(10000)], 5, 49985),
                          ([-5, -3, -1, -3, -5, -3, -6, -7], 3, -1),
                          ([-3, -5, 3, 6, -7], 3, 9)])
def test_positive_case(nums, k, result):
    """Testing that correct list gives right answer"""
    assert find_maximal_subarray_sum(nums, k) == result


def test_k_lower_one_case():
    """Testing that k < 1 list returns 0"""
    nums = [-5, -3, -1, -3, -5, -3, -6, -7]
    k = 0
    result = 0
    assert find_maximal_subarray_sum(nums, k) == result
