#!usr/bin/env python3
from pytest import raises


def raise_exception():
    raise ValueError


def test_1():
    with raises(ValueError):
        raise_exception()
