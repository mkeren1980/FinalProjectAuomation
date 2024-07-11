import time

import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class CheckoutPage(BasePage):

    # Locators
    EMAIL_INPUT = (By.CSS_SELECTOR, "[name='guest_email']")
    ERROR_MSG_EMAIL = (By.CSS_SELECTOR, "#root>div>div.Router-MainItems>main>section>div>div:nth-child(1)>div>"
                                        "div.CheckoutGuestForm.FieldForm>form>div>div>div>div.Field-ErrorMessages>div")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "[name='firstname']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "[name='lastname']")
    STREET_INPUT = (By.CSS_SELECTOR, "[name='street_0']")
    COUNTRY_DD_LIST = (By.CSS_SELECTOR, "#address-country-id_wrapper>ul>div>li")
    COUNTRY_DD_BTN = (By.CSS_SELECTOR, "#address-country-id_wrapper>div")
    CITY_INPUT = (By.CSS_SELECTOR, "[name='city']")
    POSTCODE_INPUT = (By.CSS_SELECTOR, "[name='postcode']")
    PHONE_INPUT = (By.CSS_SELECTOR, "[name='telephone']")
    PROCEED_TO_BILLING_BTN = (By.CSS_SELECTOR, ".Button.CheckoutShipping-Button")
    STANDARD_POST_BTN = (By.ID, "option-Standard\ Post")
    CASH_CHECKBOX = (By.CSS_SELECTOR, "[name='option-Cash On Delivery']")
    TERMS_CHECKBOX = (By.ID, "termsAndConditions")
    COMPLETE_ORDER_BTN = (By.CSS_SELECTOR, ".Button.CheckoutBilling-Button")
    CHECKOUT_TITLE = (By.CSS_SELECTOR, "div:nth-child(1)>div>div.Checkout-Header>div")
    CHECKOUT_ORDER_TITLE = (By.CSS_SELECTOR, ".CheckoutSuccess>h3")
    CHECKOUT_SUB_TITLE = (By.CSS_SELECTOR, ".CheckoutSuccess>p")
    CONTINUE_SHOPPING_BTN = (By.CSS_SELECTOR, ".Button.CheckoutSuccess-ContinueButton")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("fill personal information in checkout with email: {email}, first name: {first_name}, "
                 "last name: {last_name}, street number: {}, city: {city}, "
                 "postcode: {postcode} and phone number {phone}")
    def personal_information(self, email, first_name, last_name, street, city, postcode, phone):
        self.fill_text(self.EMAIL_INPUT, email)
        self.fill_text(self.FIRST_NAME_INPUT, first_name)
        self.fill_text(self.LAST_NAME_INPUT, last_name)
        self.fill_text(self.STREET_INPUT, street)
        self.fill_text(self.CITY_INPUT, city)
        self.fill_text(self.POSTCODE_INPUT, postcode)
        self.fill_text(self.PHONE_INPUT, phone)

    @allure.step("click on country dropdown button")
    def click_country_dd(self):
        self.click(self.COUNTRY_DD_BTN)

    @allure.step("click on specific country by index: {index}")
    def select_country(self, index):
        select_country_list = self.get_list(self.COUNTRY_DD_LIST)
        if index < len(select_country_list):
            WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable(select_country_list[index])).click()

    @allure.step("preform shipping method section checkboxes")
    def shipping_method(self):
        self.driver.execute_script("window.scrollTo(300,document.body.scrollHeight);")
        with allure.step("check the standard post checkbox"):
            self.click(self.STANDARD_POST_BTN)
            self.click(self.PROCEED_TO_BILLING_BTN)
        time.sleep(2)

    @allure.step("preform billing address section checkboxes")
    def billing_address(self):
        with allure.step("check the cash checkbox"):
            self.click(self.CASH_CHECKBOX)
        self.click(self.TERMS_CHECKBOX)
        self.click(self.COMPLETE_ORDER_BTN)

    @allure.step("get the header of complete purchase")
    def complete_purchase_header(self):  # Display
        return self.get_text(self.CHECKOUT_TITLE)

    @allure.step("get the text of the order number - complete the purchase")
    def complete_purchase_order_number(self):
        return self.get_text(self.CHECKOUT_ORDER_TITLE)

    @allure.step("get  the sub-text of complete purchase")
    def complete_purchase_sub_header(self):
        return self.get_text(self.CHECKOUT_SUB_TITLE)

    @allure.step("click on continue shopping button once complete the purchase")
    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)

    @allure.step("get notification about required email in checkout")
    def error_msg_email(self):
        error_msg_email = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(self.ERROR_MSG_EMAIL))
        return error_msg_email.text
