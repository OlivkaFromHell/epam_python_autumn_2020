from hw.task01 import cache


def test_positive_case1():
    time_invoked = 0

    @cache(times=2)
    def f(a):
        nonlocal time_invoked
        time_invoked += 1
        return a

    f(1) + f(2) + f(3) + f(4)

    assert time_invoked == 4


def test_positive_case2():
    time_invoked = 0

    @cache(times=2)
    def f(a: int, b: int = 1):
        nonlocal time_invoked
        time_invoked += 1
        return a * b

    f(1, b=1) + f(a=1, b=1) + f(1)

    assert time_invoked == 1


def test_positive_case3():
    time_invoked = 0

    @cache(times=2)
    def f(a: int):
        nonlocal time_invoked
        time_invoked += 1
        return a

    f(1) + f(2) + f(2) + f(2)

    assert time_invoked == 2


def test_positive_case4():
    time_invoked = 0

    @cache(times=2)
    def f(a: int):
        nonlocal time_invoked
        time_invoked += 1
        return a

    f(1) + f(2) + f(2) + f(2) + f(2)

    assert time_invoked == 3


def test_positive_case5():
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
