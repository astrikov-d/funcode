# coding: utf-8
from app.decorators import cache_decorator, Cache


def test_cache():
    cache = Cache()
    cache.set('key', 'value')
    value = cache.get('key')
    assert value == 'value'
    assert cache.has('key')


def test_cache_decorator(mocker):
    @cache_decorator
    def get_long_response(user_id):
        return user_id * 1000

    mocker.spy(Cache, 'has')
    mocker.spy(Cache, 'get')
    mocker.spy(Cache, 'set')

    get_long_response(100)
    assert Cache.has.call_count == 1
    assert Cache.get.call_count == 0
    assert Cache.set.call_count == 1

    get_long_response(100)
    assert Cache.has.call_count == 2
    assert Cache.get.call_count == 1
    assert Cache.set.call_count == 1

    get_long_response(50)
    assert Cache.has.call_count == 3
    assert Cache.get.call_count == 1
    assert Cache.set.call_count == 2