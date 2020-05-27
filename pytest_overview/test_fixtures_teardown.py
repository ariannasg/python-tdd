#!usr/bin/env python3
import pytest


@pytest.fixture()
def setup1():
    print('\nFixture setup 1')
    yield
    print('Fixture teardown 1')


@pytest.fixture()
def setup2(request):
    print('\nFixture setup 2')

    def teardown_a():
        print('Fixture teardown a')

    def teardown_b():
        print('Fixture teardown b')

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)


def test_fixture_1(setup1):
    print('Executing test_fixture_teardown_1')
    assert True


def test_fixture_2(setup2):
    print('Executing test_fixture_teardown_2')
    assert True
