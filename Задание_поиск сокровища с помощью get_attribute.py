from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    img_klad = browser.find_element(By.XPATH, "//img")
    x = img_klad.get_attribute("valuex")
    res = calc(x)

    input_res = browser.find_element(By.XPATH, "//input")
    input_res.send_keys(res)

    check_off = browser.find_element(By.XPATH, "//div[2]//input")
    check_off.click()

    radio_but = browser.find_element(By.XPATH, "//div[2]//input[3]")
    radio_but.click()

    but_ok = browser.find_element(By.CSS_SELECTOR, "button.btn")
    but_ok.click()


finally:
    time.sleep(10)
    browser.quit()

