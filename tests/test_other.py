# coding: utf-8
import pytest

from itertools import product


def test_other():
    def myappend(a=[], num=0):
        a.append(num)
        return a

    a = [1, 2, 3]
    assert myappend(a) == [1, 2, 3, 0]
    assert myappend() == [0]
    assert myappend() == [0, 0]


@pytest.mark.parametrize('value, expected', [
    ('1.2.3', ['1.2.3', '1.2 3', '1 2.3', '1 2 3']),
    ('1.2.3.4.5.6',
     ['1.2.3.4.5.6', '1.2.3.4.5 6', '1.2.3.4 5.6', '1.2.3.4 5 6', '1.2.3 4.5.6', '1.2.3 4.5 6', '1.2.3 4 5.6',
      '1.2.3 4 5 6', '1.2 3.4.5.6', '1.2 3.4.5 6', '1.2 3.4 5.6', '1.2 3.4 5 6', '1.2 3 4.5.6', '1.2 3 4.5 6',
      '1.2 3 4 5.6', '1.2 3 4 5 6', '1 2.3.4.5.6', '1 2.3.4.5 6', '1 2.3.4 5.6', '1 2.3.4 5 6', '1 2.3 4.5.6',
      '1 2.3 4.5 6', '1 2.3 4 5.6', '1 2.3 4 5 6', '1 2 3.4.5.6', '1 2 3.4.5 6', '1 2 3.4 5.6', '1 2 3.4 5 6',
      '1 2 3 4.5.6', '1 2 3 4.5 6', '1 2 3 4 5.6', '1 2 3 4 5 6']),
])
def test_product(value, expected):
    def filler(word, from_char, to_char):
        options = [(c,) if c != from_char else (from_char, to_char) for c in word]
        return (''.join(o) for o in product(*options))

    assert list(filler(value, ".", ' ')) == expected