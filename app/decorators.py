# coding: utf-8
import json

from hashlib import md5


class Cache(object):
    __cache = {}
    __slots__ = '__cache',

    @classmethod
    def get(cls, key):
        return cls.__cache[key]

    @classmethod
    def set(cls, key, value):
        cls.__cache[key] = value

    @classmethod
    def has(cls, key):
        return key in cls.__cache


CACHE = Cache()


class CacheDecorator(object):
    def __init__(self, func):
        self.func = func

    @staticmethod
    def construct_cache_key(*func_args):
        m = md5()
        m.update(json.dumps(func_args))
        return m.digest()

    def __call__(self, *args, **kwargs):
        key = self.construct_cache_key(*args)
        if CACHE.has(key):
            return CACHE.get(key)
        result = self.func(*args, **kwargs)
        CACHE.set(key, result)
        return result


def cache_decorator(func):
    def wrapped(*args, **kwargs):
        cache = CacheDecorator(func)
        return cache(*args, **kwargs)

    return wrapped