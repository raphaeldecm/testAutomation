import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Exemplo(unittest.TestCase):
    
    ## Setup
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.google.com")

    def test_abrir_pagina(self):
        

    ## TearDown
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()