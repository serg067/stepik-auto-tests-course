from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
    return math.log(abs(12*math.sin(x)))


try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)
    button = browser.find_element_by_id("book")
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"),"$100")
    )
    button.click()
    x_temp = browser.find_element_by_id("input_value")
    x = int(x_temp.text)
    result = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(result)
    button2 = browser.find_element_by_id("solve")
    button2.click()

finally:
    time.sleep(5)
    browser.quit()
