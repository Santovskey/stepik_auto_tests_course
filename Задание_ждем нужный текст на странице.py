from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

try:
    res = WebDriverWait(browser, '12').until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    """Получить число с ответом."""
    x = browser.find_element(By.ID, "input_value")
    x = int(x.text)
    res = math.log(abs(12*math.sin(x)))
    """ВВвод числа с ответом."""
    input_res = browser.find_element(By.CSS_SELECTOR, "[name = 'text']")
    input_res.send_keys(res)

    """Нажать кнопку 'Submit'."""
    input_sub = browser.find_element(By.CSS_SELECTOR, "[id='solve']")
    input_sub.click()

    assert True
finally:
    time.sleep(10)
    browser.quit()