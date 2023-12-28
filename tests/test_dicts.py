import pytest
from utils.dicts import get_val


def test_get_val():
    assert get_val({1: 3, "a": "hello", 3: True}, 1, ), 3
    assert get_val({1: 3, "a": "hello", 3: True}, key=False), 'git'
    assert get_val({1: 3, "a": "hello", 3: True}, key=3), True

