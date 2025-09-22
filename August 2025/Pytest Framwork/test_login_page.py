import time
from selenium import webdriver
import pytest
import pyttsx3
from selenium.webdriver.edge.webdriver import WebDriver




class Test_login():
    def test_login_01(self, Setup: WebDriver):
        self.driver = Setup
        driver = self.driver
        driver.find_element_by_id("user-name").send_keys("standard_user")
        driver.find_element_by_id("password").send_keys("secret_sauce")
        driver.find_element_by_id("login-button").click()
        actual_text = driver.find_element_by_xpath('//span[@class="title"]').text
        print(actual_text)
        engine=pyttsx3.init()
        engine.say(actual_text)
        engine.runAndWait()
        expected_text = "Products"
        assert actual_text == expected_text



    def test_login_02(self, Setup: WebDriver):
        self.driver = Setup
        driver = self.driver
        engine=pyttsx3.init()
        driver.find_element_by_id("user-name").send_keys("standard_user")
        driver.find_element_by_id("password").send_keys("secret")
        driver.find_element_by_id("login-button").click()
        error = driver.find_element_by_xpath('//*[@id="login_button_container"]/div/form/div[3]/h3').text
        print(error)
        engine.say(error)
        engine.runAndWait()


    def test_login_03(self, Setup: WebDriver):
        self.driver = Setup
        driver = self.driver
        driver.find_element_by_id("user-name").send_keys("standard")
        driver.find_element_by_id("password").send_keys("secret_sauce")
        driver.find_element_by_id("login-button").click()
        error = driver.find_element_by_xpath('//*[@id="login_button_container"]/div/form/div[3]/h3').text
        print(error)
        engine=pyttsx3.init()
        engine.say(error)
        engine.runAndWait()
