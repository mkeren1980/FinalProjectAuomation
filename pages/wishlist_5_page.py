import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class WishlistPage(BasePage):

    # Locators
    WISHLIST_BTN_LIST = (By.CSS_SELECTOR, ".ProductWishlistButton")
    WISHLIST_COUNT = (By.CSS_SELECTOR, ".MyAccount-Heading>span")
    WISHLIST_REMOVE_BTN = (By.CSS_SELECTOR, "[aria-label='Remove']")
    WISHLIST_PRODUCT_NAME_LIST = (By.CSS_SELECTOR, ".WishlistItem-FigureWrapper>a>h4")



    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("add product item to wishlist according to index: {index}")
    def wishlist_btn(self, index):
        wishlist_btn_list = self.get_list(self.WISHLIST_BTN_LIST)
        if index < len(wishlist_btn_list):
            WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(wishlist_btn_list[index])).click()

    @allure.step("get the number of items in wishlist")
    def wishlist_count(self):
        return self.get_text(self.WISHLIST_COUNT)

    @allure.step("click on the X button to remove item from wishlist")
    def wishlist_product_remove(self):
        self.click(self.WISHLIST_REMOVE_BTN)

    @allure.step("get the name of the product item in the wishlist according to index: {index}")
    def wishlist_product_name(self, index):  #
        wishlist_product_name_list = self.get_list(self.WISHLIST_PRODUCT_NAME_LIST)
        if index < len(wishlist_product_name_list):
            return self.get_text(self.WISHLIST_PRODUCT_NAME_LIST)
