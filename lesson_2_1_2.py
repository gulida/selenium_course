from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код

    people_radio = browser.find_element_by_id("peopleRule") 
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    # assert robots_checked is None
    assert robots_checked is not None, "Robots radio is not selected by default"
    print("value of robots radio: ", robots_checked)
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()