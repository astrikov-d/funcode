# coding: utf-8
import pytest

from app.models import AppUser
from app.views import HomepageView


@pytest.mark.django_db()
def test_payments(user, receivers):
    view = HomepageView()

    data = {
        'user': user,
        'amount': 5,
        'receivers': [receiver.inn for receiver in receivers]
    }

    view.process_data(data)

    assert AppUser.objects.get(pk=user.pk).balance == 5

    for receiver in receivers:
        assert AppUser.objects.get(pk=receiver.pk).balance == 12.5

    data['receivers'] = []

    view.process_data(data)
    assert AppUser.objects.get(pk=user.pk).balance == 5
