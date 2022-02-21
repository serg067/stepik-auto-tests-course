import math
from selenium import webdriver
import time
link = "https://wmtestcustom8.webim.ru/"
login = 'admin@wmtc8.ru'
password = 'password'


try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(10)
    input1 = browser.find_element_by_id("login_or_email")
    input1.send_keys(login)
    input2 = browser.find_element_by_id("password")
    input2.send_keys(password)
    button = browser.find_element_by_css_selector("form  .btn-primary")
    button.click()
    time.sleep(10)

finally:
    time.sleep(5)
    browser.quit()
