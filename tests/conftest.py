# import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# def pytest_exception_interact(driver, report):
#     if report.failed:
#         allure.attach(body=driver.get_screenshot_as_png(), name="screenshot",
#                       attachment_type=allure.attachment_type.PNG)


@pytest.fixture(scope="class", autouse=True)
def driver_init(request):
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    driver.get("https://tech-demo.scandipwa.com/")
    driver.maximize_window()
    yield  # after class
    driver.quit()