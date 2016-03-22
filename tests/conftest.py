# coding: utf-8
import pytest

from app.models import AppUser


@pytest.fixture()
def user():
    return AppUser.objects.get_or_create(email='john@doe.com')[0]