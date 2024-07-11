import time

import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By




class CartPage(BasePage):

    # Locators
    CART_BTN = (By.CSS_SELECTOR, "[aria-label='Cart']")
    CART_COUNT = (By.CSS_SELECTOR, ".Header-MinicartButtonWrapper>span")
    CART_REMOVE_PRODUCT = (By.CSS_SELECTOR, "#RemoveItem")
    CART_REMOVE_MSG = (By.CSS_SELECTOR, ".CartOverlay-ContentWrapper>p")
    CHECKOUT_BTN = (By.CSS_SELECTOR, ".CartOverlay-CheckoutButton.Button")

    # PRODUCT_TITLE_CART_LIST = (By.CSS_SELECTOR, ".CartItem-Title.CartItem-Title_isMobileLayout>p")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("click on the cart button")
    def cart(self):
        self.click(self.CART_BTN)

    @allure.step("get the number of the items in the cart")
    def cart_count(self):
        return self.get_text(self.CART_COUNT)

    @allure.step("remove item from the cart")
    def remove_product(self):
        time.sleep(3)
        self.click(self.CART_REMOVE_PRODUCT)

    @allure.step("get remove product message")
    def remove_product_msg(self):
        return self.get_text(self.CART_REMOVE_MSG)

    @allure.step("click n the checkout button in the cart")
    def checkout_btn(self):
        self.click(self.CHECKOUT_BTN)
