import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',  # Default to Chrome, can stay NONE
                     help="Choose browser: Chrome or Safari")
    parser.addoption('--language', action='store', default='ru',  # Default to English
                     help="Choose language: ")

@pytest.fixture
def language(request):
    return request.config.getoption("--language")

@pytest.fixture
def stepik_browser(request):
    browser_name = request.config.getoption("browser_name").lower()
    language = request.config.getoption("--language")

    stepik_browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        stepik_browser = webdriver.Chrome(options=options)
        print("\nstart chrome browser for test..")
    elif browser_name == "safari":
        print("\nstart safari browser for test..")
        stepik_browser = webdriver.Safari()
    else:
        raise pytest.UsageError("--browser_name should be chrome or safari")
    stepik_browser.set_window_size(1920, 1080)


    yield stepik_browser

    print("\nquit browser..")
    stepik_browser.quit()

