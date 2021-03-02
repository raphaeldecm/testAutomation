import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Exemplo(unittest.TestCase):
    
    ## Setup
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.google.com")

    def test_abrir_pagina(self):
        assert "Google" in self.driver.title, "O Teste falhou."
    
    def test_buscar_enter(self):
        element = self.driver.find_element_by_name("q")
        element.send_keys("Raphael Muniz")
        element.send_keys(Keys.RETURN)
        assert "Muniz" in self.driver.page_source, "O Teste falou."

    ## TearDown
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()