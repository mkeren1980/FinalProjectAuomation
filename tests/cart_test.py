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


@allure.epic("Cart")
@allure.feature("Manage Cart")
class TestCart:

    @allure.severity(Severity.NORMAL)
    @allure.description("Test adding a product to the cart from the product page")
    @allure.title("Test Case 019: Add Product to Cart and Verify Cart Count")
    def test_tc019(self):
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
        time.sleep(1)

        with allure.step("main page steps"):
            p2.home_page_categories(2)
        time.sleep(1)
        with allure.step("product page steps"):
            p3.product_card(2)
            allure.attach(self.driver.get_screenshot_as_png(), name="Home Page Categories",
                          attachment_type=allure.attachment_type.PNG)

            time.sleep(1)
            assert p3.product_title() == "PS4 game Ghost of Tsushima (0,711,719,366,508)"
            p3.add_to_cart()
            allure.attach(self.driver.get_screenshot_as_png(), name="Product Added to Cart",
                          attachment_type=allure.attachment_type.PNG)
        time.sleep(2)
        with allure.step("login page steps"):
            assert p1.alert() == "Product was added to cart!"
            allure.attach(self.driver.get_screenshot_as_png(), name="Product Added Alert",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("cart page steps"):
            assert p4.cart_count() == "1"
            allure.attach(self.driver.get_screenshot_as_png(), name="Cart Count",
                          attachment_type=allure.attachment_type.PNG)

    @allure.severity(Severity.NORMAL)
    @allure.description("Test removing a product from the cart and verifying the cart is empty")
    @allure.title("Test Case 020: Remove Product from Cart and Verify Cart is Empty")
    def test_tc020(self):
        with allure.step("cart page steps"):
            time.sleep(1)
            p4.cart()
            p4.remove_product()
            time.sleep(2)
            assert p4.remove_product_msg() == "You have no items in your shopping cart."
            allure.attach(self.driver.get_screenshot_as_png(), name="Product Removed from Cart",
                          attachment_type=allure.attachment_type.PNG)
            time.sleep(4)

    @allure.severity(Severity.BLOCKER)
    @allure.description("Test the complete buyer process of purchasing a product without logging in, "
                        "including searching, adding to cart, and completing the purchase")
    @allure.title("Test Case 021: Full Buyer Process Without Login - Successful Purchase")
    def test_tc021(self):
        with allure.step("main page steps"):
            p2.search_item("laptop")
            time.sleep(2)
            p2.select_search_dropdown(5)
            allure.attach(self.driver.get_screenshot_as_png(), name="Search Item",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("product page steps"):
            p3.add_to_cart()
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name="Add to Cart",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("cart page steps"):
            p4.cart()
            time.sleep(2)
            p4.checkout_btn()
        with allure.step("checkout page steps"):
            p6.personal_information("mkeren4@gmail.com", "keren", "miron", "ehud manor 15",
                                    "Tel-Aviv", "5423212", "05236999541")
            time.sleep(2)
            p6.click_country_dd()
            time.sleep(2)
            p6.select_country(109)
            time.sleep(5)
            p6.shipping_method()
            time.sleep(4)
            p6.billing_address()
            time.sleep(10)
            allure.attach(self.driver.get_screenshot_as_png(), name="Checkout Details",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("checkout page steps"):
            assert p6.complete_purchase_header() == "Thank you for your purchase!"
            assert "Your Order # Is" in p6.complete_purchase_order_number()
            assert p6.complete_purchase_sub_header() == ("We`ll email you an order "
                                                         "confirmation with details and tracking info.")
            allure.attach(self.driver.get_screenshot_as_png(), name="Purchase Confirmation",
                          attachment_type=allure.attachment_type.PNG)
            p6.continue_shopping()

    @allure.severity(Severity.CRITICAL)
    @allure.description("Test the complete buyer process of attempting to purchase a product without logging in, "
                        "where the email field is required and not provided")
    @allure.title("Test Case 022: Full Buyer Process Without Login - Missing Email")
    def test_tc022(self):
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
        time.sleep(1)
        with allure.step("main page steps"):
            time.sleep(4)
            p2.search_item("laptop")
            time.sleep(2)
            p2.select_search_dropdown(5)
            allure.attach(self.driver.get_screenshot_as_png(), name="Search Item No Email",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("product page steps"):
            p3.add_to_cart()
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name="Add to Cart No Email",
                          attachment_type=allure.attachment_type.PNG)
        with allure.step("cart page steps"):
            p4.cart()
            time.sleep(2)
            p4.checkout_btn()
            allure.attach(self.driver.get_screenshot_as_png(), name="Checkout Button No Email",
                          attachment_type=allure.attachment_type.PNG)
            with allure.step("checkout page steps"):
                p6.personal_information("", "keren", "miron", "ehud manor 15",
                                        "Tel-Aviv", "5423212", "05236999541")
            time.sleep(5)
            p6.shipping_method()
            time.sleep(2)
            assert p6.error_msg_email() == "This field is required!"
            allure.attach(self.driver.get_screenshot_as_png(), name="Error Message Email",
                          attachment_type=allure.attachment_type.PNG)

            time.sleep(5)
