import unittest
from selenium import webdriver

class RegisterUserTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        #hacemos click en el elemento del menú desplegable
        driver.find_element_by_link_text('Log In').click()

        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        #verificamos si el boton está desplegado y esté habilidato(el usuario puede interactuar con el)
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        #comprobamos si el texto es igual al titulo de la pestaña de nuestro driver
        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        sumbit_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button')

        self.assertTrue(first_name.is_enabled()
        and middle_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_subscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and sumbit_button.is_enabled())

        first_name.send_keys('Test')
        driver.implicitly_wait(3)
        middle_name.send_keys('Test')
        driver.implicitly_wait(3)
        last_name.send_keys('Test')
        driver.implicitly_wait(3)
        email_address.send_keys('Test@gmail.com')
        driver.implicitly_wait(3)
        password.send_keys('Test')
        driver.implicitly_wait(3)
        confirm_password.send_keys('Test')
        driver.implicitly_wait(3)
        sumbit_button.send_keys('Test')
        
        sumbit_button.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)

    