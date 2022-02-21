import math
from selenium import webdriver
import time
link = "http://suninjuly.github.io/execute_script.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_temp = browser.find_element_by_id("input_value")
    x = x_temp.text
    result = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(result)
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()
    option2 = browser.find_element_by_css_selector("input[value='robots']")
    option2.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
