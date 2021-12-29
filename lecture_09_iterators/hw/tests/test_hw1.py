import pytest
from hw.hw1 import merge_sorted_files


@pytest.fixture
def opened_files(request, tmpdir):
    """fixture which creates multiple files with parameterized data"""
    amount_files = len(request.param)
    list_of_paths = []
    for i in range(amount_files):
        file = tmpdir.join(f'test_{i}.txt')
        file.write(request.param[i])
        list_of_paths.append(file.strpath)

    return list_of_paths


@pytest.mark.parametrize("opened_files", [
    ('1\n3\n5', '2\n4\n6'),
], indirect=True)
@pytest.mark.parametrize('result', [
    [1, 2, 3, 4, 5, 6],
])
def test_positive_case_1(opened_files, result):
    assert list(merge_sorted_files([*opened_files])) == result


@pytest.mark.parametrize("opened_files", [
    ('1\n3\n5', '2\n4\n6', '3\n7\n9'),
], indirect=True)
@pytest.mark.parametrize('result', [
    [1, 2, 3, 3, 4, 5, 6, 7, 9],
])
def test_positive_case_2(opened_files, result):
    assert list(merge_sorted_files([*opened_files])) == result


@pytest.mark.parametrize("opened_files", [
    ('1', '2', '3', '4', '5', '6', '7', '8'),
], indirect=True)
@pytest.mark.parametrize('result', [
    [1, 2, 3, 4, 5, 6, 7, 8],
])
def test_positive_case_3(opened_files, result):
    assert list(merge_sorted_files([*opened_files])) == result
