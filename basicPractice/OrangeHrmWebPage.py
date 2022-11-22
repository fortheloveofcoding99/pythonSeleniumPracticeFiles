import webbrowser

# 3 different ways of invoking the browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


#through driver-manger
# s=Service(ChromeDriverManager().install())
# driver=webdriver.Chrome(service=s)

#through chromeDriver exe saved in project/local
s1=Service('C:/Users/befor/New folder/chromedriver')
driver=webdriver.Chrome(service=s1)

#through chromedriver saved in the scripts folder of the python interpreter SDK
#driver = webdriver.Chrome()

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.implicitly_wait(5)
print(driver.title)
weblinks = driver.find_elements(By.CLASS_NAME,'orangehrm-login-container')
print(len(weblinks))
