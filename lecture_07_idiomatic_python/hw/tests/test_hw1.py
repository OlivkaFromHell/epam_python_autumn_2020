import pytest
from hw.hw1 import find_occurrences

example_tree_1 = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
    },
    "fourth": "RED",
}

example_tree_2 = {"RED": "RED", 'big': {'vas': ['RED', {'A': 'RED'}]}}

example_tree_3 = {1: [1, {1: 1}]}

example_tree_4 = {'1': [1, {1: 1}]}


@pytest.mark.parametrize('tree, element, result', [
    (example_tree_1, 'RED', 6),
    (example_tree_1, 'value1', 1),
    (example_tree_1, 'nested_key', 1),
    (example_tree_1, 'BLUE', 2),
    (example_tree_2, 'RED', 4),
    (example_tree_2, 'big', 1),
    (example_tree_3, 1, 4),
    (example_tree_4, 1, 3),
])
def test_positive_case(tree, element, result):
    assert find_occurrences(tree, element) == result
