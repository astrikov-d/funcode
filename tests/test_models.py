# coding: utf-8
import pytest


@pytest.mark.django_db()
def test_app_user(user):
    user.balance = 10000
    user.save(update_fields=['balance'])

    assert not user.can_be_charged(20000)
    assert user.can_be_charged(10000)
    assert user.can_be_charged(1000)

    result = user.change_balance(5000)
    assert user.balance == 15000
    assert result == 15000

    result = user.change_balance(-30000)
    assert result is None
    assert user.balance == 15000

    user.change_balance(10.5)
    assert user.balance == 15010.5