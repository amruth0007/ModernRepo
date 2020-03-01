import unittest
from selenium import webdriver

class assertTest(unittest.TestCase):

    def test_assert(self):
        self.driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        googletitle=self.driver.title
        #self.assertTrue(googletitle=='Google')
        self.assertFalse(googletitle=='Google123')

if __name__ == '__main__':
    unittest.main()