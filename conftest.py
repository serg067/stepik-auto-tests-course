import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help='Choose language: ru, en, ... (etc.)')
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nStart Chrome browser for test ...")
        browser = webdriver.Chrome(options=options)
    else:
        print('Давай без экспериментов. Поддерживается только Chrome')

    yield browser
    print("\nquit browser..")
    browser.quit()