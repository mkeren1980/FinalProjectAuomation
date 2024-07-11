import time

import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# Incorrect email format!

class LoginPage(BasePage):

    LOGIN_ICON_BTN = (By.CSS_SELECTOR, "#myAccount")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    SIGN_IN_BTN = (By.CSS_SELECTOR, ".MyAccountOverlay-SignInButton>button")
    WELCOME_MSG =(By.CSS_SELECTOR, ".Header-Welcome.Header-Welcome_type_Welcome")
    LOG_OUT_BTN = (By.CSS_SELECTOR, ".MyAccountTabListItem:nth-child(8)")
    WISHLIST_BTN = (By.CSS_SELECTOR, ".MyAccountTabListItem:nth-child(4)")
    ALERT = (By.XPATH, "//div[@class='NotificationList']/div/p")
    EMAIL_REQUIRED_MSG = (By.CSS_SELECTOR, ".Field-Wrapper.Field-Wrapper_type_email>.Field-ErrorMessages")
    PASS__REQUIRED_MSG = (By.CSS_SELECTOR, ".Field-Wrapper.Field-Wrapper_type_password>.Field-ErrorMessages")
    ALERT_PASSWORD_ERROR = (By.CSS_SELECTOR, ".Notification_type_error>p")
    ALERT_PASSWORD_ERROR_CLOSE = (By.CSS_SELECTOR, ".Notification_type_error.Notification_is_opening>button")
    FORGET_PASSWORD_BTN = (By.CSS_SELECTOR, "[type='button']")
    SEND_RESET_LINK_BTN = (By.CSS_SELECTOR, ".Button.MyAccountOverlay-ResetPassword")
    RESET_MSG = (By.CSS_SELECTOR, "#forgot-password-success")
    GOT_IT_BTN = (By.CSS_SELECTOR, "[aria-labelledby='forgot-password-success']>button")
    HOME_BTN = (By.CSS_SELECTOR, ".Breadcrumbs-List>li>a:nth-child(1)")
    WISHLIST_CLEAR_ALL_BTN = (By.CSS_SELECTOR, ".Button.Button_isHollow.Button_isWithoutBorder"
                                               ".MyAccountMyWishlist-ClearWishlistButton")
    NOTIFICATION_WISHLIST_CLEARED = (By.CSS_SELECTOR, ".Notification.Notification_type_success.Notification_is_closing")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("click on the Login button")
    def log_in(self):
        time.sleep(1)
        self.click(self.LOGIN_ICON_BTN)

    @allure.step("click on the Logout button")
    def log_out(self):
        WebDriverWait(self.driver, 3).until(ec.element_to_be_clickable(self.LOG_OUT_BTN)).click()

    @allure.step("get Login message")
    def welcome_msg(self):  #
        return self.get_text(self.WELCOME_MSG)

    @allure.step("login with email: {email} and password: {password}")
    def log_in_data(self, email, password):
        time.sleep(1)
        self.fill_text(self.EMAIL_FIELD, email)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.click(self.SIGN_IN_BTN)

    @allure.step("get success and error message notification")
    def alert(self):
        alert_element = WebDriverWait(self.driver, 30).until(
            ec.visibility_of_element_located(self.ALERT))
        return alert_element.text

    @allure.step("get error invalid email message")
    def log_in_email_error(self):
        return self.get_text(self.ALERT_PASSWORD_ERROR)

    @allure.step("get error required email message")
    def email_required_error(self):
        return self.get_text(self.EMAIL_REQUIRED_MSG)

    @allure.step("get error required password message")
    def password_required_error(self):
        time.sleep(1)
        return self.get_text(self.PASS__REQUIRED_MSG)

    @allure.step("click on forget password button")
    def forget_password(self):
        self.click(self.FORGET_PASSWORD_BTN)

    @allure.step("enter email: {email} reset a password")
    def rest_password(self, email):
        time.sleep(1)
        self.fill_text(self.EMAIL_FIELD, email)
        self.click(self.SEND_RESET_LINK_BTN)

    @allure.step("get reset password message ")
    def reset_msg(self):
        time.sleep(1)
        return self.get_text(self.RESET_MSG)

    @allure.step("click on close button to close reset password message")
    def close_reset_msg(self):
        time.sleep(1)
        self.click(self.GOT_IT_BTN)

    @allure.step("click on my wishlist tab in the account page")
    def my_wishlist(self):
        self.click(self.WISHLIST_BTN)

    @allure.step("click clear all wishlist button in the account page")
    def clear_all_wishlist(self):  #
        self.click(self.WISHLIST_CLEAR_ALL_BTN)

    @allure.step("get notification message from clear all items from wishlist")
    def notification_clear_all(self):
        notification_element = WebDriverWait(self.driver, 20).until(
            ec.visibility_of_element_located(self.NOTIFICATION_WISHLIST_CLEARED)
        )
        notification_text = notification_element.text
        return notification_text

    @allure.step("click on home button from wishlist in the account page to return to main page ")
    def home_btn(self):
        self.click(self.HOME_BTN)