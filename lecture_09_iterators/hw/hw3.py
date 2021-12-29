"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
# >>> universal_file_counter(test_dir, "txt")
6
# >>> universal_file_counter(test_dir, "txt", str.split)
6

"""
import collections.abc
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
        dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:

    counter = 0
    file_contents = [
        path.read_text()
        for path in Path(dir_path).rglob(f'*.{file_extension}')
    ]

    if isinstance(tokenizer, collections.abc.Callable):
        for file_text in file_contents:
            counter += len(tokenizer(file_text))
    elif tokenizer is None:
        for file_text in file_contents:
            counter += file_text.count('\n') + 1

    return counter


if __name__ == '__main__':
    print('total:', universal_file_counter(Path('files'), 'txt', str.split))
