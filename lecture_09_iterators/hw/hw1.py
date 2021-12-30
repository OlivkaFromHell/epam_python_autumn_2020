"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

#>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Iterator, List, Union


def data_generator(list_of_numbers: list) -> Iterator:
    while list_of_numbers:
        first_elems = [j[0] for j in list_of_numbers]
        to_return = min(first_elems)
        del list_of_numbers[first_elems.index(to_return)][0]

        # if list is empty -> delete list form list_of_numbers
        if not list_of_numbers[first_elems.index(to_return)]:
            del list_of_numbers[first_elems.index(to_return)]

        yield to_return


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    file_contest = [
        list(map(
            int, Path(__file__).parent.joinpath(path)
            .read_text().split('\n')))
        for path in file_list
    ]

    generators = data_generator(file_contest)
    for num in generators:
        yield num


if __name__ == '__main__':
    print(list(merge_sorted_files(["files/file1.txt", "files/file2.txt"])))
