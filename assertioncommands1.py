import unittest
from selenium import webdriver

class asserttest(unittest.TestCase):

    def test_assert(self):
        self.driver=webdriver.Chrome(executable_path="C:\selenium\drivers\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        titleofgoogle=self.driver.title
        print(titleofgoogle)
        #self.assertEqual("Google123",titleofgoogle,"both are not equal so failed")
        self.assertNotEqual("Google123",titleofgoogle)

if __name__ == '__main__':
    unittest.main()