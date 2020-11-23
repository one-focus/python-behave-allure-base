from .login_page import LoginPage
from .main_page import MainPage
from .search_results_page import SearchResultsPage

page_map = {
    "login": LoginPage,
    "main": MainPage,
    "search results": SearchResultsPage
}


def factory(page_name: str):
    """Encapsulate screen creation"""
    return page_map[page_name]
