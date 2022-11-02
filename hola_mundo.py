import unittest;
#orquestar las pruebas juntos con los reportes
from pyunitreport import HTMLTestRunner;
#comunicarnos con el navegador
from selenium import webdriver;

#Hacen referencía a unittest.TestCase que seran nuestros casos de prueba
class HelloWorld(unittest.TestCase):
    @classmethod #Decorador para correr las pruebas en una ventana
    def setUpClass(cls): #prepara el entorno de la prueba
        #conectamos con nuestro webdriver
        cls.driver = webdriver.Chrome(executable_path=r'D:\\Respaldo\\curso-selenium\\chromedriver.exe')
        #return super().setUp()
        driver = cls.driver
        #esperar 10 segundos para realizar la siguiente acción
        driver.implicitly_wait(10)

    #caso de prueba donde realizaremos una serie de pruebas para que el navegador las automatice
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_visit_wikipedia(self):
        self.driver.get('https://www.wikipedia.org')

    @classmethod
    def tearDownClass(cls): #se ejecuta al finalizar la prueba
        #cierra la ventana y todas sus pestañas
        cls.driver.quit()
        #return super().tearDown()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='hola-mundo-report'))