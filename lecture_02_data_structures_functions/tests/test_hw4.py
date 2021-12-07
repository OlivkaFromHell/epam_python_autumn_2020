from hw.hw4 import cache


def test_positive_case1():
    def func(a, b):
        return (a ** b) ** 2

    cache_func = cache(func)

    some = 100, 200

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)

    assert val_1 is val_2


def test_positive_case2():
    check = True

    def func(a, b):
        nonlocal check
        check = not check
        return a + b

    cache_func = cache(func)

    some = 'import', 'this'

    cache_func(*some)
    cache_func(*some)

    assert not check


def test_positive_case3():
    check = True

    def func(repeat: str, amount: int):
        nonlocal check
        check = not check
        return repeat * amount

    cache_func = cache(func)

    some = 'zzz', 3

    cache_func(*some)
    cache_func(*some)

    assert not check


def test_args_order():
    check = True

    def func(a: int, b: int):
        nonlocal check
        check = not check
        return a - b

    cache_func = cache(func)

    cache_func(3, 2)
    cache_func(2, 3)

    assert check


def test_kwargs_order():
    check = True

    def func(a: int, b: int):
        nonlocal check
        check = not check
        return a - b

    cache_func = cache(func)

    cache_func(a=3, b=2)
    cache_func(b=2, a=3)

    assert not check


def test_args_kwargs_name():
    check = True

    def func(a: str, b: str):
        nonlocal check
        check = not check
        return a + b

    cache_func = cache(func)

    cache_func('2', b='\'b\'')
    cache_func(a='2', b='\'b\'')

    assert not check
