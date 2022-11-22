from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


driver = webdriver.Edge(executable_path=r"C:\Users\befor\New folder\msedgedriver.exe")

driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://demoqa.com/automation-practice-form')

driver.find_element(By.ID,'firstName').send_keys('Joe')
driver.find_element(By.ID,'lastName').send_keys('Biden')
driver.find_element(By.ID,'userEmail').send_keys('joeBiden@att.net')
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
butn = driver.find_element(By.XPATH,"//*[@id='gender-radio-1']")
driver.execute_script("arguments[0].click();", butn)
# actions = ActionChains(driver) // actions class to click element
# actions.move_to_element(butn).perform()
driver.find_element(By.ID,'userNumber').send_keys('9090909090')
driver.find_element(By.XPATH,'//*[@id="hobbiesWrapper"]/div[2]/div[1]/label').click()
driver.find_element(By.ID,'currentAddress').send_keys('A313 bangalore')
# dd = driver.find_element(By.ID,'state').click()
# dd.send_keys(Keys.ARROW_DOWN)
# dd.send_keys(Keys.RETURN)
# #
# dd_select = Select(dd)
#
# dd_select.select_by_visible_text('NCR')

subt = driver.find_element(By.ID,'submit')

driver.execute_script('arguments[0].click();',subt)

