#KeyNotes

#DOM is Document Object Model
#When the webpage is loaded browser creates a DOM of the page and Xpath works on the DOM
#Xpath is an address of the element
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.implicitly_wait(5)
print(driver.title)
print(driver.current_url)
#print(driver.page_source)
weblinks = driver.find_elements(By.CLASS_NAME,'orangehrm-login-container')
print(len(weblinks))
driver.find_element(By.XPATH,"//input[contains(@name,'user')]").send_keys("Admin")
driver.find_element(By.XPATH,"//input[starts-with(@name,'pass')]").send_keys("admin123")
driver.find_element(By.XPATH,"//button[contains(@type,'submit')]").click()
driver.find_element(By.XPATH,"//p[text()='(1) Pending Self Review']").click()
driver.find_element(By.XPATH,"//button[contains(@title,'Evaluate')]").click()
rev_stat=driver.find_element(By.XPATH,"//p[text()='Review Status']")
rev_stat.get_attribute()
time.sleep(5)