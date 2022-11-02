import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class LanguageOptionsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='./chromedriver.exe')
        driver  = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
    
    def test_select_language(self):
        exposed_options = ['English', 'French','German']
        actived_options = []
        
        select_language = Select(self.driver.find_element_by_id('select-language'))
        self.assertEqual(3, len(select_language.options))

        for option in select_language.options:
            actived_options.append(option.text)
        
        #comprobamos si son identicas
        self.assertEqual(exposed_options, actived_options)

        #comprobamos si la opción por defecto es igual a Ingles
        self.assertEqual('English', select_language.first_selected_option.text)

        select_language.select_by_visible_text('German')

        #validamos que aparezcan esos parametros en la url
        self.assertTrue('store=german' in self.driver.current_url)

        select_language = Select(self.driver.find_element_by_id('select-language'))

        #elegimos el idioma por su indice
        select_language.select_by_index(0)

        self.driver.implicitly_wait(30)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)