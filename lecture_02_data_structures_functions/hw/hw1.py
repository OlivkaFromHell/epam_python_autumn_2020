"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import re
import string
import unicodedata
from string import punctuation
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Return list of 10 longest words consisting from largest amount of unique symbols sorted from longest"""
    with open(file_path, encoding="raw_unicode_escape") as f:
        line_break = False  # if the last line ends with unfinished word: frei-\nlich'
        unfinished_word = ""
        longest_words = {}
        for line in f:
            words = line.strip().split(" ")

            # TODO: solve for case with hyphen('-') divides words (not lines)
            #  such as 'geistig-politi\nschen' should return 'geistig-politischen' instead of 'geistigpolitischen'
            if line_break and len(words):
                complete_word = unfinished_word + words[0]
                complete_word = re.sub(
                    r"[\W\d_]", "", complete_word
                )  # delete all unicode punctuation
                unique_symbols_amount = len(set(complete_word))
                longest_words.update(
                    {complete_word: unique_symbols_amount}
                )  # str -> set gives unique letters
                words.pop(
                    0
                )  # delete the first word in a line, cause we already proceed it
                unfinished_word = ""

            if len(words) and len(words[-1]) and words[-1][-1] != "-":
                for word in words:
                    word = word.strip(punctuation)
                    unique_symbols_amount = len(set(word))
                    longest_words.update(
                        {word: unique_symbols_amount}
                    )  # str -> set gives unique letters

            # remove the unfinished word from processing
            if len(words) and words[-1] and words[-1][-1] == "-":
                unfinished_word = words.pop()[:-1]

            # checks keys where longest words ends on the line and continuous on the next line
            if unfinished_word:
                line_break = True
            else:
                unfinished_word = ""
                line_break = False

            # sorting dict by values in reverse order
            longest_words = {
                k: v
                for k, v in sorted(
                    longest_words.items(), key=lambda item: item[1], reverse=True
                )
            }
            longest_words = dict(list(longest_words.items())[:10])

    longest_diverse_words = list(longest_words.keys())

    return longest_diverse_words


def get_rarest_char(file_path: str) -> str:
    """Return the rarest char"""
    with open(file_path, encoding="raw_unicode_escape") as f:
        rarest_chars = {}
        for line in f:
            for char in line:
                if (
                    unicodedata.category(char)[0] == "P"
                ):  # if char is unicode punctuation char
                    if char in rarest_chars:
                        amount = rarest_chars[char]
                        rarest_chars.update({char: amount + 1})
                    else:
                        rarest_chars.update({char: 1})

    rarest_char = min(rarest_chars, key=rarest_chars.get)

    return rarest_char


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, encoding="raw_unicode_escape") as f:
        punctuation_chars_amount = 0
        for line in f:
            for char in line:
                if char in punctuation:
                    punctuation_chars_amount += 1

    return punctuation_chars_amount


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, encoding="raw_unicode_escape") as f:
        non_ascii_amount = 0
        for line in f:
            for char in line:
                if char not in string.printable:
                    non_ascii_amount += 1

    return non_ascii_amount


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Return first most common non ascii char"""
    with open(file_path, encoding="raw_unicode_escape") as f:
        non_ascii = {}
        for line in f:
            for char in line:
                if char not in string.printable:
                    if char in non_ascii:
                        amount = non_ascii[char]
                        non_ascii.update({char: amount + 1})
                    else:
                        non_ascii.update({char: 1})

    if non_ascii:
        most_common_non_ascii_char = max(non_ascii, key=non_ascii.get)
        return most_common_non_ascii_char
    else:
        return "No non ascii chars in the file"
