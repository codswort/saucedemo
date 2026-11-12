import pytest
from selenium.webdriver.common.by import By

@pytest.mark.basic
def test_order(browser):
    browser.get("https://www.saucedemo.com/")

    username_field = browser.find_element(By.ID, "user-name")
    username_field.send_keys("standard_user")
    password_field = browser.find_element(By.ID, "password")
    password_field.send_keys("secret_sauce")
    login_button_by_id = browser.find_element(By.ID, "login-button")
    login_button_by_id.click()

    choose = browser.find_element(By.XPATH, "//div[@data-test = 'inventory-item-name' and contains(text(), 'Red')]")
    choose.click()
    buy = browser.find_element(By.CSS_SELECTOR, "[data-test = 'add-to-cart']")
    buy.click()
    bag = browser.find_element(By.CSS_SELECTOR, "[data-test = 'shopping-cart-badge']")
    bag.click()

    text_of_order = browser.find_element(By.XPATH, "//div[text() = 'Test.allTheThings() T-Shirt (Red)']")
    cost_of_order = browser.find_element(By.XPATH, "//div[@class = 'inventory_item_price']")

    assert text_of_order.text == "Test.allTheThings() T-Shirt (Red)" and cost_of_order.text == "$15.99", "Название товара и цена должны быть правильными"
