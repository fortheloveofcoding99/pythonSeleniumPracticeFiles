from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(executable_path=r"C:\Users\befor\New folder\msedgedriver.exe")

driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://demoqa.com/automation-practice-form')

vorname = driver.find_element(By.ID,'firstName')

print(vorname.is_displayed())

print(vorname.is_enabled())

radio_button = driver.find_element(By.XPATH,"//*[@id='genterWrapper']/div[2]/div[1]/label")

print(radio_button.is_selected())

driver.quit()

