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
