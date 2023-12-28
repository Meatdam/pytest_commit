import pytest
from utils.dicts import get_val


@pytest.mark.parametrize('collection, key, default', [
    ({1: 3, "a": "hello", 3: True}, 1, 3),
    ({1: 3, "a": "hello", 3: True}, False, 'git'),
    ({1: 3, "a": "hello", 3: True}, 3, True)
])
def test_get_val(collection, key, default):
    assert get_val(collection, key, default)
