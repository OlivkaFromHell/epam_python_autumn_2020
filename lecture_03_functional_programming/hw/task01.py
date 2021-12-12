"""
In previous homework task 4, you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        return input('? ')   # careful with input() in python2, use raw_input() instead

    >> f()
    ? 1
    '1'
    >> f()     # will remember previous value
    '1'
    >> f()     # but use it up to two times only
    '1'
    >> f()
    ? 2
    '2'
"""

import inspect
from typing import Callable


def cache(times: int) -> Callable:
    """Cache decorator which returns func result n times"""
    cached_values = {}

    def _cache(func: Callable) -> Callable:

        def wrapper(*args, **kwargs):
            bound = inspect.signature(func).bind(*args, **kwargs)
            bound.apply_defaults()
            key = str(bound.arguments)

            if key not in cached_values:
                cached_values[key] = [func(*args, **kwargs), times+1]

            if cached_values[key][1] > 1:
                cached_values[key][1] -= 1
                return cached_values[key][0]

            result = cached_values[key][0]
            del cached_values[key]
            return result

        return wrapper

    return _cache
