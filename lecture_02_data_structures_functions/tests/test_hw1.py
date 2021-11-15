import pytest
from hw.hw1 import (count_non_ascii_chars, count_punctuation_chars,
                    get_longest_diverse_words, get_most_common_non_ascii_char,
                    get_rarest_char)


@pytest.mark.parametrize('filepath,longest_diverse_words', [
    ('test_files_hw1/test_data1.txt', ['Mario', 'It\'s', 'Me']),
    ('test_files_hw1/test_data2.txt', ['aaaaaa']),
    ('test_files_hw1/test_data3.txt', ['complicated', 'Beautiful', 'Explicit',
                                       'complex', 'Complex', 'Python', 'implicit',
                                       'Simple', 'Peters', 'better']),
    ('test_files_hw1/test_data4.txt', ['consectetur', 'adipiscing', 'pulvinar',
                                       'aliquet', 'dignissim', 'libero',
                                       'tempor', 'Lorem', 'ipsum', 'Fusce']),
])
def test_longest_diverse_words(filepath, longest_diverse_words):
    assert get_longest_diverse_words(filepath) == longest_diverse_words


@pytest.mark.parametrize('filepath,rarest_char', [
    ('test_files_hw1/test_data1.txt', '\''),
    ('test_files_hw1/test_data2.txt', '-'),
    ('test_files_hw1/test_data3.txt', ','),
    ('test_files_hw1/test_data4.txt', ','),
])
def test_rarest_char(filepath, rarest_char):
    assert get_rarest_char(filepath) == rarest_char


@pytest.mark.parametrize('filepath,punctuation_chars_amount', [
    ('test_files_hw1/test_data1.txt', 3),
    ('test_files_hw1/test_data2.txt', 1),
    ('test_files_hw1/test_data3.txt', 5),
    ('test_files_hw1/test_data4.txt', 7),
])
def test_count_punctuation_chars(filepath, punctuation_chars_amount):
    assert count_punctuation_chars(filepath) == punctuation_chars_amount


@pytest.mark.parametrize('filepath,non_ascii_amount', [
    ('test_files_hw1/test_data1.txt', 0),
    ('test_files_hw1/test_data2.txt', 0),
    ('test_files_hw1/test_data3.txt', 0),
    ('test_files_hw1/test_data4.txt', 0),
    ('test_files_hw1/test_data5.txt', 2),
])
def test_count_non_ascii_chars(filepath, non_ascii_amount):
    assert count_non_ascii_chars(filepath) == non_ascii_amount


@pytest.mark.parametrize('filepath,most_common_non_ascii_char', [
    ('test_files_hw1/test_data1.txt', 'No non ascii chars in the file'),
    ('test_files_hw1/test_data2.txt', 'No non ascii chars in the file'),
    ('test_files_hw1/test_data3.txt', 'No non ascii chars in the file'),
    ('test_files_hw1/test_data4.txt', 'No non ascii chars in the file'),
    ('test_files_hw1/test_data5.txt', '»'),
])
def test_get_most_common_non_ascii_char(filepath, most_common_non_ascii_char):
    assert get_most_common_non_ascii_char(filepath) == most_common_non_ascii_char
