from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    input1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    input1.click()
    input2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    input2.click()
    input3 = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    input3.click()

    time.sleep(1)

finally:

    time.sleep(5)
    browser.quit()
