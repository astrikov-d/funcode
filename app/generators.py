# coding: utf-8


class reverse_gen(object):

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 1
        self.count = len(iterable)

    def __iter__(self):
        return self

    def next(self):
        if self.index <= self.count:
            current, self.index = self.iterable[-self.index], self.index + 1
            return current
        raise StopIteration
