from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/cats.html")

# time.sleep(1)
button = browser.find_element_by_id("button")
# button.click()

# time.sleep(2)
# message = browser.find_element_by_id("verify_message")

# assert "successful" in message.text

time.sleep(3)
browser.quit()
