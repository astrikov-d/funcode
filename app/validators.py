# coding: utf-8
def validate_inn(value):
    return len(value.replace(' ', '').replace('-', '')) == 10