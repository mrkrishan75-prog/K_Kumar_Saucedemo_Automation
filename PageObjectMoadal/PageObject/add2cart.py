class AddToCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.add2cart_button_1_id = "add-to-cart-sauce-labs-backpack"
        self.add2cart_button_2_id = "add-to-cart-sauce-labs-bike-light"
        self.cart_icon_id = "shopping_cart_container"



    def click_add2cart_1(self):
        self.driver.find_element_by_id(self.add2cart_button_1_id).click()

    def click_add2cart_2(self):
        self.driver.find_element_by_id(self.add2cart_button_2_id).click()

    def view_cart(self):
        self.driver.find_element_by_class_name("shopping_cart_link").click()

    def message_card(self):
        cart = self.driver.find_element_by_xpath("//span[@class='title']").text
        print(cart)
        return cart
        time.sleep(2)

    def remove_item(self):
        self.driver.find_element_by_id("remove-sauce-labs-backpack").click()
        self.driver.find_element_by_id("remove-sauce-labs-bike-light").click()
        self.driver.find_element_by_id("continue-shopping").click()
        homepage = self.driver.find_element_by_xpath("//div[@class='app_logo']").text
        print(homepage)
        return homepage
        time.sleep(2)
        
    def number_of_items(self):
        numbers = self.driver.find_element_by_xpath("//span[@class='shopping_cart_badge']").text
        print(numbers)
        return numbers
        time.sleep(2)
