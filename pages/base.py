import time
from datetime import datetime
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)
        self._action = ActionChains(driver)

    def get_page_title(self):
        return self._driver.title

    def find_element(self, locator):
        el = self._wait.until(expected_conditions.element_to_be_clickable((By.XPATH, locator)))
        return el

    def find_elements(self, locator):
        el = self._driver.find_elements(By.XPATH, locator)
        return el

    def click(self, locator):
        el = self.find_element(locator)
        self._action.move_to_element(el)
        time.sleep(0.5)
        el.click()

    def input_text(self, locator, txt):
        el = self.find_element(locator)
        self._action.move_to_element(el)
        time.sleep(0.5)
        el.send_keys(txt)

    def wait_until_element_is_visible(self, locator):
        # self.save_screenshot()
        self._wait.until(expected_conditions.visibility_of_element_located((By.XPATH, locator)))

    def wait_until_element_not_visible(self, locator):
        # self.save_screenshot()
        self._wait.until(expected_conditions.invisibility_of_element_located((By.XPATH, locator)))

    def wait_until_title_contains(self, title):
        self._wait.until((expected_conditions.title_contains(title)))

    def save_screenshot(self):
        self._driver.save_screenshot("results/img_" + self.get_timestamp() + ".png")

    @staticmethod
    def get_timestamp():
        timestamp = datetime.now().strftime("%y%m%d_%H%M%S%f")
        return timestamp
