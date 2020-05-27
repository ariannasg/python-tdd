#!usr/bin/env python3
import pytest


def raise_exception():
    raise ValueError


def test_1():
    with pytest.raises(ValueError):
        raise_exception()


@pytest.mark.skip
def test_2():
    with pytest.raises(ValueError):
        raise_exception()
