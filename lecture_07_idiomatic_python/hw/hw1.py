"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
import collections
from typing import Any, Collection

# Example tree:
example_tree = {
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


def find_occurrences(tree: dict, element: Any) -> int:
    """Returns the number of occurences of element in dict object"""

    def _find_occurences_in_collection(collection_obj: (Collection, dict), element: Any) -> int:
        """find occurences of element if there is a Collection object as input"""
        _counter = 0
        for i in collection_obj:
            if isinstance(i, collections.abc.Mapping):
                _counter += find_occurrences(i, element)
            elif i == element:
                _counter += 1
        return _counter

    counter = 0

    for key, value in tree.items():
        if not isinstance(value, (str, dict)) and isinstance(value, collections.abc.Collection):
            counter += _find_occurences_in_collection(value, element)
        if isinstance(value, collections.abc.Mapping):
            counter += find_occurrences(value, element)
        if key == element:
            counter += 1
        if value == element:
            counter += 1

    return counter


if __name__ == '__main__':
    my_tree = {"RED": "RED", 'big': {'vas': ['RED', {'A': 'RED'}]}}
    print(find_occurrences(example_tree, "RED"))  # 6
    print(find_occurrences(my_tree, "RED"))
