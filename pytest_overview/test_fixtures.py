#!usr/bin/env python3
import pytest


@pytest.fixture()
def setup():
    print('Fixture setup')


@pytest.fixture()
def setup2():
    print('Fixture setup2')


@pytest.fixture(autouse=True)
def setup3():
    print('Fixture setup3')


@pytest.mark.usefixtures('setup', 'setup2')
def test_fixture_1():
    print('Executing test_fixture_1')
    assert True


def test_fixture_2(setup):
    print('Executing test_fixture_2')
    assert True
