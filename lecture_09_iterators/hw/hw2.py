"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

# >>> with supressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager


class Suppresor:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return isinstance(exc_val, self.exception)


@contextmanager
def suppresor(exception):
    try:
        yield
    except exception:
        pass


if __name__ == '__main__':
    with suppresor(IndexError):
        [][2]
