from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    confirm = browser.switch_to.alert                           # модальное окно
    confirm.accept()                                            # тык ОК в модальном окне
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    input3 = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    input3.click()
    alert = browser.switch_to.alert
    print(browser.switch_to.alert.text)
    alert.accept()

    time.sleep(1)

finally:

    time.sleep(5)
    browser.quit()
