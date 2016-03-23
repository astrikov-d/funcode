# coding: utf-8
def clean_inn(value):
    return str(value).replace('-', '').replace(' ', '').strip()
