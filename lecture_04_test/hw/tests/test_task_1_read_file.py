import pytest
from hw.task_1_read_file import MagicNumberError, read_magic_number


@pytest.fixture
def opened_file(request, tmpdir):
    file = tmpdir.join('test.txt')
    file.write(request.param)
    return file.strpath


@pytest.mark.parametrize("opened_file", [
    '2\nHi, fellows\nisdigit',
    '2.4\nStar\nWars',
    '1\n',
    '2.999999\n3\n5',
], indirect=True)
def test_positive_case(opened_file):
    assert read_magic_number(opened_file) is True


@pytest.mark.parametrize("opened_file", [
    '100\nBye, fellows\nis',
    '3\nLOTR',
    '-3\n',
    '0.999999',
    '1e4\n',
], indirect=True)
def test_negative_case(opened_file):
    assert read_magic_number(opened_file) is False


@pytest.mark.parametrize("opened_file", [
    '\nBye, fellows\nis',
    '2,1\nLOTR',
    '0.9.3\n',
    'python4.999999',
], indirect=True)
def test_with_error(opened_file):
    with pytest.raises(ValueError):
        read_magic_number(opened_file)


@pytest.mark.parametrize("opened_file", '\n', indirect=True)
def test_empty_file(opened_file):
    with pytest.raises(MagicNumberError):
        read_magic_number(opened_file)
