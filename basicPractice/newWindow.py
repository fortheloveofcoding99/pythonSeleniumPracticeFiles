import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://testautomationpractice.blogspot.com/')
wait = WebDriverWait(driver,10)

driver.find_element(By.XPATH, "//*[@id='Wikipedia1_wikipedia-search-input']").send_keys('appium',Keys.ENTER)

window1st = driver.current_window_handle

assert len(driver.window_handles) == 1

driver.find_element(By.XPATH,"//a[text()='Appium']").click()
driver.find_element(By.XPATH,"//a[text()='Appius Claudius Caecus']").click()
driver.find_element(By.XPATH,"//a[text()='AppImage']").click()
driver.find_element(By.XPATH,"//a[text()='Appius Claudius Crassus Inregillensis Sabinus']").click()

wait.until(EC.number_of_windows_to_be(6))

windowIds = driver.window_handles

for winId in windowIds:
    driver.switch_to.window(winId)
    print(driver.title)

time.sleep(5)
driver.quit()