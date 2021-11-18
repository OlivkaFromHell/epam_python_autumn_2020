import pytest
from hw.task04 import is_armstrong


@pytest.mark.parametrize('number', [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])
def test_positive_case(number):
    assert is_armstrong(number)


@pytest.mark.parametrize('number', [11, 32, 300, 400, 8321])
def test_negative_case(number):
    assert not is_armstrong(number)
