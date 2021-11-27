import pytest
from hw.task03 import make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly"
    }
]

blank_data = []


@pytest.mark.parametrize('data,keys,result', [
    (sample_data, {'name': 'Bill', 'type': 'person'}, sample_data[0]),
    (sample_data, {'name': 'polly', 'type': 'bird'}, sample_data[1]),
])
def test_positive_case(data, keys, result):
    output = make_filter(**keys).apply(data)[0]
    assert output == result


@pytest.mark.parametrize('data,keys', [
    (sample_data, {'name': 'Bill', 'type': 'bird'}),
    (sample_data, {'name': 'polly', 'type': 'person'}),
])
def test_negative_case(data, keys):
    assert make_filter(**keys).apply(data) == []


@pytest.mark.parametrize('keys', [
    ({'name': 'Bill', 'type': 'bird'}),
    ({'name': 'polly', 'type': 'person'}),
])
def test_no_data(keys):
    assert make_filter(**keys).apply([]) == []


@pytest.mark.parametrize('data', [
    sample_data,
    blank_data
])
def test_no_keys(data):
    assert make_filter().apply(data) == data


def test_blank_data():
    assert make_filter().apply(blank_data) == blank_data


@pytest.mark.parametrize('keys', [
    ({'name': 'Bill', 'type': 'bird'}),
    ({'name': 'polly', 'type': 'person'}),
])
def test_blank_data_with_keys(keys):
    assert make_filter(**keys).apply(blank_data) == blank_data
