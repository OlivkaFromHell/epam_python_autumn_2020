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
    ans = []
    arr = list(arr)
    ind_start = arr.index(start)
    if not stop:
        for i in range(ind_start):
            ans.append(arr[i])
    else:
        ind_stop = arr.index(stop)
        for i in range(ind_start, ind_stop, step):
            ans.append(arr[i])

    return ans
