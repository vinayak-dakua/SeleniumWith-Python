from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#ser_obj = Service("c://chromedriver.exe")
#driver = webdriver.Chrome(service=ser_obj)
driver = webdriver.Chrome(executable_path="c://chromedriver.exe")
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()
drop_down_ele = driver.find_element(By.XPATH,"//select[@name='country_id']")
drop_Down = Select(drop_down_ele)
# drop_Down.select_by_visible_text("India")
# drop_Down.select_by_value("2")
# drop_Down.select_by_index(3)
# alloptions = drop_Down.options
# print(len(alloptions))
# for opt in alloptions:
#     print(opt.text)