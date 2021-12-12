import pytest
from hw.task_3_get_print_output import my_precious_logger


@pytest.mark.parametrize('msg', [
    'OK',
    'ERROR: invalid data',
    'Passed'
])
def test_positive_stdout_case(msg, capsys):
    my_precious_logger(msg)
    out, err = capsys.readouterr()
    assert out == msg
    assert err == ''


@pytest.mark.parametrize('msg', [
    'error: invalid data',
    'error: stack overflow',
    'error',
])
def test_positive_stderr_case(msg, capsys):
    my_precious_logger(msg)
    out, err = capsys.readouterr()
    assert out == ''
    assert err == msg


def test_blank_input(capsys):
    my_precious_logger('')
    out, err = capsys.readouterr()
    assert out == ''
    assert err == ''


@pytest.mark.parametrize('msg', [
    'ERROR: invalid data',
    'Error: stack overflow',
    'ErROr',
])
def test_error_upper_case(msg, capsys):
    my_precious_logger(msg)
    out, err = capsys.readouterr()
    assert out == msg
    assert err == ''
