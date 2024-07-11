import time
import allure
from allure_commons.types import Severity

from pages.cart_4_page import CartPage
from pages.checkout_6_page import CheckoutPage
from pages.login_1_page import LoginPage
from pages.main_2_page import MainPage
from pages.prodcut_3_page import ProductPage

global p1
global p2
global p3
global p4
global p6


@allure.epic("Filter")
@allure.feature("Product Filtering")
class TestFilter:
    @allure.severity(Severity.CRITICAL)
    @allure.description("Test filtering products by a specified price range and verifying "
                        "the products fall within that range")
    @allure.title("Test Case 023: Filter Products by Price Range and Verify")
    def test_tc023(self):
        global p1
        p1 = LoginPage(self.driver)
        global p2
        p2 = MainPage(self.driver)
        global p3
        p3 = ProductPage(self.driver)
        global p4
        p4 = CartPage(self.driver)
        global p6
        p6 = CheckoutPage(self.driver)

        time.sleep(2)
        with allure.step("main page steps"):
            p2.menu_categories(2)
            time.sleep(4)
        with allure.step("product page steps"):
            p3.shopping_options_list(2)
            time.sleep(2)
        with allure.step("verify that the items count is found"):
            assert p3.item_count() is True
        time.sleep(7)
        assert p3.product_prices_list(2000.00, 2999.99) is True
        allure.attach(self.driver.get_screenshot_as_png(), name="Range of prices",
                      attachment_type=allure.attachment_type.PNG)

    @allure.severity(Severity.NORMAL)
    @allure.description("Test sorting products by price in descending order High to Low and verifying the order")
    @allure.title("Test Case 024: Sort Products by Price Descending High to Low")
    def test_tc024(self):
        with allure.step("product page steps"):
            p3.category_sort_click()
            time.sleep(1)
            p3.category_sort(4)
            time.sleep(7)
            assert p3.product_prices_list_sort_asc() is True
            allure.attach(self.driver.get_screenshot_as_png(), name="Price Descending Order",
                          attachment_type=allure.attachment_type.PNG)

    @allure.severity(Severity.NORMAL)
    @allure.description("Test sorting products by name in alphabetical order and verifying the order")
    @allure.title("Test Case 025: Sort Products by Name")
    def test_tc025(self):
        with allure.step("product page steps"):
            p3.category_sort_click()
            time.sleep(1)
            p3.category_sort(1)
            time.sleep(7)
            assert p3.product_names_list_sort() is True
            allure.attach(self.driver.get_screenshot_as_png(), name="Name Alphabetical Order",
                          attachment_type=allure.attachment_type.PNG)

    @allure.severity(Severity.NORMAL)
    @allure.description("Test sorting products by price in ascending order Low to High and verifying the order")
    @allure.title("Test Case 026: Sort Products by Price Ascending Low to High")
    def test_tc026(self):
        with allure.step("product page steps"):
            p3.category_sort_click()
            time.sleep(1)
            p3.category_sort(3)
            time.sleep(7)
            assert p3.product_prices_list_sort_desc() is True
            allure.attach(self.driver.get_screenshot_as_png(), name="Price Ascending Order",
                          attachment_type=allure.attachment_type.PNG)

    @allure.severity(Severity.NORMAL)
    @allure.description("Test removing the applied price filter from products and verifying the filter is removed")
    @allure.title("Test Case 027: Remove Filter from Products by Price Range")
    def test_tc027(self):
        p3.remove_filter()
        time.sleep(1)
        allure.attach(self.driver.get_screenshot_as_png(), name="Filter Removed",
                      attachment_type=allure.attachment_type.PNG)