from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path="C:\\Users\\befor\\New folder\\chromedriver.exe")

driver = webdriver.Edge(executable_path=r"C:\Users\befor\New folder\msedgedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

x = driver.title

print('{} {} {}'.format("The title of the page is ",x,"and it is matching"))

#print(driver.page_source)

driver.close()
