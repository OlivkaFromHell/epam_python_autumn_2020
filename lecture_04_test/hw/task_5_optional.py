"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


# >>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
# from typing import Generator


def fizzbuzz(n: int):
    """
    Generate n FizzBuzz numbers

    >>> list(fizzbuzz(5))
    ['1', '2', 'fizz', '4', 'buzz']
    """

    for i in range(1, n + 1):
        if i % 15 == 0:
            yield 'fizz buzz'
        elif i % 3 == 0:
            yield 'fizz'
        elif i % 5 == 0:
            yield 'buzz'
        else:
            yield str(i)


if __name__ == '__main__':
    print(list(fizzbuzz(25)))
