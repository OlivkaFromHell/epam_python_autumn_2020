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


@pytest.mark.parametrize('data,keys,result', [
    (sample_data, {'name': 'Bill', 'type': 'person'}, sample_data[0]),
    (sample_data, {'name': 'polly', 'type': 'bird'}, sample_data[1]),
])
def test_positive_case(data, keys, result):
    output = make_filter(**keys).apply(data)[0]
    assert output == result
