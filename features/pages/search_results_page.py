from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):

    @property
    def _elements_map(self):
        return {
            "topic title": (By.ID, "firstHeading"),
            'search field': (By.ID, 'searchInput'),
            'search button': (By.ID, 'searchButton')
        }

    def _verify_page(self):
        self.on_this_page("topic title")

    def get_topic_title(self):
        return self.get_text("topic title")
