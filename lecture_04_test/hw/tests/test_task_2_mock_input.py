from unittest import mock

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

        return FakeResponse()

    with mock.patch('requests.get', new=fake_get):
        assert count_dots_on_i('https://vk.com/') == 0


def test_negative_case2():
    def fake_get(url='https://vk.com/', *args, **kwargs):
        class FakeResponse:
            text = """<!DOCTYPE html>
                <html>
                <body>

                <h1>Hello, World!</h1>

                </body>
                </html>"""

        return FakeResponse()

    with mock.patch('requests.get', new=fake_get):
        assert not count_dots_on_i('https://vk.com/') != 0
