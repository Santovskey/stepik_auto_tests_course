from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
values = ["Ivan", "Rogov", "foo@mail.ru"]

try:

    """Запуск браузера и открытие сайта."""
    browser = webdriver.Chrome()
    browser.get(link)

    """Заполнение формы."""
    for num, val in enumerate(values, 1):
        input_val = browser.find_element(By.XPATH, f"//div//div//input[{num}]")
        input_val.send_keys(val)

    """Загрузка файла."""
    input_file = browser.find_element(By.ID, "file")
    file = os.path.abspath(os.path.dirname('test.txt'))
    input_file.send_keys(file + '\\test.txt')

    """Нажать кнопку 'Submit'."""
    input_sub = browser.find_element(By.CSS_SELECTOR, "button.btn")
    input_sub.click()

finally:
    time.sleep(5)
    browser.quit()
##    pass
