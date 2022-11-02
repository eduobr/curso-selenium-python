import unittest
from ddt import ddt, data, unpack
from selenium import webdriver

@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")

    #tuplas con los terminos que vamos a buscar y la cantidad que esperamos como resultado
    @data(('dress',5), ('music',5))
    @unpack #desenpaquetamos las tuplas y puedan ser consultadas de forma individual
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        #obtenemos los productos buscados
        products = driver.find_elements_by_xpath('//h2[@class= "product-name"]/a')
        print(f'Found {len(products)} products')

        for product in products:
            print(product.text)

        self.assertEqual(expected_count, len(products))

        

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
