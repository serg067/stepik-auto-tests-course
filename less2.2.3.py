from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
link = "http://suninjuly.github.io/selects2.html"
def calc(x,y):
    return str(int(x)+int(y))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id("num1").text
    y_element = browser.find_element_by_id("num2")
    num2 = y_element.text
    result = calc(num1,num2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
