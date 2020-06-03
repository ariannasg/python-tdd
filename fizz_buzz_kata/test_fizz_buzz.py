#!usr/bin/env python3
import pytest


def fizz_buzz(value):
    if is_multiple(value, 3):
        if is_multiple(value, 5):
            return "Fizz_buzz"
        return "Fizz"
    if is_multiple(value, 5):
        return "Buzz"
    return str(value)


def is_multiple(value, mod):
    return (value % mod) == 0


fizz_buzz_test_data = [
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (5, "Buzz"),
    (6, "Fizz"),
    (10, "Buzz"),
    (15, "Fizz_buzz"),
]


@pytest.mark.parametrize("number,expected_output", fizz_buzz_test_data)
def test_multiplication(number, expected_output):
    result = fizz_buzz(number)
    assert result == expected_output
