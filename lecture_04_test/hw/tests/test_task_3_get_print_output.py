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
    assert out == msg + '\n'
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
    assert err == msg + '\n'


@pytest.mark.parametrize('msg', [
    'error: invalid data',
    'error: stack overflow',
    'error',
])
def test_negative_case(msg, capsys):
    my_precious_logger(msg)
    out, err = capsys.readouterr()
    assert out != msg + '\n'
    assert err != ''
