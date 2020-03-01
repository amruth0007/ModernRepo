import unittest
from selenium import webdriver

class assertcommand(unittest.TestCase):

    def test_assert(self):
        #self.driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
        self.driver=None
        #self.assertIsNone(self.driver)

        self.assertIsNotNone(self.driver)

if __name__ == "__main__":
    unittest.main()
