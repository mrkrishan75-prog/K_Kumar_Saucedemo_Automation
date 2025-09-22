from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyttsx3
import time

driver_path = "driver\msedgedriver.exe"
driver = webdriver.Edge(executable_path=driver_path)
driver.maximize_window()
driver.get("file:///E:/Automation%20Testing/August%202025/locators/Practice%20Website/Practice.html")


# driver.find_element_by_class_name("inputs").send_keys("krishan")
# driver.find_element_by_link_text("Click to visit youtube").click()
# driver.find_element_by_partial_link_text("youtube").click()


# driver.find_element_by_xpath("//input[@placeholder='Enter Your Name']").send_keys("krishan")
engine=pyttsx3.init()

# text = driver.find_element_by_xpath("//fieldset[@class='pull-right']/legend").text
# print(text)
# engine.say(text)
# engine.runAndWait()
# text = driver.find_element_by_xpath('//*[@id="checkbox-example"]/fieldset/legend').text
# print(text)
# engine.say(text)
# engine.runAndWait()

# checkboxes=driver.find_elements_by_xpath("//input[@type='checkbox']")
# for checkboxe in checkboxes:
#     checkboxe.click()


# dropdown=Select(driver.find_element_by_id("dropdown-class-example"))
# dropdown.select_by_index(2)
# dropdown.select_by_value("option1")
# dropdown.select_by_visible_text("Option3")


driver.find_element_by_id("name").send_keys("krishan")
driver.find_element_by_id("alertbtn").click()
popup=driver.switch_to_alert()
time.sleep(0.5)
print(popup.text)
engine.say(popup.text)
popup.dismiss()
engine.runAndWait()