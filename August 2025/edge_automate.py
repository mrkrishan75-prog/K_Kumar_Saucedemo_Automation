from selenium import webdriver
driver_path = "driver\msedgedriver.exe"
driver = webdriver.Edge(executable_path=driver_path)
driver.maximize_window()
driver.get("https://www.saucedemo.com")
driver.find_element_by_id("user-name").send_keys("standard_user")
driver.find_element_by_id("password").send_keys("secret_sauce")
driver.find_element_by_id("login-button").click()
driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
driver.find_element_by_class_name("shopping_cart_badge").click()
driver.find_element_by_id("checkout").click()
driver.find_element_by_id("first-name").send_keys("Krishan")
driver.find_element_by_id("last-name").send_keys("Kumar")
driver.find_element_by_id("postal-code").send_keys("122001")
driver.find_element_by_id("continue").click()
driver.find_element_by_id("finish").click()
driver.find_element_by_id("back-to-products").click()
driver.find_element_by_id("react-burger-menu-btn").click()
driver.find_element_by_xpath("//*[@id='react-burger-cross-btn']").click()
driver.find_element_by_css_selector("#react-burger-cross-btn").click()



