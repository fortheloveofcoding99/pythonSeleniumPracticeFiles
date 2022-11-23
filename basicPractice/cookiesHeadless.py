import time

from selenium import webdriver
from selenium.webdriver.common.by import By

ops = webdriver.ChromeOptions()
#ops.headless=True
driver = webdriver.Chrome(options=ops)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://www.lufthansa.com/in/en/homepage')
driver.find_element(By.ID,'cm-acceptAll').click()
cookies = driver.get_cookies()
size = len(cookies)
print(size)
driver.add_cookie({'name':'domain','value':'.wwws.airfrance.fr/splash'})
size = len(cookies)
print(size)

time.sleep(3)
driver.quit()
#https://wwws.airfrance.fr/splash