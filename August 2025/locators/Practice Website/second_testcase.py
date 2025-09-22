from selenium import webdriver
import pytest
import time


driver_path = "driver\\msedgedriver.exe"
driver = webdriver.Edge(executable_path=driver_path)
driver.maximize_window()
driver.get("https://www.saucedemo.com")
time.sleep(3)

driver.find_element_by_id("user-name").send_keys("standard_user")
driver.find_element_by_id("password").send_keys("secret_sauce")
driver.find_element_by_id("login-button").click()
actual_text = driver.find_element_by_xpath('//span[@class="title"]').text
print(actual_text)
expected_text = "Products"
assert actual_text == expected_text
driver.quit()
