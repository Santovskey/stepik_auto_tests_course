from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.XPATH, "//div//div//span[2]")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.XPATH, "//div//div//input")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[for=robotCheckbox]")
    option1.click()
    option1 = browser.find_element(By.CSS_SELECTOR, "[for=robotsRule]")
    option1.click()
    option1 = browser.find_element(By.XPATH, "//div//button")
    option1.click()


finally:
    time.sleep(5)
    browser.quit()
