from pages.base import BasePage
from data.locator import SignIn


class SignInPage(BasePage):

    def wait_for_signin_page_to_load(self):
        self.wait_until_element_is_visible(SignIn.email)

    def enter_email(self):
        self.find_element(SignIn.email).send_keys('Hello')
