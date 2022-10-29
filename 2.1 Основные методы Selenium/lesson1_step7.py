from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
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

    print()
    print("Yeah! That's it!")
    print()
    time.sleep(5)
    browser.quit()
