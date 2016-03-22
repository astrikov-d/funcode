# coding: utf-8
import pytest

from app.generators import reverse_gen


@pytest.mark.parametrize('iterable', [
    ([1, 2, 3, 4],),
    ((1, 2, 3, 4),),
    ('some string',),
])
def test_reverse_gen(iterable):
    generator = reverse_gen(iterable)

    for index in xrange(1, len(iterable) + 1):
        if index < len(iterable) + 1:
            item = generator.next()
            assert item == iterable[-index]
        else:
            with pytest.raises(StopIteration):
                generator.next()
