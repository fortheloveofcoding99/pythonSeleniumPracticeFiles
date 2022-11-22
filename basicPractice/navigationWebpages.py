from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge(executable_path=r"C:\Users\befor\New folder\msedgedriver.exe")

driver.get('https://demoqa.com/browser-windows')

print(driver.title)

time.sleep(5)

driver.get("http://demo.guru99.com/test/newtours/")

print(driver.title)

time.sleep(5)

driver.back()

print(driver.title)

time.sleep(5)

driver.forward()

print(driver.title)

time.sleep(5)

driver.quit()
