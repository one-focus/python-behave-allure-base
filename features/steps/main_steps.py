from behave import *

from features.pages.search_results_page import SearchResultsPage


@when('I search for "{text}"')
def step_impl(context, text):
    context.current_page.type_in('search field', text)
    context.current_page.click_on('search button')
    context.current_page = SearchResultsPage(context.driver)
