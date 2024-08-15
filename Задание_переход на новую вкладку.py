from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/redirect_accept.html"


try:

    """Запуск браузера и открытие сайта."""
    browser = webdriver.Chrome()
    browser.get(link)

    """Нажать на кнопку"""
    input_sub = browser.find_element(By.CSS_SELECTOR, "button.btn")
    input_sub.click()

    """Переключиться на новую вкладку"""
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    """Получить число с ответом."""
    x = browser.find_element(By.ID, "input_value")
    x = int(x.text)
    res = math.log(abs(12*math.sin(x)))
    """ВВвод числа с ответом."""
    input_res = browser.find_element(By.CSS_SELECTOR, "[name = 'text']")
    input_res.send_keys(res)

    """Нажать кнопку 'Submit'."""
    input_sub = browser.find_element(By.CSS_SELECTOR, "button.btn")
    input_sub.click()

finally:
    time.sleep(5)
    browser.close()
    browser.quit()
##    pass
