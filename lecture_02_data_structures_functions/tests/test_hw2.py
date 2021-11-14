import pytest

from hw.hw2 import major_and_minor_elem


@pytest.mark.parametrize('inp,elem', [
    ([3, 2, 3], (3, 2)),
    ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
    ([1, 1, 1, 1, 1, 1, 1], (1, 1)),
    ([1, 2, 5, 5, 5], (5, 2)),
])
def test_positive_case(inp, elem):
    assert major_and_minor_elem(inp) == elem


@pytest.mark.parametrize('inp', [
    [1, 2, 3],
    [1],
    [1, 2],
    [1, 2, 3, 5, 5],
])
def test_negative_case(inp):
    try:
        major_and_minor_elem(inp)
    except ValueError:
        pass
