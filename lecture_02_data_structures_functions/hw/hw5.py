"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Any, Iterable, List


def custom_range(arr: Iterable[Any], start: Any, stop: Any = None, step: int = 1) -> List:
    """Return blank list if start element isn't in arr"""
    arr = list(arr)
    try:
        ind_start = arr.index(start)
    except ValueError:
        return []

    if not stop:
        return arr[:ind_start]
    else:
        try:
            ind_stop = arr.index(stop)
        except ValueError:
            return []
        return arr[ind_start:ind_stop:step]
