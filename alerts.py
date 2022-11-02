import unittest
from selenium import webdriver
import time

class CompareProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver  = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
    
    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

        driver.find_element_by_class_name('link-compare').click()
        time.sleep(3)
        driver.find_element_by_link_text('Clear All').click()

        #cambia el focus al Alert
        alert = driver.switch_to.alert
        alert_text = alert.text
        time.sleep(3)

        
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)
        #presionamos el boton aceptar
        alert.accept()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)