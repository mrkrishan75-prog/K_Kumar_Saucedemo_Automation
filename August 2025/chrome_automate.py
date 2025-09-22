from selenium import webdriver
driver_path = "driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()
driver.get("https://www.soucedemo.com")
driver.find_element_by_id("user-name").send_keys("standard_user")
driver.find_element_by_id("password").send_keys("secret_sauce")
driver.find_element_by_id("login-button").click()
driver.find_element_by_id("add-to-cart-sauce-labs-backpack").click()
driver.find_element_by_class_name("shopping_cart_badge").click()
driver.find_elements_by_class_name("search_query").send_keys("Babbu maan songs")
driver.find_element_by_xpath("//*[@id='center']/yt-searchbox/button/span/span/div").click()