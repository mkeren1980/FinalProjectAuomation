import time

import allure
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def highlight_element(self, locator, color):
        element = self.driver.find_element(*locator)
        original_style = element.get_attribute("style")
        new_style = "background-color: " + color + ";" + original_style

        # Change the style temporarily
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, new_style)

        # Change the style back after a few milliseconds
        self.driver.execute_script("setTimeout(function () { arguments[0].setAttribute('style', arguments[1]); }, 400);"
                                   , element, original_style)

    def __init__(self, driver):
        self.driver: WebDriver = driver

    @allure.step("fill in the fields with paramters")
    def fill_text(self, locator, text):
        self.highlight_element(locator, "Yellow")
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    @allure.step("click on an element")
    def click(self, locator):
        time.sleep(1)
        self.highlight_element(locator, "Yellow")
        self.driver.find_element(*locator).click()

    @allure.step("click enter from the keyboard")
    def click_enter(self, locator):
        self.driver.find_element(*locator).send_keys(Keys.ENTER)

    @allure.step("hover on an element")
    def hover(self, element):
        self.driver.execute_script("arguments[0].style.border='4px solid yellow'", element)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        time.sleep(5)
        self.driver.execute_script("arguments[0].style.border=''", element)

    @allure.step("get text value")
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("select a value option from dropdown")
    def get_select(self, locator, value):
        el = self.driver.find_element(*locator)
        dd = Select(el)
        dd.select_by_value(value)

    @allure.step("find elements for a list")
    def get_list(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("verify if an element is display or not")
    def get_display(self, locator):
        try:
            if self.driver.find_element(*locator).is_displayed():
                return True
            else:
                return False
        except NoSuchElementException:
            return True
