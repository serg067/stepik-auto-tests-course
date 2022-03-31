import time
from selenium import webdriver
import pytest


class TestOnlineShop():
    def test_locales_shop(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        time.sleep(2)
        button = browser.find_element_by_css_selector('.btn-add-to-basket')
        assert button is None, f"Expected result: Произошла ошибка при поиске кнопки. Кнопка не найдена."