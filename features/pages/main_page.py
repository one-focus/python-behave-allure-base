from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):

    @property
    def _elements_map(self):
        return {
            "top banner": (By.ID, 'mp-topbanner'),
            'search field': (By.ID, 'searchInput'),
            'search button': (By.ID, 'searchButton')
        }

    def _verify_page(self):
        self.on_this_page('top banner')
