from selenium.webdriver.edge.webdriver import WebDriver
from PageObject.loginpage import Loginpage
class Test_login:
    def test_login_01(self, Setup):
        login_page = Loginpage(Setup)
        login_page.enterusername("standard_user")
        login_page.enterpassword("secret_sauce")
        login_page.loginbutton()

    def test_login_02(self, Setup):
        login_page = Loginpage(Setup)
        login_page.enterusername("standard_user")
        login_page.enterpassword("secret_sauc")
        login_page.loginbutton()
        Error_message = login_page.geterrormessage()
        expected_message = "Epic sadface: Username and password do not match any user in this service"
        assert Error_message == expected_message
        print(Error_message)