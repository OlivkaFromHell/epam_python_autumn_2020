import pytest
from hw.hw2 import backspace_compare


@pytest.mark.parametrize('first, second, result', [
    ("ab#c", "ad#c", True),
    ("a##c", "#a#c", True),
    ("a#c", "b", False),
    ("aa##d", "#d", True),
    ("aa##da", "#da", True),
    ("###a", "###a", True),
])
def test_positive_case(first, second, result):
    assert backspace_compare(first, second) == result


def test_only_sharp():
    assert backspace_compare('#', '##')


@pytest.mark.parametrize('first, second, result', [
    ('a', 'a', True),
    ('a', 'b', False)
])
def test_only_strings(first, second, result):
    assert backspace_compare(first, second) == result
