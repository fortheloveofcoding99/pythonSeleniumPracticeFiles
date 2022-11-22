from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://testautomationpractice.blogspot.com/')

product = Select(driver.find_element(By.ID,'products'))

product.select_by_visible_text('Yahoo')


driver.switch_to.frame('frame-one1434677811')

