import unittest

class TC_login(unittest.TestCase):

    def test_gmail(self):
        print("This is gmail login")
        self.assertTrue(True)

    def test_facebook(self):
        print("This is facebook login")
        self.assertTrue(True)

    def test_Twitter(self):
        print("This is Twitter login")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()