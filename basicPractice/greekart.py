from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

service_obj = Service("C:/Users/befor/New folder/msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(3)
url ='https://rahulshettyacademy.com/seleniumPractise/#/'
driver.get(url)
driver.find_element(By.CSS_SELECTOR,'.search-keyword').send_keys('ca')
items = driver.find_elements(By.CSS_SELECTOR,"//div[@class='products']/div")
for item in items:
        driver.find_element(By.XPATH,'div/button').click()

driver.close()