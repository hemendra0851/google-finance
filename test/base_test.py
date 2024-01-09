from pytest import mark
from pages.home import HomePage
from pages.sign_in import SignInPage
from pages.market_trend import MarketTrendPages
from pages.calendar import CalendarPage


@mark.usefixtures("create_driver")
class TestBase:

    def __init__(self):
        self.home_page = HomePage(self.driver)
        self.signin_page = SignInPage(self.driver)
        self.calendarpage = CalendarPage(self.driver)
        self.market_page = MarketTrendPages(self.driver)
