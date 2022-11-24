import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities import XlUtils

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://cleartax.in/s/simple-compound-interest-calculator')

file = 'C:/Users/befor/PycharmProjects/seleniumWithPython/basicPractice/testWriteData.xlsx'

rows = XlUtils.getRowCount(file, 'SiPage')

for r in range(2,rows+1):
    IntType=XlUtils.readData(file,'SiPage',r,1)
    prin=XlUtils.readData(file,'SiPage',r,2)
    rate=XlUtils.readData(file,'SiPage',r,3)
    periodUni=XlUtils.readData(file,'SiPage',r,4)
    period=XlUtils.readData(file,'SiPage',r,5)
    TotValue=XlUtils.readData(file,'SiPage',r,6)
    expect=XlUtils.readData(file,'SiPage',r,7)

    #passing the values to application
    interestType = Select(driver.find_element(By.ID, 'a'))
    interestType.select_by_visible_text(IntType)
    driver.find_element(By.ID, 'c').clear()
    driver.find_element(By.ID, 'c').send_keys(prin)
    driver.find_element(By.ID, 'd').clear()
    driver.find_element(By.ID, 'd').send_keys(rate)
    periodUnit = Select(driver.find_element(By.ID, 'f'))
    periodUnit.select_by_visible_text(periodUni)
    driver.find_element(By.ID, 'e').clear()
    driver.find_element(By.ID, 'e').send_keys(period)
    #(// div[@class ='output'])[3]
    amnt=driver.find_element(By.XPATH,"//*[@id='calc']/div/div[8]/div/span").text.split()
    print(amnt[1])

    #validation
    if TotValue == amnt[1]:
        XlUtils.writeData(file,'SiPage',r,8,'Passed')
        XlUtils.fillGreenColor(file,'SiPage',r,8)
    else:
        XlUtils.writeData(file,'SiPage', r, 8, 'Failed')
        XlUtils.fillRedColor(file,'SiPage',r,8)
    time.sleep(1)
driver.close()







