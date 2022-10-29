from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    a = int(x_element.text) + int(y_element.text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(a))  # ищем элемент с текстом a
    browser.find_element(By.CSS_SELECTOR, ".btn-default").click()

    time.sleep(1)

finally:

    print()
    print("Yeah! That's it!")
    print()
    time.sleep(5)
    browser.quit()
