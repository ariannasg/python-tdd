#!usr/bin/env python3
import pytest


@pytest.fixture(params=[1, 2, 3])
def setup_numbers(request):
    return request.param


def test_numbers(setup_numbers):
    print(f'Executing with: {setup_numbers}')
    assert True


testdata = [
    (1, 2),
    (2, 4),
    (3, 6),
]


@pytest.mark.parametrize("number,expected", testdata)
def test_multiplication(number, expected):
    result = number * 2
    assert result == expected


testdata2 = [
    (10, 2, 8),
    (10, 5, 5),
    (10, 6, 4),
]


@pytest.mark.parametrize("a,b,expected", testdata2)
def test_multiplication(a, b, expected):
    result = a - b
    assert result == expected