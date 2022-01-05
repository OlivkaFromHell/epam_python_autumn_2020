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

    for path in Path(dir_path).rglob(f'*.{file_extension}'):
        with open(path) as f:
            text = f.read()
            if isinstance(tokenizer, collections.abc.Callable):
                counter += len(tokenizer(text))
            elif tokenizer is None:
                counter += text.count('\n') + 1

    return counter


if __name__ == '__main__':
    print('total:', universal_file_counter(Path('files'), 'txt', str.split))
