from pathlib import Path

import pytest
from hw.hw3 import universal_file_counter


@pytest.fixture
def opened_files(request, tmpdir):
    """fixture which creates multiple files with parameterized data"""
    amount_files = len(request.param)
    list_of_paths = []
    for i in range(amount_files):
        file = tmpdir.join(f'test_{i}.txt')
        file.write(request.param[i])
        list_of_paths.append(file.strpath)

    return Path(tmpdir)


@pytest.mark.parametrize("opened_files", [
    ('1\n3\n5', '2\n4\n6'),
], indirect=True)
@pytest.mark.parametrize('result', [
    6,
])
def test_positive_case_without_tokenizer(opened_files, result):
    assert universal_file_counter(opened_files, 'txt') == result


@pytest.mark.parametrize("opened_files", [
    ('1\n3\n5', '2\n4\n6'),
], indirect=True)
@pytest.mark.parametrize('result, tokenizer', [
    (6, str.split),
])
def test_positive_case_with_tokenizer_1(opened_files, result, tokenizer):
    assert universal_file_counter(opened_files, 'txt', tokenizer) == result


@pytest.mark.parametrize("opened_files", [
    ('1', '2', '3'),
], indirect=True)
@pytest.mark.parametrize('result, tokenizer', [
    (3, str.split),
])
def test_positive_case_with_tokenizer_2(opened_files, result, tokenizer):
    assert universal_file_counter(opened_files, 'txt', tokenizer) == result


@pytest.mark.parametrize("opened_files", [
    ('1\n3', '2', '3'),
], indirect=True)
@pytest.mark.parametrize('result, tokenizer', [
    (4, str.splitlines),
])
def test_positive_case_with_tokenizer_3(opened_files, result, tokenizer):
    assert universal_file_counter(opened_files, 'txt', tokenizer) == result
