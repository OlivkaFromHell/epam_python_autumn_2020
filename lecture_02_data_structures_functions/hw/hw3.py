"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from itertools import product
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    list_k_items = []
    for comb in product(*args):
        list_k_items.append([*comb])
    # another solution is just: return list(product(*args))
    # but it returns List[Tuple] instead List[List]
    return list_k_items
