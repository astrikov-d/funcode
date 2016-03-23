# coding: utf-8
from app.classes import Keeper


def test_weakref():
    for i in (1, 2):
        Keeper()

    assert Keeper.get_instances()
    assert len(Keeper.get_instances()) == 2
