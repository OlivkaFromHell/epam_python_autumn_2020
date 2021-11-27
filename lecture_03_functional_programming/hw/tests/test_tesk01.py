from hw.task01 import cache


def test_positive_case1():
    @cache(times=2)
    def f():
        return 3

    assert f() + f() + f() + f() == 12


def test_positive_case2():
    @cache(times=2)
    def f(a: int, b: int = 4):
        return a * b

    assert f(1, b=1) + f(1, b=1) + f(2, b=1) + f(1) == 8


def test_positive_case3():
    @cache(times=3)
    def f(a: int):
        return a

    assert f(1) + f(2) + f(2) + f(2) == 7


def test_positive_case4():
    times = 5
    time_invoked = 0

    @cache(times=times)
    def greeting(name: str):
        nonlocal time_invoked
        time_invoked += 1
        return f'Hey, {name}'

    for _ in range(6):
        greeting('Dan')

    assert time_invoked == 1
    greeting('Alice')
    assert time_invoked == 2


def test_positive_case_with_id():
    @cache(times=1)
    def func(a, b):
        return (a ** b) ** 2

    some = 100, 200
    val_1 = func(*some)
    val_2 = func(*some)
    val_3 = func(*some)

    assert val_1 is val_2
    assert val_2 is not val_3
