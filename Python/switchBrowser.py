from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="c://chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

print(driver.current_window_handle)

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
ides = (driver.window_handles)
driver.switch_to.window(ides[1])
print(driver.title)
driver.close()