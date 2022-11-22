from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Edge(executable_path=r"C:\Users\befor\New folder\msedgedriver.exe")

driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://the-internet.herokuapp.com/challenging_dom')



col = driver.find_elements(By.XPATH,'//*[@id="content"]/div/div/div/div[2]/table/thead/tr/th')
row = driver.find_elements(By.XPATH,'//*[@id="content"]/div/div/div/div[2]/table/tbody/tr')

cols = len(col)
rows = len(row)

print(cols,rows)

for r in range (2, rows+1):
    for c in range(1, cols+1):
        value = driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div/div[2]/table/tbody/tr["+str(c)+"]/td["+str(r)+"]').text
        print(value,end=' ')
    print()