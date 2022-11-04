from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)                                  # говорим WebDriver ждать все элементы в течение 5 секунд

try:
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.CSS_SELECTOR, "#book").click()
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    input3 = browser.find_element(By.CSS_SELECTOR, "#solve")
    input3.click()
    alert = browser.switch_to.alert
    print(browser.switch_to.alert.text)
    alert.accept()

    time.sleep(1)

finally:

    time.sleep(5)
    browser.quit()
