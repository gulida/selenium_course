from selenium import webdriver
import time
import math

def calc (x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")   
    button.click()

    new_window = browser.window_handles[1]
    # first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    button = browser.find_element_by_tag_name("button")   
    button.click()

finally:
    time.sleep(5)
    browser.quit()