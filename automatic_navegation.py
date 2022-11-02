import unittest
from selenium import webdriver
import time

class NavigationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver  = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://www.google.com/')

    def test_browser_navigation(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('platzi')
        time.sleep(3)
        search_field.submit()

        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)
        driver.refresh()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)