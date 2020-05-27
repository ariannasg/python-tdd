#!usr/bin/env python3


def setup_function(function):
    if function == test1:
        print('Setting up test1!')
    elif function == test2:
        print('Setting up test2!')


def teardown_function(function):
    if function == test1:
        print('Tearing down test1!')
    elif function == test2:
        print('Tearing down test2!')


def test1():
    print('Executing test1')
    assert True


def test2():
    print('Executing test2')
    assert True
