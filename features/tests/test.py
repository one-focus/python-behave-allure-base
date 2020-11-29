from appium import webdriver

# настройки
caps = {
   'platformName': 'Android',
   'version': '9.0',
   'app': 'https://github.com/sozdai/behave-sample/raw/main/com.instagram.android.apk',
   'appActivity': 'com.instagram.mainactivity.LauncherActivity',
   'appPackage': 'com.instagram.android',
}


capabilities = {
    "browserName": "chrome",
    "browserVersion": "85.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True
    }
}

# создание
driver = webdriver.Remote("http://0.0.0.0:4723/wd/hub", capabilities)
driver.implicitly_wait(5)

assert "Log In" in driver.page_source


