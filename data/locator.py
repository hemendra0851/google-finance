"""
module for locators
"""
from dataclasses import dataclass


@dataclass
class Home:
    """
    dataclass for Home Page locators
    """
    header_logo = "(//header//div)[2]//a[@title='Finance']"
    main_menu = "//div[@aria-label='Main menu']"
    menu_item = "//a[@role='menuitem']//div[text()]"
    menu_portfolio = "//div[@role='heading' and text()='Portfolios']/following-sibling::span"
    menu_watchlist = "//div[@role='heading' and text()='Watchlists']/following-sibling::span"
    menu_settings = "//a[@role='menuitem']//div[text()='Settings']"
    compare_markets_heading = "//span[@id='market-rundown-heading']"
    compare_markets_tabs = \
        "(//span[@id='market-rundown-heading']/parent::div/following-sibling::div)"
    compare_markets_indices = \
        "(((//div[@aria-labelledby='market-rundown-heading']/div)[3]//a)//div[text()])[1]"
    search = "((//div[@data-placeholder='Search for stocks, ETFs & more'])[3]/input)[2]"
    search_options = "//div[@role='option']"
    search_result_heading = "(//main/div/div/div[@role='heading'])[2]"
    sign_in_btn = "(//span[text()='Sign in'])[2]"
    follow_index = ("((//body/c-wiz)[2]//div[@role='main']//div["
                    "@id='smart-watchlist-title']/following-sibling::ul//i)[1]")
    add_to_calendar_icon = \
        ("((((//body/c-wiz)[2]//div[@role='main']//div[text()='Earnings calendar'])[1]"
         "/following-sibling::div)[2]//i/following-sibling::a)[1]")


@dataclass
class SignIn:
    """
    dataclass for Sign In Page locators
    """
    title = "//span[text()='Sign in']"
    email = "//input[@type='email']"


@dataclass
class MarketTrends:
    """
    dataclass for Market Trends Page locators
    """
    page_heading = "//div[text()='Explore market trends']"
    trend_name_tab_item = "(//body/c-wiz)[3]//div[@role='navigation']//a"
    trend_heading = "((//body/c-wiz)[3]//div[@role='main']//span[text()])[1]"
    subtext = ("//span[text()='The stocks or funds with the highest trading volume (in shares) "
               "during the current trading session']")
    shareBtn = "(//span[text()='Share'])[1]"


@dataclass
class Calendar:
    """
    dataclass for Calendar Page locators
    """
    header = "//a[@aria-label='Google Workspace']"
    text = "//h1[contains(text(),'Shareable online calendar')]"
