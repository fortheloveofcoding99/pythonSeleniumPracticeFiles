from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Edge(executable_path=r"C:\Users\befor\New folder\msedgedriver.exe")

driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.yatra.com/')


links = driver.find_elements(By.TAG_NAME,'a')

print(len(links))

for link in links:
    print(link.text)

driver.find_element(By.LINK_TEXT,'Offers').click()
#
# wait = WebDriverWait(driver, 5)
#
# ele = driver.find_element(By.LINK_TEXT,'Go to current travel information1')
#
# driver.execute_script("arguments[0].click();",ele)