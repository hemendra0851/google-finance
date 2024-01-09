import time
from pages.base import BasePage
from data.locator import Home


class MainMenu(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_main_menu(self):
        self.click(Home.main_menu)
        self.wait_until_element_is_visible(Home.menu_item)
        time.sleep(0.5)

    def get_menu_items(self):
        return [el.text for el in self.find_elements(Home.menu_item)]

    def is_main_menu_opened(self):
        return self.find_element(Home.menu_settings).is_displayed()

    def open_portfolio_menu_item(self):
        self.click(Home.menu_portfolio)

    def open_watchlist_menu_item(self):
        self.click(Home.menu_watchlist)
