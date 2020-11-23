from behave import *

from features.pages.main_page import MainPage
from pages import LoginPage


@given('I open {page_name} page')
def step_impl(context, page_name):
    base_url = context.config.get('settings', 'base_url')
    if page_name == "home":
        context.driver.get(f'{base_url}')
        context.current_page = MainPage(context.driver)
    elif page_name == "login":
        context.driver.get(f'{base_url}/w/index.php?title=Special:UserLogin')
        context.current_page = LoginPage(context.driver)


@when('I log in')
def step_impl(context):
    context.current_page.type_in('username field', context.config.get('user', 'username'))
    context.current_page.type_in('password field', context.config.get('user', 'password'))
    context.current_page.click_on('login button')
    context.current_page = MainPage(context.driver)  # Verify user is on main page


# use of data table example
@then('I see validation message for')
def step_impl(context):
    for row in context.table:
        context.execute_steps(f'''
        When I type "{row['username']}" in username field
        When I type "{row['password']}" in password field
        When I click on login button
        Then I see "{row['text']}" on the page
        ''')
