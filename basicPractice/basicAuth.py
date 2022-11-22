





from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')# to pass the username and password inside the url