from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(executable_path=r"C:\Users\befor\New folder\msedgedriver.exe")

driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://the-internet.herokuapp.com/windows')

print(driver.current_window_handle)

driver.find_element(By.LINK_TEXT,'Click Here').click()

print(driver.current_window_handle)

handles = driver.window_handles

print(handles)

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)