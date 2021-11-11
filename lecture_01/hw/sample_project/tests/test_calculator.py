import pytest
from calculator.calc import check_power_of_2


@pytest.mark.parametrize("test_input", [65536, 1024, 4])
def test_positive_case(test_input):
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(test_input)


@pytest.mark.parametrize("test_input",
                         [12, 3, 121, 1000,
                          *[i for i in range(10, 1000, 25) if i % 3 == 0]])
def test_negative_case(test_input):
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(test_input)


@pytest.mark.parametrize("test_input",
                         [-1, -4, -128, -500,
                          *[i for i in range(-100, 0, 6)]])
def test_negative_number_case(test_input):
    """Testing that negative number give False"""
    assert not check_power_of_2(test_input)


def test_zero_case():
    """Testing that zero number give False"""
    assert not check_power_of_2(0)
