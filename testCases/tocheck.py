import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "strong")))
driver.find_element(By.ID, "Email").clear()
driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")
driver.find_element(By.XPATH,"//button[@class='button-1 login-button']").click()
time.sleep(5)
txt = driver.title
print(txt)
driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()


