#!usr/bin/env python3


class TestClass:
    # the decorator is used for passing the un-instantiated class object rather than a unique instance of the class
    @classmethod
    def setup_class(cls):
        print('Setup TestClass')

    @classmethod
    def teardown_class(cls):
        print('Teardown TestClass')

    def setup_method(self, method):
        if method == self.test1:
            print('Setting up test1 in TestClass!')
        elif method == self.test2:
            print('Setting up test2 in TestClass!')

    def teardown_method(self, method):
        if method == self.test1:
            print('Tearing down test1 in TestClass!')
        elif method == self.test2:
            print('Tearing down test2 in TestClass!')

    def test1(self):
        print('Executing test1 in TestClass')
        assert True

    def test2(self):
        print('Executing test2 in TestClass')
        assert True
