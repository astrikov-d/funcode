# coding: utf-8
import pytest

from app.validators import validate_inn


@pytest.mark.parametrize('value, valid', [
    (None, False),
    ('1234567890', True),
    (1234567890, True),
    (12345, False),
    ('a' * 10, False)
])
def test_validate_inn(value, valid):
    assert validate_inn(value) == valid
