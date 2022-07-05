import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="c://chromedriver.exe")
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR, "[onclick='jsPrompt()']").click()
#
# time.sleep(5)
# alert_window = driver.switch_to.alert
# print(alert_window.text)
# alert_window.send_keys("welcome")
# #alert_window.accept()
# alert_window.dismiss()

# driver.get("https://the-internet.herokuapp.com/basic_auth")
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
