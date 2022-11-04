from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# with open("test.txt", "w") as file:
#     content = file.write("automationbypython")  # create test.txt file
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("mail@Smolensk.ru")
    element = browser.find_element(By.NAME, "file")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

    time.sleep(1)

finally:

    time.sleep(10)
    browser.quit()
