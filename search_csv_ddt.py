import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver

def get_data(file_name):
    rows = []
    #obtenemos el archivo en modo lectura
    data_file = open(file_name, 'r')
    #la libreria csv se va a encargar de leer el archivo
    reader = csv.reader(data_file)
    #pase a la siguiente linea de datos omitiendo la cabecera
    next(reader, None)

    for row in reader:
        #la fila en reader se va agregar a la lista de filas
        rows.append(row)
    
    return rows

@ddt
class SearchCsvDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")

    #tuplas con los terminos que vamos a buscar y la cantidad que esperamos como resultado
    #@data(('dress',5), ('music',5))

    #ya no pasamos una tupla sino una funcíon para obtener los datos
    @data(*get_data('testdata.csv'))

    @unpack #desenpaquetamos las tuplas y puedan ser consultadas de forma individual
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        #obtenemos los productos buscados
        products = driver.find_elements_by_xpath('//h2[@class= "product-name"]/a')

        expected_count = int(expected_count)
        
        if expected_count > 0:
            self.assertEqual(expected_count, len(products))
        else:
            message = driver.find_element_by_class_name('note-msg')
            self.assertEqual('Your search returns no results.', message)
        
        print(f'Found {len(products)} products')
        
        #print(f'Found {len(products)} products')

        #for product in products:
        #    print(product.text)

        #self.assertEqual(expected_count, len(products))

        

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)
