import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_cart_button(stepik_browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    stepik_browser.get(url)

    button = WebDriverWait(stepik_browser, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='add_to_basket_form']/button"))
        )
    assert button is not None, "Add to Cart button is not visible on the product page."
    print(f"Test result: button with text <{button.text}> is visible on page")
    time.sleep(2)

def test_language(language):
    assert language in ["en", "ru", "es"], f"Unsupported language: {language}"
    print(f"Running test with language: {language}")