from datetime import datetime, timezone, timedelta
from time import sleep

from behave import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

import gmail
import pages

use_step_matcher('re')


@when('click on (?P<element_name>[^"]*?)(?: in "(?P<section>[^"]*?)")?')
def click_on(context, element_name, section=None):
    sleep(0.5)
    if section:
        section_xpath = context.page.get_element_by_name(section)[1]
        element = context.page.get_element_by_name(element_name)
        if element[0] == 'xpath':
            try:
                context.driver.find_element_by_xpath(f'{section_xpath}{element[1]}').click()
            except NoSuchElementException:
                raise RuntimeError(f'Cannot click {element_name} in {section}')
        else:
            raise RuntimeError(f'Use XPATH for "{element_name}" locator')
    else:
        context.page.click_on(element_name)


@when('enter "(?P<text>[^"]*)" in (?P<field_name>[^"]*)(?: in "(?P<section>[^"]*?)")?')
def enter_in(context, text, field_name, section=None):
    if 'generated' in text:
        time = datetime.now(timezone.utc) + timedelta(hours=3)
        context.values[text] = text = text.replace("generated", f'{time.strftime("%d.%m.%Y %H:%M:%S")}')
    if section:
        section_xpath = context.page.get_element_by_name(section)[1]
        element = context.page.get_element_by_name(field_name)
        if element[0] == 'xpath':
            try:
                element = context.driver.find_element_by_xpath(f'{section_xpath}{element[1]}')
                element.clear()
                element.send_keys(text)
            except NoSuchElementException:
                raise RuntimeError(f'Cannot find "{field_name}" in "{section}". With xpath {section_xpath}{element[1]}')
        else:
            raise RuntimeError(f'Use XPATH for "{field_name}" locator')
    else:
        context.page.enter_in(field_name, text)


@then('text in "(?P<element>.*)" is (?P<option>.*)')
def text_in_element_is_state(context, element, option):
    if element == 'body': element = By.TAG_NAME, 'body'
    if 'displayed' in option:
        assert context.page.is_element_displayed(element), f'Element {element} is not displayed'
    elif 'not displayed' in option:
        assert context.page.is_element_invisible(element), f'Element {element} is displayed'
    elif 'enabled' in option:
        assert context.page.is_element_displayed(element), f'Element {element} is disabled'
    elif 'disabled' in option:
        assert not context.page.is_element_displayed(element), f'Element {element} is enabled'
    else:
        element_text = context.page.get_text(element)
        if option not in element_text:
            raise RuntimeError(f'Text for element {element}: "{element_text}". Expected: {option}')


@step('page (?P<page_name>.*) is opened')
def init_screen(context, page_name):
    """Instantiating verifies that we're on that page"""
    context.page = pages.factory(page_name)(context.driver)


@given('open "(?P<page_name>.*)" (?P<option>page|url)')
def open_page(context, page_name, option):
    context.driver.get(page_name if page_name.startswith('http') else f'https://{page_name}')
    context.page = pages.factory(page_name)(context.driver) if pages.factory(page_name) else None


@when('remember "(?P<key>.*)" as "(?P<value>.*)"')
def remember(context, key, value):
    context.values[value] = context.page.get_text(key)


@then('email with "(?P<query>.*)" contains "(?P<text>.*)" in "(?P<seconds>.*)" sec')
def email_with_subject_contains_text_in_sec(context, query, text, seconds):
    query = get_context_value(context, query)
    text = get_context_value(context, text)
    sleep(5)
    for i in range(10):
        messages = gmail.search_message(query)
        if len(messages) < 1:
            sleep(int(seconds) / 10)
        elif len(messages) == 1:
            message = messages[0].replace('\r\n', ' ').replace('\xa0', ' ')
            break
        else:
            RuntimeError(f'{len(messages)} found for "{query}". Expected: 1. Change search parameters')
    else:
        raise RuntimeError(f'No message with text "{query}" in {seconds} sec')

    errors = []
    for search_text in text.split(';'):
        if search_text not in message:
            errors.append(f'"{search_text}" не найден в "{message}"')
    if errors:
        raise RuntimeError(errors)


def get_context_value(context, text):
    for value in context.values:
        if value in text:
            text = text.replace(value, context.values[value])
    return text


@when("wait (?P<seconds>.*) sec")
def wait_for_sec(context, seconds):
    sleep(int(seconds))


@when("open last tab")
def open_last_tab(context):
    context.driver.switch_to_window(context.driver.window_handles[-1])
