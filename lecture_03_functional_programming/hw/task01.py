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

from typing import Callable


def cache(times: int) -> Callable:
    """Cache decorator which returns func result n times"""
    def _cache(func: Callable) -> Callable:
        output = None
        counter_times = times

        def wrapper(*args, **kwargs):
            nonlocal counter_times, output

            if counter_times == times:
                counter_times = times - 1
                output = func(*args, **kwargs)
                return output

            if counter_times == -1:
                counter_times = times - 1
                output = func(*args, **kwargs)
                return output

            if counter_times >= 0:
                counter_times -= 1
                return output

        return wrapper

    return _cache
