import time

import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class ProductPage(BasePage):

    # Locators
    PRODUCT_CARD_LIST = (By.CSS_SELECTOR, ".ProductCard.ProductCard_layout_grid>a")
    PRODUCT_CARD_ADD_CART_BTN_LIST = (By.CSS_SELECTOR, ".AddToCart.Button")
    ADD_CART_BTN= (By.CSS_SELECTOR, ".AddToCart.Button ")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".ProductPage-ProductActions>H1")
    SHOPPING_OPTIONS_LIST = (By.CSS_SELECTOR, ".Field.Field_type_checkbox.ProductAttributeValue-Text")
    CATEGORY_SORT_BTN = (By.CSS_SELECTOR, "#category-sort_wrapper>div")
    CATEGORY_SORT_LIST =(By.CSS_SELECTOR, "#category-sort_wrapper>ul>div>li")
    PRODUCT_PRICES_LIST = (By.CSS_SELECTOR, ".ProductPrice-Price>span")
    PRODUCT_NAMES_LIST = (By.CSS_SELECTOR, ".ProductCard-Name")
    ITEMS_COUNT = (By.CSS_SELECTOR, ".CategoryPage-Miscellaneous>p")
    TITLE_SEARCH_RESULT = (By.CSS_SELECTOR, ".CategoryDetails-Heading.SearchPage-Heading>span")
    PAGINATION_LIST_ITEM = (By.CSS_SELECTOR, ".Pagination-ListItem")
    PAGINATION_NEXT_BTN = (By.CSS_SELECTOR, "[aria-label='Next page']")
    PAGINATION_CURRENT_BTN = (By.CSS_SELECTOR, ".PaginationLink.PaginationLink_isCurrent")
    REMOVE_FILTER_BTN = (By.CSS_SELECTOR, "[aria-label='Close']")
    CHECKBOX_LABEL_LIST = (By.CSS_SELECTOR, ".Field-CheckboxLabel")

    def __init__(self, driver):
        super().__init__(driver)
        self.saved_product_name = None  # Instance variable to store the product name

    @allure.step("verify that value: {value} is found in the title of the results page")
    def search_result(self, value):
        if value == self.get_text(self.TITLE_SEARCH_RESULT):
            return True
        else:
            return False

    @allure.step("removes any leading or trailing whitespace from product names")
    def get_filtered_names(self):
        product_names = []
        product_names_list = self.get_list(self.PRODUCT_NAMES_LIST)
        for name_element in product_names_list:
            name = name_element.text.strip()
            product_names.append(name)
        return product_names

    @allure.step("verify that value: {value} is found in the products title")
    def search_result_title(self, value):
        product_names = self.get_filtered_names()
        for i in range(len(product_names) - 1):
            if value in product_names[i].lower():
                return True
        return False

    @allure.step("verify that value: {value} is found in the product title (Auto-Suggest)")
    def single_product_title(self, value):
        if value in self.get_text(self.PRODUCT_TITLE).lower():
            return True
        else:
            return False

    @allure.step("click on next button in the pagination according the amount of the index: {index}")
    def pagination(self, index):
        self.driver.execute_script("window.scrollTo(300,document.body.scrollHeight);")
        self.driver.execute_script("window.scrollTo(300,document.body.scrollHeight);")
        time.sleep(2)
        pagination = self.get_list(self.PAGINATION_LIST_ITEM)
        if index < len(pagination):
            for i in range(0, index - 1, 1):
                self.driver.execute_script("window.scrollTo(300,document.body.scrollHeight);")
                time.sleep(2)
                self.click(self.PAGINATION_NEXT_BTN)
                self.driver.execute_script("window.scrollTo(300,document.body.scrollHeight);")


    @allure.step("verify that the current number is according to index: {index}")
    def pagination_number(self, index):
        if self.get_text(self.PAGINATION_CURRENT_BTN) == str(index):
            return True
        else:
            return False

    @allure.step("click product card according to index: {index}")
    def product_card(self, index):
        product_card_list = self.get_list(self.PRODUCT_CARD_LIST)
        if index < len(product_card_list):
            WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(product_card_list[index])).click()

    @allure.step("hover product card according to index: {index}")
    def product_card_hover(self, index):
        self.driver.execute_script("window.scrollTo(300,document.body.scrollHeight);")
        product_card_list = self.get_list(self.PRODUCT_CARD_LIST)
        if index < len(product_card_list):
            self.hover(product_card_list[index])

    @allure.step("get product title once clicking on a product card")
    def product_title(self):
        product_title = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(self.PRODUCT_TITLE))
        return product_title.text

    @allure.step("click on add to cart button from a single product item")
    def add_to_cart(self):
        self.click(self.ADD_CART_BTN)

    @allure.step("click on add to cart button product card by index: {index}")
    def product_add_to_cart(self, index):  # Click on add to cart from p
        product_card_add_cart_list = self.get_list(self.ADD_CART_BTN)
        if index < len(product_card_add_cart_list):
            WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(product_card_add_cart_list[index])).click()

    @allure.step("click on product card by index: {index}")
    def product_card_click(self, index):
        product_card_list = self.get_list(self.PRODUCT_CARD_LIST)
        if index < len(product_card_list):
            WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(product_card_list[index])).click()

    @allure.step("get a list of checkbox of shopping options and click on a checkbox according to index: {index}")
    def shopping_options_list(self, index):
        shopping_options_list = self.get_list(self.SHOPPING_OPTIONS_LIST)
        if index < len(shopping_options_list):
            (WebDriverWait(self.driver, 30).until
             (ec.element_to_be_clickable(shopping_options_list[index])).click())

    @allure.step("click on the category sort dropdown button")
    def category_sort_click(self):  #
        self.click(self.CATEGORY_SORT_BTN)

    @allure.step("click on an option from the dropdown according to index: {index}")
    def category_sort(self, index):  #
        category_sort_list = self.get_list(self.CATEGORY_SORT_LIST)
        if index < len(category_sort_list):
            WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(category_sort_list[index])).click()

    @allure.step("get the number of items found after filtering")
    def item_count(self):
        time.sleep(3)
        product_prices_list = self.get_list(self.PRODUCT_PRICES_LIST)
        items_found = (str(len(product_prices_list)) + " " + "items found")
        if self.get_text(self.ITEMS_COUNT) == items_found:
            return True
        else:
            return False

    @allure.step("extract text content from each WebElement and convert to float")
    def get_filtered_prices(self):
        filtered_prices = []
        product_prices_list = self.get_list(self.PRODUCT_PRICES_LIST)
        for element in product_prices_list:
            price_text = element.text.strip()
            try:
                # Remove non-numeric characters except for '.' and ','
                if '$' in price_text:
                    price_value = float(price_text.replace('$', '').replace(',', ''))
                elif '€' in price_text:
                    price_value = float(price_text.replace('€', '').replace('.', '').replace(',', '.'))
                else:
                    raise ValueError("Unsupported currency format")
                filtered_prices.append(price_value)
            except ValueError:
                # Handle cases where price_text cannot be converted to float
                pass
        return filtered_prices

    @allure.step("verify the product prices are in the price range")
    def product_prices_list(self, min_price, max_price):
        filtered_prices = self.get_filtered_prices()
        for price in filtered_prices:
            if min_price<= price <= max_price:
                return True
            else:
                return False

    @allure.step("verify the product prices are sorted from High to low")
    def product_prices_list_sort_asc(self):  # Verify
        filtered_prices = self.get_filtered_prices()
        for i in range(len(filtered_prices) - 1):
            if filtered_prices[i] > filtered_prices[i + 1] + 1:
                return True
        return False

    @allure.step("verify the product prices are sorted from  Low to High")
    def product_prices_list_sort_desc(self):
        filtered_prices = self.get_filtered_prices()
        for i in range(len(filtered_prices) - 1):
            if filtered_prices[i] < filtered_prices[i + 1] + 1:
                return True
        return False

    @allure.step("verify the product prices are sorted from A to Z")
    def product_names_list_sort(self):
        product_names = self.get_filtered_names()
        for i in range(len(product_names) - 1):
            if product_names[i].lower() < product_names[i + 1].lower():
                return True
        return False

    @allure.step("save the product card name (To compare it to wishlitst item title)")
    def product_names_list(self, index):
        product_names = self.get_filtered_names()
        if index < len(product_names):
            self.saved_product_name = product_names[index].lower()
        return self.saved_product_name

    @allure.step("remove filter of shopping options")
    def remove_filter(self):
        self.click(self.REMOVE_FILTER_BTN)