import logging

import pytest
from hw.task_3_get_print_output import my_precious_logger


@pytest.mark.parametrize('msg', [
    'OK',
    'ERROR: invalid data',
    'Passed'
])
def test_positive_stdout_case(msg, caplog):
    caplog.set_level(logging.INFO)
    my_precious_logger(msg)
    for record in caplog.records:
        assert record.levelname == "INFO"


@pytest.mark.parametrize('msg', [
    'error: invalid data',
    'error: stack overflow',
    'error',
])
def test_positive_stderr_case(msg, caplog):
    caplog.set_level(logging.INFO)
    my_precious_logger(msg)
    for record in caplog.records:
        assert record.levelname == "ERROR"


def test_blank_input(caplog):
    caplog.set_level(logging.INFO)
    my_precious_logger('')
    for record in caplog.records:
        assert record.levelname == "INFO"


@pytest.mark.parametrize('msg', [
    'ERROR: invalid data',
    'Error: stack overflow',
    'ErROr',
])
def test_error_upper_case(msg, caplog):
    caplog.set_level(logging.INFO)
    my_precious_logger(msg)
    for record in caplog.records:
        assert record.levelname == "INFO"
