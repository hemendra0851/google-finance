from pages.base import BasePage
from data.locator import Calendar, SignIn


class CalendarPage(BasePage):

    def wait_for_calendar_tab_to_load(self, browser: str, options: list):

        if browser == 'chrome' and 'headless' not in options:
            self.wait_until_element_is_visible(Calendar.header)
        else:
            self.wait_until_element_is_visible(SignIn.email)
