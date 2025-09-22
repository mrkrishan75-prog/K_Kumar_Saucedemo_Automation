class Loginpage:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_id = "user-name"
        self.password_textbox_id = "password"
        self.login_button_id = "login-button"
        self.errormessage_xpath = "//h3[@data-test='error']"
    

    def enterusername(self, name):
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(name)

    def enterpassword(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def loginbutton(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def geterrormessage(self):
        Error_message = self.driver.find_element_by_xpath(self.errormessage_xpath).text
        print(Error_message)
        return Error_message
    
    def login(self, name, password):
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(name)
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
        self.driver.find_element_by_id(self.login_button_id).click()