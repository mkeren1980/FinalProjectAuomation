import time
import allure
from allure_commons.types import Severity
from pages.login_1_page import LoginPage
from pages.main_2_page import MainPage
from pages.prodcut_3_page import ProductPage

global p1
global p2
global p3


@allure.epic("Search")
@allure.feature("Product Search")
class TestSearch:

    @allure.severity(Severity.CRITICAL)
    @allure.description("Test searching for a product by keyword and verifying search results")
    @allure.title("Test Case 001: Search for Product by Keyword")
    def test_tc001(self):
        global p1
        p1 = LoginPage(self.driver)
        global p2
        p2 = MainPage(self.driver)
        global p3
        p3 = ProductPage(self.driver)

        time.sleep(1)
        with allure.step("main page steps"):
            p2.search_item_enter("laptop")
            allure.attach(self.driver.get_screenshot_as_png(), name="Search Step",
                          attachment_type=allure.attachment_type.PNG)
            time.sleep(5)
        with allure.step("product page steps"):
            assert p3.search_result("laptop") is True
            allure.attach(self.driver.get_screenshot_as_png(), name="Search Result Step",
                          attachment_type=allure.attachment_type.PNG)
            time.sleep(5)
            assert p3.search_result_title("laptop") is True
        time.sleep(2)
        with allure.step("main page steps"):
            p2.logo()

    @allure.severity(Severity.CRITICAL)
    @allure.description("Test searching with a keyword that yields no results using auto-suggest")
    @allure.title("Test Case 002: Search with No Results Found (Auto-Suggest)")
    def test_tc002(self):
        with allure.step("main page steps"):
            time.sleep(1)
            p2.search_item("aabb")
            allure.attach(self.driver.get_screenshot_as_png(), name="Search Step",
                          attachment_type=allure.attachment_type.PNG)
            time.sleep(5)
            assert p2.no_result_msg() == "No results found!"
            allure.attach(self.driver.get_screenshot_as_png(), name="No Results Step",
                          attachment_type=allure.attachment_type.PNG)

            p2.logo()

    @allure.severity(Severity.NORMAL)
    @allure.description("Test searching with a keyword that yields no results using enter")
    @allure.title("Test Case 003: Search with No Results Found (Enter)")
    def test_tc003(self):
        with allure.step("main page steps"):
            time.sleep(1)
            p2.search_item_enter("aabb")
            time.sleep(5)
            assert p2.no_result_msg_enter("We Are Sorry!", "There Were No Products Found Matching Your Request.",
                                          "Please, try removing selected filters and try again!")
            time.sleep(1)
            p2.logo()

    @allure.severity(Severity.MINOR)
    @allure.description("Test searching with special characters and verifying search results using enter")
    @allure.title("Test Case 004: Search with Special Characters (Enter)")
    def test_tc004(self):
        with allure.step("main page steps"):
            time.sleep(1)
            p2.search_item_enter("laptop@#")
            time.sleep(5)
        with allure.step("product page steps"):
            assert p3.search_result("laptop@#") is True
            time.sleep(5)
            assert p3.search_result_title("laptop") is True
            time.sleep(2)
        with allure.step("main page steps"):
            p2.logo()

    @allure.severity(Severity.CRITICAL)
    @allure.description("Test searching with auto-suggest and verifying the selected product title")
    @allure.title("Test Case 005: Search with Auto-Suggest")
    def test_tc005(self):
        with allure.step("main page steps"):
            time.sleep(1)
            p2.search_item("laptop")
            time.sleep(5)
            p2.select_search_dropdown(5)
            time.sleep(1)
            assert p3.single_product_title("laptop") is True
            allure.attach(self.driver.get_screenshot_as_png(), name="Selected Product Step",
                          attachment_type=allure.attachment_type.PNG)
            p2.logo()

    @allure.severity(Severity.NORMAL)
    @allure.description("Test pagination of search results and verifying the displayed page number")
    @allure.title("Test Case 006: Search Results Pagination")
    def test_tc006(self):
        with allure.step("main page steps"):
            time.sleep(1)
            p2.menu_categories(2)
            time.sleep(2)
        with allure.step("product page steps"):
            p3.pagination(4)
            time.sleep(7)
            assert p3.pagination_number(4) is True
            time.sleep(2)