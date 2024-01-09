from pytest import mark
from data.content import Content
from pages.home import HomePage
from pages.sign_in import SignInPage
from pages.market_trend import MarketTrendPages
from pages.calendar import CalendarPage


class HomePageTest:

    def test_homepage_loaded(self, create_driver):
        self.home_page = HomePage(create_driver[0])
        self.home_page.open_home_page()
        assert self.home_page.get_page_title() == Content.homePageTitle

    def test_available_market_tabs(self, create_driver):
        self.home_page = HomePage(create_driver[0])
        self.home_page.open_home_page()
        actual_markets_names = self.home_page.get_market_names()
        assert actual_markets_names.sort() == Content.market_tabs.sort()

    @mark.parametrize("market_name", ['US', 'Europe'])
    def test_available_indices_for_markets(self, market_name, create_driver):
        home_page = HomePage(create_driver[0])
        home_page.open_home_page()
        home_page.click_market_name(market_name)
        assert home_page.get_market_names().sort() == Content.market_index[market_name].sort()

    @mark.smoke
    def test_search_stock_and_other_assets(self, create_driver):
        home_page = HomePage(create_driver[0])
        home_page.open_home_page()
        home_page.search_asset('BTC/INR')
        assert home_page.get_search_result_heading() == 'Bitcoin to Indian Rupee'

    def test_follow_index_as_guest(self, create_driver):
        self.home_page = HomePage(create_driver[0])
        self.signin_page = SignInPage(create_driver[0])

        self.home_page.open_home_page()
        self.home_page.follow_index_as_guest()
        self.signin_page.wait_for_signin_page_to_load()

        assert self.signin_page.get_page_title() == 'Sign in - Google Accounts'

    @mark.smoke
    def test_add_event_to_calendar_as_guest(self, create_driver):
        home_page = HomePage(create_driver[0])
        calendarpage = CalendarPage(create_driver[0])

        home_page.open_home_page()
        home_page.add_event_to_calendar()
        calendarpage.wait_for_calendar_tab_to_load(create_driver[1], create_driver[2])

        if create_driver[1] == 'chrome' and 'headless' not in create_driver[2]:
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
    def test_search_market_trends(self, trend_name, expected_title, create_driver):
        home_page = HomePage(create_driver[0])
        market_page = MarketTrendPages(create_driver[0])

        home_page.open_home_page()
        home_page.select_market_trend(trend_name)
        market_page.wait_for_market_trend_page_to_load()

        assert market_page.get_page_title() == expected_title + " - Google Finance"
        assert market_page.is_selected_trend_tab_present(trend_name) is True
        assert market_page.get_selected_trend_heading() == trend_name
