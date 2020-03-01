import unittest

class Hemraj(unittest.TestCase):

    @unittest.skip("I will run this test case later so stopped Test1")
    def test_Test1(self):
        print("this is test case1")

    @unittest.SkipTest
    def test_Test2(self):
        print("This is test case2")

    @unittest.skipIf(1==1,"Skipped as 1 equal to 1")
    def test_Test3(self):
        print("This is test case3")

    def test_Test4(self):
        print("this is test case 4")

    def test_Test5(self):
        print("This is test case 5")

if __name__== "__main__":
    unittest.main()