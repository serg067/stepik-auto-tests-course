import math
from selenium import webdriver
import time
link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector('#treasure')
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("input[value='robots']")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
