"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
import inspect
from typing import Callable


def cache(func: Callable) -> Callable:
    cached_values = {}

    def wrapper(*args, **kwargs):
        bound = inspect.signature(func).bind(*args, **kwargs)
        bound.apply_defaults()
        key = str(bound.arguments)

        if key not in cached_values:
            cached_values[key] = func(*args, **kwargs)

        return cached_values[key]

    return wrapper
