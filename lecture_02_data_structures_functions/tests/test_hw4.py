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
    def func(a, b):
        return a + b

    cache_func = cache(func)

    some = 'import', 'this'

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)

    assert val_1 is val_2


def test_positive_case3():
    def func(repeat: str, amount: int):
        return repeat * amount

    cache_func = cache(func)

    some = 'zzz', 3

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)

    assert val_1 is val_2


def test_args_order():
    def func(a: int, b: int):
        return a - b

    cache_func = cache(func)

    val_1 = cache_func(3, 2)
    val_2 = cache_func(2, 3)

    assert val_1 is not val_2


def test_args_name():
    def func(a: str, b: str):
        return a + b

    cache_func = cache(func)

    val_1 = cache_func('2', b='\'b\'')
    val_2 = cache_func(a='2', b='\'b\'')

    assert val_1 is not val_2
