#!usr/bin/env python3
from pytest import approx


def test_floats():
    assert not (0.1 + 0.2) == 0.3


def test_floats2():
    assert (0.1 + 0.2) == approx(0.3)
