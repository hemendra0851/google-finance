# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
import time
from pages.base import BasePage
from data.locator import MarketTrends


class MarketTrendPages(BasePage):

    def wait_for_market_trend_page_to_load(self):
        self.wait_until_element_is_visible(MarketTrends.shareBtn)
        time.sleep(2)

    def is_selected_trend_tab_present(self, trend_name):
        return self.find_element(MarketTrends.trend_name_tab_item +
                                 f"[text()='{trend_name}']").is_displayed()

    def get_selected_trend_heading(self):
        return self.find_element(MarketTrends.trend_heading).text
