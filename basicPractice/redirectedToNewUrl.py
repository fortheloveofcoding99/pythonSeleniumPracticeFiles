from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(executable_path=r"C:\Users\befor\New folder\msedgedriver.exe")

driver.get("https://demoqa.com/browser-windows")

print(driver.title)

print(driver.current_url)

driver.find_element(By.ID,'tabButton').click()

time.sleep(2)

driver.close()

time.sleep(2)

driver.quit()