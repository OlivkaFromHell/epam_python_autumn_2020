import pytest
from hw8.hw1 import KeyValueStorage


@pytest.fixture
def opened_file(request, tmpdir):
    file = tmpdir.join('test.txt')
    file.write(request.param)
    return file.strpath


@pytest.mark.parametrize("opened_file", [
    'name=kek\n'
    'last_name=top\n'
    'power=9001\n'
    'song_name=shadilay\n'
], indirect=True)
@pytest.mark.parametrize('key, value', [
    ('name', 'kek'),
    ('last_name', 'top'),
    ('power', 9001),
    ('song_name', 'shadilay'),
])
def test_accessible_as_collection(opened_file, key, value):
    storage = KeyValueStorage(opened_file)
    assert storage[key] == value


@pytest.mark.parametrize("opened_file", [
    'name=kek\n'
    'last_name=top\n'
    'power=9001\n'
    'song_name=shadilay\n'
], indirect=True)
@pytest.mark.parametrize('key, value', [
    ('name', 'kek'),
    ('last_name', 'top'),
    ('power', 9001),
    ('song_name', 'shadilay'),
])
def test_accessible_as_attribute(opened_file, key, value):
    storage = KeyValueStorage(opened_file)
    assert getattr(storage, key) == value


@pytest.mark.parametrize("opened_file", [
    '__doc__=kek\n'
    'items=top\n'
    'update=9001\n'
], indirect=True)
@pytest.mark.parametrize('key, value', [
    ('__doc__', 'kek'),
    ('items', 'top'),
    ('update', 9001),
])
def test_attribute_is_built_in(opened_file, key, value):
    storage = KeyValueStorage(opened_file)
    assert getattr(storage, key) != value


@pytest.mark.parametrize("opened_file", [
    '2=kek\n'
    '-3=top\n'
    'name value=9001\n'
    'sys-name=9001\n',
], indirect=True)
def test_key_is_digit(opened_file):
    with pytest.raises(ValueError):
        KeyValueStorage(opened_file)


@pytest.mark.parametrize("opened_file", [
    'keys=54\n'
    'items=MY_ITEMS\n',
], indirect=True)
def test_custom_case(opened_file):
    storage = KeyValueStorage(opened_file)
    assert getattr(storage, 'keys') != 54
