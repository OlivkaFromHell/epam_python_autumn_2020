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


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:

    file_contest = [
        Path(__file__).parent.joinpath(path).read_text().split('\n')
        for path in file_list
    ]

    merged_lists = []
    for lst in file_contest:
        lst = list(map(int, lst))
        merged_lists.extend(lst)

    merged_lists.sort()
    return iter(merged_lists)


if __name__ == '__main__':
    print(list(merge_sorted_files(["files/file1.txt", "files/file2.txt"])))
