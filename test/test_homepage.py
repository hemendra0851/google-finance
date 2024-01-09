from pytest import mark
from data.content import Content
from pages.home import HomePage
from pages.sign_in import SignInPage
from pages.market_trend import MarketTrendPages
from pages.calendar import CalendarPage


@mark.usefixtures('create_driver')
class HomePageTest:

    def test_homepage_loaded(self):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        assert home_page.get_page_title() == Content.homePageTitle

    def test_available_market_tabs(self):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        actual_markets_names = home_page.get_market_names()
        assert actual_markets_names.sort() == Content.market_tabs.sort()

    @mark.parametrize("market_name", ['US', 'Europe'])
    def test_available_indices_for_markets(self, market_name):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        home_page.click_market_name(market_name)
        assert home_page.get_market_names().sort() == Content.market_index[market_name].sort()

    @mark.smoke
    def test_search_stock_and_other_assets(self):
        home_page = HomePage(self.driver)
        home_page.open_home_page()
        home_page.search_asset('BTC/INR')
        assert home_page.get_search_result_heading() == 'Bitcoin to Indian Rupee'

    def test_follow_index_as_guest(self):
        home_page = HomePage(self.driver)
        signin_page = SignInPage(self.driver)

        home_page.open_home_page()
        home_page.follow_index_as_guest()
        signin_page.wait_for_signin_page_to_load()

        assert signin_page.get_page_title() == 'Sign in - Google Accounts'

    @mark.smoke
    def test_add_event_to_calendar_as_guest(self):
        home_page = HomePage(self.driver)
        calendarpage = CalendarPage(self.driver)

        home_page.open_home_page()
        home_page.add_event_to_calendar()
        calendarpage.wait_for_calendar_tab_to_load(self.browser, self.options)

        if self.browser == 'chrome' and 'headless' not in self.options:
            assert (calendarpage.get_page_title() ==
                    'Shareable online calendar and scheduling – Google Calendar')
        else:
            assert (calendarpage.get_page_title() ==
                    'Google Calendar - Sign in to Access & Edit Your Schedule')

    @mark.smoke
    @mark.parametrize("trend_name, expected_title",
                      [("Most active", "Most Active Stocks"),
                       ("Gainers", "Top Stock Gainers"),
                       ("Losers", "Top Stock Losers")])
    def test_search_market_trends(self, trend_name, expected_title):
        home_page = HomePage(self.driver)
        market_page = MarketTrendPages(self.driver)

        home_page.open_home_page()
        home_page.select_market_trend(trend_name)
        market_page.wait_for_market_trend_page_to_load()

        assert market_page.get_page_title() == expected_title + " - Google Finance"
        assert market_page.is_selected_trend_tab_present(trend_name) is True
        assert market_page.get_selected_trend_heading() == trend_name
