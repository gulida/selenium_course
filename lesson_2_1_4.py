from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код

    num1_element = browser.find_element_by_id('num1')
    num2_element = browser.find_element_by_id('num2')

    x = num1_element.text
    y = num2_element.text
    sum = str(str(int(x) + int(y)))


    print('Summ of X and Y', sum)
    # browser.find_element_by_tag_name("select").click()
    # browser.find_element_by_css_selector("[value=sum]").click()

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum) 

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()