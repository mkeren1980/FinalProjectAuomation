import time
import allure
from allure_commons.types import Severity

from pages.login_1_page import LoginPage

global p1


@allure.epic("Security")
@allure.feature("Login")
class TestLogin:

    @allure.description("Test logging in with valid credentials and verifying the success message and welcome message")
    @allure.title("Test Case 007: Log In Successfully and Verify Welcome Message")
    @allure.story("As a user, I want to log in after entering valid credentials")
    def test_tc007(self):
        global p1
        p1 = LoginPage(self.driver)
        time.sleep(2)
        with allure.step("login page steps"):
            p1.log_in()
            p1.log_in_data("mkeren4@gmail.com", "vv123456")
            allure.attach("Login with valid credentials", name="Login Step",
                          attachment_type=allure.attachment_type.TEXT)
            time.sleep(2)
            assert p1.alert() == "You are successfully logged in!"
            allure.attach(self.driver.get_screenshot_as_png(), name="Login successfully",
                          attachment_type=allure.attachment_type.PNG)
            time.sleep(4)
            assert p1.welcome_msg() == "Welcome, Keren!"
            allure.attach(self.driver.get_screenshot_as_png(), name="Welcome account successfully",
                          attachment_type=allure.attachment_type.PNG)


    @allure.severity(Severity.CRITICAL)
    @allure.description("Test logging out successfully and verifying the logout message")
    @allure.title("Test Case 008: Log Out Successfully")
    @allure.story("As a user, I want to log out and see a successful logout message")
    def test_tc008(self):
        with allure.step("login page steps"):
            with allure.step("login page steps"):
                time.sleep(4)
                p1.log_in()
                time.sleep(4)
                p1.log_out()
                assert p1.alert() == "You are successfully logged out!"
                allure.attach(self.driver.get_screenshot_as_png(), name="Logout Screenshot",
                              attachment_type=allure.attachment_type.PNG)
                time.sleep(2)

    @allure.severity(Severity.NORMAL)
    @allure.description("Test resetting password by providing an email and verifying the reset message")
    @allure.title("Test Case 009: Reset Password and Verify Reset Message")
    @allure.story("As a user, I want to reset my password and receive a confirmation message")
    def test_tc009(self):
        with allure.step("login page steps"):
            p1.log_in()
            p1.forget_password()
            time.sleep(1)
            p1.rest_password("mkeren4@gmail.com")
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name="Reset Password Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            assert p1.reset_msg() == ('If there is an account associated with mkeren4@gmail.com you will receive an '
                                      'email with a link to reset your password')
            p1.close_reset_msg()
            time.sleep(1)

    @allure.severity(Severity.CRITICAL)
    @allure.description("Test logging in with incorrect password and verifying the error message")
    @allure.title("Test Case 010: Log In Fail with Incorrect Password")
    @allure.story("As a user, I want to see an error message when logging in with an incorrect password")
    def test_tc010(self):
        with allure.step("login page steps"):
            p1.log_in_data("mkeren4@gmail.com", "123456")
            time.sleep(2)
            allure.attach(self.driver.get_screenshot_as_png(), name="Incorrect Password Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            assert p1.log_in_email_error() == ('The account sign-in was incorrect or '
                                               'your account is disabled temporarily. '
                                               'Please wait and try again later.')
            time.sleep(2)

    @allure.severity(Severity.CRITICAL)
    @allure.description("Test logging in with empty fields and verifying the required field error messages")
    @allure.title("Test Case 011: Log In Fail with Required Fields Error")
    @allure.story("As a user, I want to see an error message when logging in with empty fields")
    def test_tc011(self):
        with allure.step("login page steps"):
            p1.log_in_data("", "")
            allure.attach(self.driver.get_screenshot_as_png(), name="Empty Fields Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            assert p1.email_required_error() and p1.password_required_error() == "This field is required!"
            time.sleep(2)

    @allure.severity(Severity.CRITICAL)
    @allure.description("Test logging in with an incorrect email format and verifying the email format error message")
    @allure.title("Test Case 012: Log In Fail with Incorrect Email Format")
    @allure.story("As a user, I want to see an error message when logging in with an incorrect email format")
    def test_tc012(self):
        with allure.step("login page steps"):
            p1.log_in_data("mkere", "vv123456")
            allure.attach(self.driver.get_screenshot_as_png(), name="Incorrect Email Format Screenshot",
                          attachment_type=allure.attachment_type.PNG)
            assert p1.email_required_error() == "Incorrect email format!"
