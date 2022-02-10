import os
import math
from selenium import webdriver
import time
link = "http://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector('.form-group input:nth-of-type(1)')
    input1.send_keys("Имя")
    input2 = browser.find_element_by_css_selector('.form-group input:nth-of-type(2)')
    input2.send_keys("Фамилия")
    input3 = browser.find_element_by_css_selector('.form-group input:nth-of-type(3)')
    input3.send_keys("Почта")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'kosmos.jpg')
    button = browser.find_element_by_id("file")
    button.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
