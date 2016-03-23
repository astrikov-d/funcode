# coding: utf-8
from .helpers import clean_inn


def validate_inn(value):
    cleaned = clean_inn(value)
    return cleaned.isdigit() and len(cleaned) == 10
