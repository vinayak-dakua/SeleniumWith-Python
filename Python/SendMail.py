from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("c://chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://accounts.google.com/signin/v2/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "[type='email']").send_keys("vinayak.dakua000@gmail.com")
