import math
from selenium import webdriver
import time
link = "http://suninjuly.github.io/alert_accept.html"
def calc(x):
    return math.log(abs(12*math.sin(x)))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_temp = browser.find_element_by_id("input_value")
    x = int(x_temp.text)
    result = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(result)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()




finally:
    time.sleep(5)
    browser.quit()
