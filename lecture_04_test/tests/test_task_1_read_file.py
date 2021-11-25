import os

import pytest
from hw.task_1_read_file import read_magic_number


@pytest.mark.parametrize("path, text", [
    ('test1.txt', '2\nHi, fellows\nisdigit'),
    ('test2.txt', '2.4\nStar\nWars'),
    ('test3.txt', '1\n'),
    ('test3.txt', '2.999999\n3\n5'),
])
def test_positive_case(path, text):
    with open(path, 'w') as f:
        f.write(text)
    assert read_magic_number(path) is True
    os.remove(path)


@pytest.mark.parametrize("path, text", [
    ('test.txt', '100\nBye, fellows\nis'),
    ('test.txt', '3\nLOTR'),
    ('test.txt', '-3\n'),
    ('test.txt', '0.999999'),
    ('test.txt', '1e4\n'),
])
def test_negative_case(path, text):
    with open(path, 'w') as f:
        f.write(text)
    assert read_magic_number(path) is False
    os.remove(path)


@pytest.mark.parametrize("path, text", [
    ('test.txt', '\nBye, fellows\nis'),
    ('test.txt', '2,1\nLOTR'),
    ('test.txt', '0.9.3\n'),
    ('test.txt', 'python4.999999'),
])
def test_with_error(path, text):
    with open(path, 'w') as f:
        f.write(text)
    with pytest.raises(ValueError):
        read_magic_number(path)

    os.remove(path)
