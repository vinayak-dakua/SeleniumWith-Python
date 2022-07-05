from selenium import webdriver
from selenium.webdriver.common.by import By
ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notification")


driver = webdriver.Chrome(executable_path="c://chromedriver.exe", options=ops)
driver.get("https://whatmylocation.com/")
driver.maximize_window()