import pytest
from selenium.webdriver.common.by import By


def test_find_elements(browser):
    browser.get("https://www.saucedemo.com/")

    # Поиск по основным локаторам
    login_button_by_id = browser.find_element(By.ID, "login-button")
    login_button_by_id = browser.find_element(By.NAME, "login-button")
    login_button_by_id = browser.find_element(By.CLASS_NAME, "submit-button")
    login_button_by_id = browser.find_elements(By.TAG_NAME, "input")

    # Авторизация
    username_field = browser.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")
    password_field = browser.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")
    login_button_by_id[2].click()

    # Поиск по ссылке
    product_name = browser.find_element(By.LINK_TEXT, "Sauce Labs Backpack")
    product_name = browser.find_element(By.PARTIAL_LINK_TEXT, "Sauce Lab")

    # Поиск по XPATH
    button_add_to_cart = browser.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
    button_add_to_cart = browser.find_element(By.XPATH, "//button[text() = 'Add to cart']")
    button_add_to_cart = browser.find_element(By.XPATH, "//button[contains(@data-test, 'add-to-car')]")
    button_add_to_cart = browser.find_element(By.XPATH, "//button[contains(text(), 'Add t')]")

    # Поиск по осям XPath:

    parent_button_div = browser.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']/parent::div")
    child_pricebar_item_price = browser.find_element(By.XPATH, "//div[@class='pricebar']/child::div")
    ancestor_button_div = browser.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']/ancestor::div")
    descendant_pricebar_button = browser.find_element(By.XPATH, "//div[@class='pricebar']/descendant::button")
    following_sibling = browser.find_element(By.XPATH, "//div[@class='pricebar']/descendant::button/preceding-sibling::div/following-sibling::button")
    preceding_sibling = browser.find_element(By.XPATH, "//div[@class='pricebar']/descendant::button/preceding-sibling::div")

    # Поиск с условием and:
    button_add_to_cart = browser.find_element(By.XPATH, "//button[text() = 'Add to cart' and @name='add-to-cart-sauce-labs-bolt-t-shirt']")

    # CSS - селекторы:
    button_add_to_cart_2 = browser.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light")
    button_add_to_cart_2 = browser.find_elements(By.CSS_SELECTOR, ".btn")
    button_add_to_cart_2 = browser.find_elements(By.CSS_SELECTOR, ".btn.btn_primary.btn_small.btn_inventory")
    button_add_to_cart_2 = browser.find_element(By.CSS_SELECTOR, "[data-test = 'add-to-cart-sauce-labs-bike-light']")
    button_add_to_cart_2 = browser.find_element(By.CSS_SELECTOR, "button")
    button_add_to_cart_2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_add_to_cart_2 = browser.find_element(By.CSS_SELECTOR, ".primary_header .bm-burger-button")
    button_add_to_cart_2 = browser.find_element(By.CSS_SELECTOR, "[aria-label ~= 'details']")
    button_add_to_cart_2 = browser.find_element(By.CSS_SELECTOR, "[data-test |= 'item']")
    button_add_to_cart_2 = browser.find_element(By.CSS_SELECTOR, "[id ^= 'item']")
    button_add_to_cart_2 = browser.find_element(By.CSS_SELECTOR, "[class $= 'img']")
    button_add_to_cart_2 = browser.find_element(By.CSS_SELECTOR, "[alt *= 'Labs']")
