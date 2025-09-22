from selenium.webdriver.edge.webdriver import WebDriver
from PageObject.loginpage import Loginpage
from PageObject.add2cart import AddToCartPage
import time

class Test_AddToCart:
    def test_addtocart_01(self, Setup: WebDriver):
        login_page = Loginpage(Setup)
        add2cart_page = AddToCartPage(Setup)
        login_page.login("standard_user", "secret_sauce")
        add2cart_page.click_add2cart_1()
        add2cart_page.click_add2cart_2()
        add2cart_page.view_cart()


    def test_addtocart_02(self, Setup):
        login_page = Loginpage(Setup)
        add2cart_page = AddToCartPage(Setup)
        login_page.login("standard_user", "secret_sauce")
        add2cart_page.click_add2cart_1()
        add2cart_page.click_add2cart_2()
        add2cart_page.view_cart()
        message = add2cart_page.message_card()
        assert message == "Your Cart"
        time.sleep(2)
        print(message)


    def test_addtocart_03(self, Setup):
        login_page = Loginpage(Setup)
        add2cart_page = AddToCartPage(Setup)
        login_page.login("standard_user", "secret_sauce")
        add2cart_page.click_add2cart_1()
        add2cart_page.click_add2cart_2()
        add2cart_page.view_cart()
        actual_homepage = add2cart_page.remove_item()
        assert actual_homepage == "Swag Labs"
        time.sleep(2)
        print(actual_homepage)



    def test_addtocart_04(self, Setup):
        login_page = Loginpage(Setup)
        add2cart_page = AddToCartPage(Setup)
        login_page.login("standard_user", "secret_sauce")
        add2cart_page.click_add2cart_1()
        add2cart_page.click_add2cart_2()
        actual_num_items = add2cart_page.number_of_items()
        assert actual_num_items == "2"
        time.sleep(2)
        print(actual_num_items)

        



