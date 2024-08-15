import selenium
from selenium.webdriver.common.by import By
import time


link = 'https://suninjuly.github.io/selects2.html'

try:
    browser = selenium.webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    result = int(num1.text) + int(num2.text)
    input_res = browser.find_element(By.CLASS_NAME, "custom-select")
    input_res.send_keys(result)
    clik_sub = browser.find_element(By.CSS_SELECTOR, "button.btn")
    clik_sub.click()

finally:
    time.sleep(5)
    browser.quit()
