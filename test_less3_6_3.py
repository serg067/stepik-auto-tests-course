import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture()
def answer():
    answer = math.log(int(time.time()))
    return answer

class TestUFO():
    string = ''
    @pytest.mark.parametrize('lesson', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
    def test_puzzle(self, lesson, browser, answer):
        link = f"https://stepik.org/lesson/{lesson}/step/1"
        browser.get(link)
        time.sleep(4)
        input1 = browser.find_element_by_css_selector('.ember-text-area')
        input1.send_keys(answer)
        button = browser.find_element_by_css_selector('.submit-submission')
        button.click()
        time.sleep(3)
        output_elem = browser.find_element_by_css_selector('.smart-hints__hint')
        output = output_elem.text
        assert output == 'Correct!',\
            f"Произошла ошибка при заполнении формы. {output} != 'Correct!'"
