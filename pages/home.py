from pages.base import BasePage
from data.locator import Home
from data.env import Env


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_home_page(self):
        self._driver.get(Env.url)
        self.wait_until_element_is_visible(Home.compare_markets_tabs)

    def get_market_names(self):
        return [el.text for el in self.find_elements(Home.compare_markets_tabs)]

    def click_market_name(self, market_name):
        locator = (f"(//span[@id='market-rundown-heading']/parent::div"
                   f"/following-sibling::div)[text()='{market_name}']")
        self.click(locator)

    def get_market_index(self):
        return [el.text for el in self.find_elements(Home.compare_markets_indices)]

    def search_asset(self, search_text):
        self.input_text(Home.search, search_text)
        self.wait_until_element_is_visible(Home.search_options)
        self.click(Home.search_options)
        self.wait_until_element_is_visible(Home.search_result_heading)

    def get_search_result_heading(self):
        return self.find_element(Home.search_result_heading).text

    def follow_index_as_guest(self):
        self.click(Home.follow_index)
        self.wait_until_element_not_visible(Home.follow_index)

    def add_event_to_calendar(self):
        self.click(Home.add_to_calendar_icon)
        tabs = self._driver.window_handles
        self._driver.switch_to.window(tabs[1])
        self.wait_until_element_not_visible(Home.add_to_calendar_icon)

    def select_market_trend(self, trend_name):
        locator = (f"(//div[text()='Market trends'])[2]"
                   f"/following-sibling::div//span[text()='{trend_name}']")
        self.click(locator)
