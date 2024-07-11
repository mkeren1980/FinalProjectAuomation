import time
import allure
from allure_commons.types import Severity

from pages.cart_4_page import CartPage
from pages.login_1_page import LoginPage
from pages.main_2_page import MainPage
from pages.prodcut_3_page import ProductPage
from pages.wishlist_5_page import WishlistPage

global p1
global p2
global p3
global p4
global p5


@allure.epic("Wishlist")
@allure.feature("Add to Wishlist")
class TestWishlist:

    @allure.severity(Severity.NORMAL)
    @allure.description("Test adding a product item to wishlist without logging in and verifying the alert message")
    @allure.title("Test Case 013: Add Product to Wishlist Without Login")
    def test_tc013(self):
        global p1
        p1 = LoginPage(self.driver)
        global p2
        p2 = MainPage(self.driver)
        global p3
        p3 = ProductPage(self.driver)
        global p4
        p4 = CartPage(self.driver)
        global p5
        p5 = WishlistPage(self.driver)
        with allure.step("main page steps"):
            time.sleep(1)
            p2.home_page_categories(3)
            time.sleep(2)
        with allure.step("product page steps"):
            p3.product_card_hover(3)
        p5.wishlist_btn(3)
        with allure.step("login page steps"):
            assert p1.alert() == "You must login or register to add items to your wishlist."
            allure.attach(self.driver.get_screenshot_as_png(), name="Wishlist without Login",
                          attachment_type=allure.attachment_type.PNG)

    @allure.severity(Severity.CRITICAL)
    @allure.description("Test adding a product item to wishlist with login and verifying it appears in the wishlist")
    @allure.title("Test Case 014: Add Product to Wishlist With Login")
    def test_tc014(self):
        with allure.step("login page steps"):
            p1.log_in()
            p1.log_in_data("mkeren4@gmail.com", "vv123456")
            time.sleep(10)
        with allure.step("product page steps"):
            p3.product_card_hover(3)
            time.sleep(3)
        with allure.step("wishlist page steps"):
            p5.wishlist_btn(3)
            time.sleep(2)
        with allure.step("login page steps"):
            p1.log_in()
            time.sleep(2)
            p1.my_wishlist()
            time.sleep(1)
        with allure.step("wishlist page steps"):
            assert p5.wishlist_count() == "(1)"
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name="Wishlist with Login",
                          attachment_type=allure.attachment_type.PNG)

    @allure.severity(Severity.CRITICAL)
    @allure.description("Test verifying the name of the single product in the wishlist")
    @allure.title("Test Case 015: Verify Wishlist Single Product Name")
    def test_tc015(self):
        with allure.step("wishlist page steps"):
            time.sleep(2)
            assert p5.wishlist_product_name(1) == p3.product_names_list(3)
            allure.attach(self.driver.get_screenshot_as_png(), name="Wishlist Single Product Name",
                          attachment_type=allure.attachment_type.PNG)

    @allure.severity(Severity.CRITICAL)
    @allure.description("Test verifying all previously added items are displayed in the wishlist")
    @allure.title("Test Case 016: Verify All Items in Wishlist")
    def test_tc016(self):
        with allure.step("login page steps"):
            p1.log_out()
            p1.log_in()
            p1.log_in_data("mkeren4@gmail.com", "vv123456")
            time.sleep(10)
            p1.log_in()
            time.sleep(2)
            p1.my_wishlist()
            time.sleep(1)
        with allure.step("wishlist page steps"):
            assert p5.wishlist_count() == "(1)"
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name="All Items in Wishlist",
                          attachment_type=allure.attachment_type.PNG)

    @allure.severity(Severity.NORMAL)
    @allure.description("Test removing a product from the wishlist and verifying the removal")
    @allure.title("Test Case 017: Remove Product from Wishlist")
    def test_tc017(self):
        with allure.step("wishlist page steps"):
            time.sleep(1)
            p5.wishlist_product_remove()
            time.sleep(1)
            assert p5.wishlist_count() == "(0)"
        with allure.step("login page steps"):
            assert p1.alert() == "Product has been removed from your Wish List!"
            allure.attach(self.driver.get_screenshot_as_png(), name="Product Removed from Wishlist",
                          attachment_type=allure.attachment_type.PNG)
            time.sleep(2)
            p1.home_btn()

    @allure.severity(Severity.NORMAL)
    @allure.description("Test adding multiple product items to wishlist and clearing all items")
    @allure.title("Test Case 018: Add Products to Wishlist and Clear All")
    def test_tc018(self):
        time.sleep(1)
        with allure.step("main page steps"):
            p2.menu_categories(3)
            time.sleep(1)
        with allure.step("product page steps"):
            p3.product_card_hover(2)
        with allure.step("wishlist page steps"):
            p5.wishlist_btn(2)
            time.sleep(1)
        with allure.step("product page steps"):
            p3.product_card_hover(1)
        with allure.step("wishlist page steps"):
            p5.wishlist_btn(1)
        with allure.step("login page steps"):
            p1.log_in()
            time.sleep(2)
            p1.my_wishlist()
            p1.clear_all_wishlist()
            assert p1.notification_clear_all() == "Close\nWishlist cleared"
        with allure.step("wishlist page steps"):
            assert p5.wishlist_count() == "(0)"
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name="Cleared Wishlist",
                          attachment_type=allure.attachment_type.PNG)
