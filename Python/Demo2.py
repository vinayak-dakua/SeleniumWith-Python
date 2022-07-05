from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

ser_obj = Service("c://chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)
driver.get("https://demo.nopcommerce.com/")
#links = driver.find_elements(By.TAG_NAME,'a')

links = driver.find_elements(By.XPATH,'//a')
print(len(links))

for link in links:
    print(link.text)
driver.close()