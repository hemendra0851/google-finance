"""
conftest.py file to create pytest fixtures
"""

from pytest import fixture
from selenium.webdriver import Chrome
from selenium.webdriver import Edge
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


@fixture(params=['chrome'])
def create_driver(request):
    """
    Creating fixture to get WebDriver
    """
    if request.param == 'chrome':
        options = ChromeOptions()
        options = add_options(options)
        driver = Chrome(options=options)
    elif request.param == 'edge':
        options = EdgeOptions()
        options = add_options(options)
        driver = Edge(options=options)
    else:
        raise NameError('invalid browser name')

    driver.implicitly_wait(10)
    request.cls.driver = driver
    request.cls.browser = request.param
    request.cls.options = options.arguments
    yield driver, request.param, options.arguments
    driver.quit()


def add_options(options):
    """
    function to add webdriver options
    """
    options.add_argument('guest')
    options.add_argument('window-size=1920x1080')
    options.add_argument('headless')
    options.add_argument('disable-gpu')
    options.add_argument('no-sandbox')
    options.add_argument('start-maximized')
    options.add_argument("log-level=3")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('detach', True)

    return options
