import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    options = Options()

    # отключается менеджер паролей Chrome
    chrome_prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }

    options.add_experimental_option("prefs", chrome_prefs)

    # настройки браузера
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()