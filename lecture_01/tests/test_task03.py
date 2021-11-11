import pytest
from hw.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    "test_input,result",
    [
        ("files_for_task03/sample_1.txt", (1, 5)),
        ("files_for_task03/sample_2.txt", (1, 9)),
        ("files_for_task03/sample_3.txt", (-10, 3)),
    ],
)
def test_positive_case_1(test_input, result):
    """Testing that actual powers of 2 give True"""
    assert find_maximum_and_minimum(test_input) == result
