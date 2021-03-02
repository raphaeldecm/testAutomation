from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://www.google.com")
driver.find_element_by_name("q").send_keys("Raphael Muniz" + Keys.RETURN)
#driver.find_element_by_name("q").send_keys(Keys.RETURN)

driver.quit()