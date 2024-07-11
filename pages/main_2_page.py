import time

import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MainPage(BasePage):

    # Locators
    SEARCH_INPUT = (By.ID, "search-field")
    SEARCH_DROPDOWN_LIST = (By.CSS_SELECTOR, ".SearchItem")
    HOME_PAGE_CATEGORIES_LIST = (By.CSS_SELECTOR, ".HomepageCategories-Figure")
    PRODUCT_CARD_LIST = (By.CSS_SELECTOR, ".ProductListPage.ProductListWidget-Page>li>a")
    PRODUCT_CARD_ADD_CART_BTN_LIST = (By.CSS_SELECTOR, ".AddToCart.Button ")
    PRODUCT_CARD_SCROLL_LIST = (By.CSS_SELECTOR, ".ProductCard-Link")
    MENU_CATEGORIES_LIST = (By.CSS_SELECTOR, ".Menu-ItemList.Menu-ItemList_type_main>li")
    NO_RESULT_FOUND_MSG = (By.CSS_SELECTOR, ".SearchOverlay-Results>p")
    NO_RESULT_FOUND_H2_MSG_ENTER = (By.CSS_SELECTOR, ".ProductList-ProductsMissing>h2")
    NO_RESULT_FOUND_H3_MSG_ENTER = (By.CSS_SELECTOR, ".ProductList-ProductsMissing>h3")
    NO_RESULT_FOUND_P_MSG_ENTER = (By.CSS_SELECTOR, ".ProductList-ProductsMissing>p")

    LOGO_BTN = (By.CSS_SELECTOR, ".Image.Image_imageStatus_IMAGE_LOADED.Logo>img")


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("search Keyword: {item} and click enter")
    def search_item_enter(self, item):  #
        self.fill_text(self.SEARCH_INPUT, item)
        self.click_enter(self.SEARCH_INPUT)

    @allure.step("search Keyword: {item} without click enter")
    def search_item(self, item):
        self.fill_text(self.SEARCH_INPUT, item)

    @allure.step("select a product from the dropdown menu after searching according to index: {index}")
    def select_search_dropdown(self, index):  #
        select_search_dropdown = self.get_list(self.SEARCH_DROPDOWN_LIST)
        if index < len(select_search_dropdown):
            WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(select_search_dropdown[index])).click()

    @allure.step("click on add to cart button from product card according to index: {index}")
    def product_card_add_to_cart(self, index):  # Clicking
        product_card_add_cart_list = self.get_list(self.PRODUCT_CARD_ADD_CART_BTN_LIST)
        if index < len(product_card_add_cart_list):
            WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(product_card_add_cart_list[index])).click()

    @allure.step("click on add to cart button from product card according to index: {index}")
    def menu_categories(self, index):  # Choosing category from menu page
        menu_categories_list = self.get_list(self.MENU_CATEGORIES_LIST)
        if index < len(menu_categories_list):
            WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(menu_categories_list[index])).click()

    @allure.step("get after search no result message from dropdown")
    def no_result_msg(self):
        return self.get_text(self.NO_RESULT_FOUND_MSG)

    @allure.step("verify after search the text of no result page")
    def no_result_msg_enter(self, h2, h3, p):
        if h2 == self.get_text(self.NO_RESULT_FOUND_H2_MSG_ENTER) and \
                h3 == self.get_text(self.NO_RESULT_FOUND_H3_MSG_ENTER) and \
                p == self.get_text(self.NO_RESULT_FOUND_P_MSG_ENTER):
            return True
        else:
            return False

    @allure.step("click on the logo button")
    def logo(self):
        return self.click(self.LOGO_BTN)

    @allure.step("click on one of the categories according to index: {index}")
    def home_page_categories(self, index):
        home_page_categories_list = self.get_list(self.HOME_PAGE_CATEGORIES_LIST)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(100,document.body.scrollHeight);")
        if index < len(home_page_categories_list):
            (WebDriverWait(self.driver, 30).
             until(ec.element_to_be_clickable(home_page_categories_list[index])).click())