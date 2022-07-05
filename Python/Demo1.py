import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="c://chromedriver.exe")
driver.get("https://jeevaorganic.com/")
driver.maximize_window()
time.sleep(30)
driver.find_element_by_class_name("mailpoet_form_close_icon").click()
products = driver.find_elements_by_xpath("//div[@class='box-text text-center']/div[1]/p[2]")
count = 1
for product in products:
    productName = product.text
    print(count, productName)
    count = count + 1
driver.find_element_by_css_selector("[class='icon-search']").click()
driver.find_element_by_css_selector("[id='dgwt-wcas-search-input-1']").send_keys("Jeeva Organic Healthy Dried Cranberries 250g")
time.sleep(3)
driver.find_element_by_css_selector("[class='dgwt-wcas-st-title']").click()
driver.find_element_by_xpath("//button[@name='add-to-cart']").click()
driver.find_element_by_xpath("//span[@class='cart-icon image-icon']/strong").click()
driver.save_screenshot()