from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

service_obj = Service("C:/Users/befor/New folder/msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
space = driver.find_element(By.ID,'autocomplete')
space.clear()
space.send_keys("Cuba")
space.send_keys(Keys.DOWN)
space.send_keys(Keys.ENTER)
allButton = driver.find_elements(By.CSS_SELECTOR,".radioButton")
for button in allButton:
    if(button.get_attribute('value')=='radio1'):
        button.click()
        break
assert allButton[0].is_selected()

# checkboxes

checkboxes = driver.find_elements(By.CSS_SELECTOR,'input[type=checkbox]')
for checkbox in checkboxes:
    if(checkbox.get_attribute('value')=='option2'):
        checkbox.click()
        assert checkbox.is_selected()

# if selected

show = driver.find_element(By.ID,'show-textbox')
hide = driver.find_element(By.ID,'hide-textbox')
show.click()
assert driver.find_element(By.ID,'displayed-text').is_displayed()
hide.click()
assert not driver.find_element(By.ID,'displayed-text').is_displayed()

# alerts

word = 'Som'
nameSpace = driver.find_element(By.CSS_SELECTOR,'#name')
nameSpace.send_keys(word)
driver.find_element(By.CSS_SELECTOR,'#alertbtn').click()
alert = driver.switch_to.alert
actual = alert.text
print(actual)
assert word in actual
alert.accept()


driver.close()

