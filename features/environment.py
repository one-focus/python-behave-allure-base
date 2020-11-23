import configparser

import allure
from selenium import webdriver
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry


# TODO check all context attributes on https://behave.readthedocs.io/en/latest/context_attributes.html#user-attributes
def before_all(context):
    caps = {
        # -- Chrome browser mobile emulation and headless options
        'goog:chromeOptions': {
            # 'mobileEmulation': {'deviceName': 'iPhone X'},
            'args': ['headless']
        }

        # -- Android options
        # "browserName": "android",
        # "version": "9.0",
        # 'selenoid:options': {
        #     'enableVNC': True,
        #     'enableVideo': True
        # }

        # -- Selenoid options
        # 'browserName': 'chrome',
        # 'version': '86.0'
        # 'enableVNC': True,
        # 'enableVideo': True,

    }
    context.driver = webdriver.Chrome(desired_capabilities=caps)
    context.driver.implicitly_wait(5)
    # -- Remote driver
    # context.driver = webdriver.Remote(command_executor='http://0.0.0.0:4444/wd/hub', desired_capabilities=caps)

    # read config
    parser = configparser.ConfigParser()
    parser.read('behave.ini')
    context.config = parser


def before_feature(context, feature):
    # retry failures
    for scenario in feature.scenarios:
        # if "flaky" in scenario.effective_tags:
            patch_scenario_with_autoretry(scenario, max_attempts=2)


def before_scenario(context, scenario):
    context.driver.delete_all_cookies()


def after_step(context, step) -> None:
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(),
                      name='bug.png',
                      attachment_type=allure.attachment_type.PNG)


def after_all(context):
    context.driver.quit()
