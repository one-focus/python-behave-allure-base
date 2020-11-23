import abc

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        pass

    def on_this_page(self, *args):
        for element_name in args:
            self.get_element(element_name)

    def click_on(self, element_name):
        self.get_clickable_element(element_name).click()

    def type_in(self, element_name, text):
        self.get_element(element_name).clear()
        self.get_element(element_name).send_keys(text)

    def get_text(self, element_name):
        return self.get_element(element_name).text

    @property
    @abc.abstractmethod
    def _elements_map(self) -> dict:
        return {}

    def get_element(self, element_name, timeout=5):
        locator = self._elements_map.get(element_name)
        if locator is None:
            raise RuntimeError(f'Failed to find element "{element_name}" at "elements_map" dictionary on screen')
        expected_condition = ec.presence_of_element_located(locator)
        return WebDriverWait(self.driver, timeout).until(
            expected_condition, message=f'Unable to locate element: "{element_name}"')

    def get_clickable_element(self, element_name, timeout=5):
        locator = self._elements_map.get(element_name)
        if locator is None:
            locator = (By.XPATH, f'//*[text() = "{element_name}"]')
        expected_condition = ec.element_to_be_clickable(locator)
        return WebDriverWait(self.driver, timeout).until(
            expected_condition, message=f'Unable to locate element: {element_name}')
