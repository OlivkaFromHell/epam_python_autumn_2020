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
from typing import Callable


def cache(func: Callable) -> Callable:
    cached_values = {}

    def wrapper(*args, **kwargs):
        key = str(f"{args} +{kwargs}")
        result = cached_values.get(key)
        if result:
            return result
        result = func(*args, **kwargs)
        cached_values[key] = result
        return result
    return wrapper
