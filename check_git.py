from selenium import webdriver
import time

link = "https://www.google.com/?gws_rd=ssl"

try:
    browser = webdriver.Chrome()
    browser.get(link)

finally:
    time.sleep(10)
    browser.quit

