import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestAbs(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_form1(self):
        browser = self.driver
        browser.get('http://suninjuly.github.io/registration1.html')

        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
        input3.send_keys("Smolensk")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Should be another text')

    def test_form2(self):
        browser = self.driver
        browser.get('http://suninjuly.github.io/registration2.html')

        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
        input3.send_keys("Smolensk")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'Should be another text')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
