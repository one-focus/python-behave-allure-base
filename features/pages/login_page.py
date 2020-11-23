from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage


# Inherits from BasePage
class LoginPage(BasePage):

    @property
    def _elements_map(self):
        return {
            'username field': (By.ID, 'wpName1'),
            'password field': (By.ID, 'wpPassword1'),
            'login button': (By.ID, 'wpLoginAttempt')
        }

    def _verify_page(self):
        self.on_this_page('username field', 'password field', 'login button')
