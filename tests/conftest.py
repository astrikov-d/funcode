# coding: utf-8
import pytest

from app.models import AppUser


@pytest.fixture()
def user():
    return AppUser.objects.get_or_create(email='john@doe.com', inn='1' * 10, balance=10)[0]


@pytest.fixture()
def receivers():
    return [
        AppUser.objects.get_or_create(email='receiver1@user.com', inn='2' * 10, balance=10)[0],
        AppUser.objects.get_or_create(email='receiver2@user.com', inn='3' * 10, balance=10)[0]
    ]
