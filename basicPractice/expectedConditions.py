from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Edge(executable_path=r"C:\Users\befor\New folder\msedgedriver.exe")

driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://demoqa.com/dynamic-properties')

wait = WebDriverWait(driver,7)

ele = driver.find_element(By.ID,'enableAfter')

et = wait.until(EC.element_to_be_clickable(ele))

et.click()

nb = driver.find_element(By.ID,'colorChange')

print(nb.text)

print(driver.title)







#driver.quit()

