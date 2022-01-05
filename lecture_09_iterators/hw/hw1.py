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


def data_generator(list_of_files: list) -> Iterator:

    rows = {}  # dict with last line from file
    files = list(map(open, list_of_files))
    files_dict = {}  # dict with links to file

    for index, file in enumerate(files):
        rows[index] = None
        files_dict[index] = file

    while files_dict:
        to_delete = None

        for file in files_dict:
            if rows[file] is None:  # read new line
                number = files_dict[file].readline().strip()

                # if this is the end of the file, mark it for delete
                if number == '':
                    # if we delete link to file from files_dict here, we will get an error
                    to_delete = file
                else:
                    rows[file] = int(number)

        # delete link to file from dict
        if to_delete is not None:
            del rows[to_delete]
            files_dict[to_delete].close()
            del files_dict[to_delete]

        if rows:
            key_file = min(rows, key=rows.get)
            to_return = rows[key_file]
            rows[key_file] = None
            yield to_return


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    file_contest = [
        Path(__file__).parent.joinpath(path)
        for path in file_list
    ]

    generators = data_generator(file_contest)
    for num in generators:
        yield num


if __name__ == '__main__':
    print(list(merge_sorted_files(["files/file1.txt", "files/file2.txt"])))
