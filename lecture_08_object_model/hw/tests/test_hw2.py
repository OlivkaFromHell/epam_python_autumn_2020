import os

import pytest
from hw.hw2 import TableData

path = os.path.join(os.getcwd(), 'example.sqlite')


@pytest.mark.parametrize('table_name, result', [
    ('presidents', 3),
    ('books', 3)
])
def test_len_attr(table_name, result):
    table = TableData(path, table_name)
    assert len(table) == result


@pytest.mark.parametrize('table_name, name, result', [
    ('presidents', 'Yeltsin',  {'name': 'Yeltsin', 'age': 999, 'country': 'Russia'}),
    ('presidents', 'Trump',  {'name': 'Trump', 'age': 1337, 'country': 'US'}),
    ('books', '1984', {'name': '1984', 'author': 'Orwell'}),
    ('books', 'Farenheit 451', {'name': 'Farenheit 451', 'author': 'Bradbury'}),
])
def test_access_as_collection(table_name, name, result):
    table = TableData(path, table_name)
    assert table.__getitem__(name) == result


@pytest.mark.parametrize('table_name, column, result', [
    ('presidents', 'name', ['Yeltsin', 'Trump', 'Big Man Tyrone']),
    ('presidents', 'age', [999, 1337, 101]),
    ('books', 'name', ['Farenheit 451', 'Brave New World', '1984']),
    ('books', 'author', ['Bradbury', 'Huxley', 'Orwell']),
])
def test_iter_method(table_name, column, result):
    table = TableData(path, table_name)
    list_of_names = []
    for row in table:
        list_of_names.append(row.__getitem__(column))
    assert list_of_names == result


@pytest.mark.parametrize('table_name, value, result', [
    ('presidents', 'Yeltsin', True),
    ('presidents', 'Putin', False),
    ('books', '1984', True),
    ('books', '100', False),
    ('books', 'Orwell', True),
    ('books', 'Lenin', False),
])
def test_contains_mathod(table_name, value, result):
    table = TableData(path, table_name)
    assert (value in table) == result
