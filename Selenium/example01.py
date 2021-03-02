import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Exemplo(unittest.TestCase):
    
    ## Setup
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_abrir_pagina(self):
        self.driver.get("http://www.google.com")
        assert "Google" in self.driver.title, "O Teste falhou."

    ## TearDown
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()