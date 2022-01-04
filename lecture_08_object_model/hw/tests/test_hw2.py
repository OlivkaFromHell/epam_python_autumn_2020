import sqlite3
from pathlib import Path

import pytest
from hw8.hw2 import TableData

path = Path(__file__).parent.joinpath('example.sqlite')


@pytest.mark.parametrize('table_name, result', [
    ('presidents', 3),
    ('books', 3)
])
def test_len_attr(table_name, result):
    with TableData(path, table_name) as table:
        assert len(table) == result


@pytest.mark.parametrize('table_name, name, result', [
    ('presidents', 'Yeltsin', {'name': 'Yeltsin', 'age': 999, 'country': 'Russia'}),
    ('presidents', 'Trump', {'name': 'Trump', 'age': 1337, 'country': 'US'}),
    ('books', '1984', {'name': '1984', 'author': 'Orwell'}),
    ('books', 'Farenheit 451', {'name': 'Farenheit 451', 'author': 'Bradbury'}),
])
def test_access_as_collection(table_name, name, result):
    with TableData(path, table_name) as table:
        assert table[name] == result


@pytest.mark.parametrize('table_name, column, result', [
    ('presidents', 'name', ['Yeltsin', 'Trump', 'Big Man Tyrone']),
    ('presidents', 'age', [999, 1337, 101]),
    ('books', 'name', ['Farenheit 451', 'Brave New World', '1984']),
    ('books', 'author', ['Bradbury', 'Huxley', 'Orwell']),
])
def test_iter_method(table_name, column, result):
    with TableData(path, table_name) as table:
        list_of_names = []
        for row in table:
            list_of_names.append(row[column])
        assert list_of_names == result


@pytest.mark.parametrize('table_name, value, result', [
    ('presidents', 'Yeltsin', True),
    ('presidents', 'Putin', False),
    ('books', '1984', True),
    ('books', '100', False),
    ('books', 'Farenheit 451', True),
    ('books', 'Lenin', False),
])
def test_contains_mathod(table_name, value, result):
    with TableData(path, table_name) as table:
        assert (value in table) == result


def test_2_instances():
    with TableData(path, 'presidents') as presidents, TableData(path, 'books') as books:
        assert len(presidents) == len(books)


def test_check_injection_avoidance():
    with TableData(path, 'books') as table:
        table['Farenheit 451; DROP DATABASE']
        assert table['Farenheit 451'] == {'name': 'Farenheit 451', 'author': 'Bradbury'}


def test_check_valid_table_name():
    with pytest.raises(sqlite3.OperationalError):
        with TableData(path, 'non_existing_table') as table:
            assert table['Farenheit 451'] == {'name': 'Farenheit 451', 'author': 'Bradbury'}
