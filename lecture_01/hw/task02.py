"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def last_fib(num: int) -> int:
    """Return last Fibonacci number sequnce before number num"""
    if num == 0:
        return 0
    fib = [0, 1]
    i = 2
    # appends fib numbers until fib[-1] == num or > num
    # if fib[-1] > num it means that first number of original sequnce
    # data isn't belong to fib nums
    while fib[-1] < num:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1

    return fib[-1]


def check_fibonacci(data: Sequence[int]) -> bool:

    if len(data) < 3:
        return False

    if data[0] != last_fib(data[0]):
        return False

    # if seq is [0, -fib1, -fib2...] it shouldn't return True
    if data[1] < 0:
        return False

    i = 0
    while i <= len(data) - 3:
        if not (data[i] + data[i+1] == data[i+2]):
            return False
        i += 1
    return True
