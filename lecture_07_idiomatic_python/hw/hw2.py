"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""
from itertools import zip_longest


def backspace_compare(first: str, second: str) -> bool:
    def process_data(data: str):
        sharp_counter = 0
        for symbol in data[::-1]:
            if symbol == '#':
                sharp_counter += 1
                continue
            if sharp_counter:
                sharp_counter -= 1
                continue
            yield symbol

    first_gen = process_data(first)
    second_gen = process_data(second)

    for first_elem, second_elem in zip_longest(first_gen, second_gen, fillvalue=None):
        if first_elem != second_elem:
            return False
    return True


if __name__ == '__main__':
    s = "a#c"
    t = "#b"
    print(backspace_compare(s, t))
