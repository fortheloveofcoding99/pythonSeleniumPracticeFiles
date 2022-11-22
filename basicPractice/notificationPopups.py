from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ops = webdriver.ChromeOptions()
ops.add_argument('--disable-notifications')
#ops.headless
driver = webdriver.Chrome(options=ops)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://whatmylocation.com/')