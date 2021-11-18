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

    assert f(3, b=1) + f(3, b=1) + f(5, b=6), f(2) == 44


def test_positive_case3():
    @cache(times=3)
    def f(a: int):
        return a

    assert f(1) + f(2) + f(2) + f(2) == 4


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
