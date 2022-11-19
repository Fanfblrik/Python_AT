import time
import pytest
from selenium.webdriver.common.by import By
import math

login = 'georg-maks@mail.ru'
password = 'jora1999'
links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1']


@pytest.mark.parametrize('link', links)
def test_correct_feedback(browser, link):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#ember32").click()
    browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(login)
    browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(password)
    browser.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()
    time.sleep(3)
    browser.find_element(By.TAG_NAME, "textarea").send_keys(str(math.log(int(time.time()) - 0.2)))
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    browser.find_element(By.CSS_SELECTOR, ".again-btn").click()
    elem = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
    result = elem.text
    assert result == "Correct!"
