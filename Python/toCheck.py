import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="c://chromedriver.exe")
driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/Create")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()

driver.find_element(By.XPATH,"//div[@class='card-body']/div[10]/div[2]/div/div/div/div").click()
