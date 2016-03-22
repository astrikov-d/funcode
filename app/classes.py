# coding: utf-8
import weakref


class Keeper(object):
    instances = []

    def __init__(self):
        self.__class__.instances.append(weakref.proxy(self))

    @classmethod
    def get_instances(cls):
        return cls.instances
