#!usr/bin/env python3
import pytest


@pytest.fixture(params=[1, 2, 3])
def setup_numbers(request):
    return request.param


def test_numbers(setup_numbers):
    print(f'Executing with: {setup_numbers}')
    assert True
