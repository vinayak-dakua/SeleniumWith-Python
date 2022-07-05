import time
from time import sleep

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#  ---------- EDIT ----------
email = 'vinayak.dakua000@gmail.com'
password = '9826193111'
#  ---------- EDIT ----------

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
url = "www.google.com"
driver.get(url)


# wait.until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(email)
# driver.find_element(By.XPATH,"//*[text()='Next']").click()
# wait.until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys(password)
# driver.find_element(By.XPATH,"//*[text()='Next']").click()
# time.sleep(10)
# driver.find_element(By.XPATH,"//div[contains(text(),'Compose')]").click()
# time.sleep(10)
# driver.find_element(By.XPATH,"//input[@id=':s9']").send_keys("praveen.dakua@gmail.com ")
# time.sleep(30)
