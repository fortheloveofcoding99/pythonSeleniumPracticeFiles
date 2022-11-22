from selenium import webdriver
from selenium.webdriver.edge.service import Service

service_obj = Service("C:/Users/befor/New folder/msedgedriver.exe")
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.implicitly_wait(3)
driver.get('https://admin-demo.nopcommerce.com/login')
print(driver.title)
url = driver.current_url
assert url == 'https://admin-demo.nopcommerce.com/login'
print(url)
driver.close()

