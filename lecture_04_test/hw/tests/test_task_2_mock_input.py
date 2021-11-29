from unittest import mock

import pytest
from hw.task_2_mock_input import count_dots_on_i


def test_positive_case1():
    def fake_get(url='https://vk.com/', *args, **kwargs):
        class FakeResponse:
            text = """<!DOCTYPE html>
                <html>
                <body>
                <h1>My First Heading</h1>
                <p>My first paragraph.</p>
                </body>
                </html>"""
            status_code = 200

        return FakeResponse()

    with mock.patch('requests.get', new=fake_get):
        assert count_dots_on_i('https://vk.com/') == 3


def test_positive_case2():
    def fake_get(url='https://vk.com/', *args, **kwargs):
        class FakeResponse:
            text = """<!DOCTYPE html>
                <html>
                <body>
                <h1>Hello, World!</h1>
                </body>
                </html>"""
            status_code = 200

        return FakeResponse()

    with mock.patch('requests.get', new=fake_get):
        assert count_dots_on_i('https://vk.com/') == 0


def test_negative_case():
    def fake_get(url='https://vk.com/', *args, **kwargs):
        class FakeResponse:
            text = """<!DOCTYPE html>
                <html>
                <body>

                <h1>Hello, World!</h1>

                </body>
                </html>"""
            status_code = 200

        return FakeResponse()

    with mock.patch('requests.get', new=fake_get):
        assert not count_dots_on_i('https://vk.com/') != 0


def test_unvalid_url():
    def fake_get(url='https://com.vk/', *args, **kwargs):
        class FakeResponse:
            text = """<!DOCTYPE html>
                <html>
                <body>

                <h1>Hello, World!</h1>

                </body>
                </html>"""
            status_code = 400

        return FakeResponse()

    with pytest.raises(Exception):
        with mock.patch('requests.get', new=fake_get):
            count_dots_on_i('https://com.vk/')
