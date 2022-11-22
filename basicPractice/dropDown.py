from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Edge(executable_path=r"C:\Users\befor\New folder\msedgedriver.exe")

driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://the-internet.herokuapp.com/dropdown')

dd  = driver.find_element(By.ID,'dropdown')

dd_select = Select(dd)

dd_select.select_by_index(1)

li1 = len(dd_select.options)

print(li1)

all_options = dd_select.options

for d in all_options:
    print(d.text)

