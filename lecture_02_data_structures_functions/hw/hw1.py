"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from collections import Counter
from string import punctuation
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Return list of 10 longest words consisting from largest amount of unique symbols sorted from longest"""
    with open(file_path, encoding='raw_unicode_escape') as f:
        line_break = False  # if the last line ends with unfinished word: frei-\nlich'
        unfinished_word = ''
        longest_words = {}
        for line in f:
            words = line.strip().split(' ')

            # remove the unfinished word from processing
            if words[-1] and words[-1][-1] == '-':
                unfinished_word = words.pop()[:-1]

            if line_break:
                complete_word = unfinished_word + words[0]
                complete_word = complete_word.strip(punctuation)
                unique_symbols_amount = len(set(complete_word))
                longest_words.update({complete_word: unique_symbols_amount})  # str -> set gives unique letters
                words.pop(0)  # delete the first word in a line, cause we proceed it

            for word in words:
                word = word.strip(punctuation)
                unique_symbols_amount = len(set(word))
                longest_words.update({word: unique_symbols_amount})  # str -> set gives unique letters

            # checks keys where longest words ends on the line and continuous on the next line
            if unfinished_word:
                line_break = True
            else:
                line_break = False

            # sorting dict by values in reverse order
            longest_words = {k: v for k, v in sorted(longest_words.items(), key=lambda item: item[1], reverse=True)}
            longest_words = dict(list(longest_words.items())[:10])

    longest_diverse_words = list(longest_words.keys())

    return longest_diverse_words


def get_rarest_char(file_path: str) -> str:
    """Return the last found rarest char"""
    with open(file_path, encoding='raw_unicode_escape') as f:
        rarest_chars = []
        for line in f:
            for char in line:
                rarest_chars.append(char)

    rarest_chr = Counter(rarest_chars).most_common()[-1][0]
    return rarest_chr


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, encoding='raw_unicode_escape') as f:
        punctuation_chars_amount = 0
        for line in f:
            for char in line:
                if char in punctuation:
                    punctuation_chars_amount += 1

    return punctuation_chars_amount


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, encoding='raw_unicode_escape') as f:
        non_ascii_amount = 0
        for line in f:
            for char in line:
                if ord(char) > 128:  # or char.isalpha() == False
                    non_ascii_amount += 1

    return non_ascii_amount


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Return first most common non ascii char"""
    with open(file_path, encoding='raw_unicode_escape') as f:
        non_ascii = []
        for line in f:
            for char in line:
                if ord(char) > 128:
                    non_ascii.append(char)
    if non_ascii:
        most_common_non_ascii_char = Counter(non_ascii).most_common(1)[0][0]
        return most_common_non_ascii_char
    else:
        return 'No non ascii chars in the file'
