import time
from selenium.webdriver.common.by import By


def test_check_button_add_to_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    time.sleep(30)           # оставил требуемые в условии 30 секунд, но лучше уменьшить до 5, чтоб не ждать
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
