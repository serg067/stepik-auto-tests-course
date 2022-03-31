from selenium import webdriver
import unittest
import time

class TestFillForm(unittest.TestCase):
    def test_fill_form1(self):
        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys("Имя")
        input2 = browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys("Фамилия")
        input3 = browser.find_element_by_css_selector('.first_block .third')
        input3.send_keys("Почта")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, 'Произошла ошибка при заполнении формы.')


    def test_fill_form2(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys("Имя")
        input2 = browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys("Фамилия")
        input3 = browser.find_element_by_css_selector('.first_block .third')
        input3.send_keys("Почта")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, 'Произошла ошибка при заполнении формы.')

unittest.main()