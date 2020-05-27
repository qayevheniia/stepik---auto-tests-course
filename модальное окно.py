from selenium import webdriver
import time
import math

def calc(x):
     return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn.btn-primary").click()
    confirm = browser.switch_to.alert #модальное окна
    confirm.accept() #согласиться с модальном окном

    formula = browser.find_element_by_id("input_value")
    x = formula.text
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    option1 = browser.find_element_by_css_selector("button.btn.btn-primary")
    option1.click()



finally:
    time.sleep(10)
    browser.quit()

# надеюсь это выдет

