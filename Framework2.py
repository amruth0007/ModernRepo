import unittest


def setUpModule():
    print("This is before Class")


def tearDownModule():
    print("This is after class")

class Hemraj(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This is before all method")

    @classmethod
    def tearDownClass(cls):
        print("this is after all method")

    @classmethod
    def setUp(self):
        print("This is login before:")

    @classmethod
    def tearDown(self):
        print("This is logout after")

    def test_Test1(self):
        print("this is test case1")

    def test_Test2(self):
        print("This is test case2")

    def test_Test3(self):
        print("This is test case3")

    def test_Test4(self):
        print("this is test case 4")

    def test_Test5(self):
        print("This is test case 5")

if __name__ == "__main__":
    unittest.main()