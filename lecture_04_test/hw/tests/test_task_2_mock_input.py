from unittest import mock

import pytest
from hw.task_2_mock_input import count_dots_on_i

text_positive_case_1 = '<!DOCTYPE html>\n' \
                       '<html>\n' \
                       '<body>\n' \
                       '<h1>My First Heading</h1>\n' \
                       '<p>My first paragraph.</p>\n' \
                       '</body>\n' \
                       '</html>\n'

text_positive_case_2 = '<!DOCTYPE html>\n' \
                       '<html>\n' \
                       '<body>\n' \
                       '<h1>Hello, World!</h1>\n' \
                       '</body>\n' \
                       '</html>\n'


def test_positive_case1():
    def fake_get(url='https://vk.com/', *args, **kwargs):
        class FakeResponse:
            text = text_positive_case_1
            status_code = 200

        return FakeResponse()

    with mock.patch('requests.get', new=fake_get):
        assert count_dots_on_i('https://vk.com/') == 3


def test_positive_case2():
    def fake_get(url='https://vk.com/', *args, **kwargs):
        class FakeResponse:
            text = text_positive_case_2
            status_code = 200

        return FakeResponse()

    with mock.patch('requests.get', new=fake_get):
        assert count_dots_on_i('https://vk.com/') == 0


def test_negative_case():
    def fake_get(url='https://vk.com/', *args, **kwargs):
        class FakeResponse:
            text = text_positive_case_2
            status_code = 200

        return FakeResponse()

    with mock.patch('requests.get', new=fake_get):
        assert not count_dots_on_i('https://vk.com/') != 0


def test_unvalid_url():
    def fake_get(url='https://com.vk/', *args, **kwargs):
        class FakeResponse:
            text = ''
            status_code = 400

        return FakeResponse()

    with pytest.raises(Exception):
        with mock.patch('requests.get', new=fake_get):
            count_dots_on_i('https://com.vk/')
