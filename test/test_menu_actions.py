from pytest import mark
from pages.home import HomePage
from pages.main_menu import MainMenu
from pages.sign_in import SignInPage


@mark.usefixtures('create_driver')
class MainMenuTest:

    def test_main_menu_opened(self):
        home_page = HomePage(self.driver)
        main_menu = MainMenu(self.driver)

        home_page.open_home_page()
        main_menu.open_main_menu()
        assert main_menu.is_main_menu_opened() is True

    @mark.smoke
    def test_available_menu_items(self):
        home_page = HomePage(self.driver)
        main_menu = MainMenu(self.driver)

        home_page.open_home_page()
        main_menu.open_main_menu()
        actual_menu_items = main_menu.get_menu_items()
        assert ({'Home', 'Market trends', 'Settings', 'Send feedback'}
                .issubset(set(actual_menu_items)))

    @mark.smoke
    def check_create_portfolio_as_guest(self):
        home_page = HomePage(self.driver)
        main_menu = MainMenu(self.driver)
        signin_page = SignInPage(self.driver)

        home_page.open_home_page()
        main_menu.open_main_menu()
        main_menu.open_portfolio_menu_item()
        signin_page.wait_for_signin_page_to_load()
        assert signin_page.get_page_title() == 'Sign in - Google Accounts'
