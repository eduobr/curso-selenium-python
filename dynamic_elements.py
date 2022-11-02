import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from time import sleep

class DynamicElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        driver = self.driver
        driver.get("https://the-internet.herokuapp.com")

    def test_name_elements(self):
        driver = self.driver
        driver.find_element_by_link_text("Disappearing Elements").click()
        options = []
        menu = 5
        tries = 1

        while len(options) < 5:
            #por cada ciclo borramos el valor de la lista
            options.clear()

            for i in range(menu):
                try:
                    option_name = driver.find_element_by_xpath(f"/html/body/div[2]/div/div/ul/li[{i+1}]/a")
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"Option number {i+1} is NOT FOUND")
                    tries+1
                    driver.refresh()
        print(f"Fínished in {tries} tries")
    
    def test_dynamic_controls(self):
        driver = self.driver
        driver.find_element_by_link_text("Dynamic Controls").click()
        checkbox = driver.find_element_by_css_selector("#checkbox > input[type=checkbox]")
        checkbox.click()

        remove_add_button = driver.find_element_by_css_selector("#checkbox-example > button")
        remove_add_button.click()

        #debe volver a aparecer el checkbox
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkbox-example > button")))
        remove_add_button.click()

        enable_disable_button = driver.find_element_by_css_selector("#input-example > button")
        enable_disable_button.click()

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#input-example > button" )))

        text_area = driver.find_element_by_css_selector("#input-example > input[type=text]")
        text_area.send_keys("Platzi")

        enable_disable_button.click()

    def tearDown(self):
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main(verbosity=2)