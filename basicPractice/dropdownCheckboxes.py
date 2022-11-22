import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://itera-qa.azurewebsites.net/home/automation')

days = driver.find_elements(By.XPATH,"//*[@type='checkbox' and contains(@id,'day')]")

for day in days:
    if day.get_attribute('id')=='wednesday':
        day.click()

places = Select(driver.find_element(By.XPATH,"//*[@class='custom-select']"))

places.select_by_visible_text('Malta')
time.sleep(2)
places.select_by_value('5')
time.sleep(2)
places.select_by_index(5)
