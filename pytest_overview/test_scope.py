#!usr/bin/env python3
import pytest


@pytest.fixture(scope='session', autouse=True)
def setup_session():
    print('\n ===>>> Session module')


@pytest.fixture(scope='module', autouse=True)
def setup_module():
    print('\n ===>>> Setup module')


@pytest.fixture(scope='function', autouse=True)
def setup_function():
    print('\n ===>>> Setup function')


@pytest.fixture(scope='class', autouse=True)
def setup_class():
    print('\n ===>>> Setup class')


def test_1():
    print('Executing test 1')
    assert True


def test_2():
    print('Executing test 2')
    assert True


class TestClass:
    def test_1(self):
        print('Executing test class 1')
        assert True

    def test_2(self):
        print('Executing test class 2')
        assert True
