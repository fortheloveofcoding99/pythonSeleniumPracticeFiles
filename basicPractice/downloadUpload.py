from selenium import webdriver
from selenium.webdriver.common.by import By
import os
##doc file download
# location = os.getcwd()
# preferences = {"download.default_directory":location,"plugins.always_open_pdf_externally":True}
# ops = webdriver.ChromeOptions()
# ops.add_experimental_option('prefs',preferences)
# driver = webdriver.Chrome(options=ops)
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get('https://file-examples.com/index.php/sample-documents-download/sample-doc-download/')
# driver.find_element(By.XPATH,"(//a[text()='Download sample DOC file'])[1]").click()

# pdf file download
location = os.getcwd()
preferences = {"download.default_directory":location,"plugins.always_open_pdf_externally":True}
ops = webdriver.ChromeOptions()
ops.add_experimental_option('prefs',preferences)
driver = webdriver.Chrome(options=ops)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/')
#driver.find_element(By.XPATH,"(//a[text()='Download sample pdf file'])[1]").click()
#driver.save_screenshot(os.getcwd()+'//screenshot.png')
#driver.get_screenshot_as_file('screenshot.png')
driver.switch_to.new_window('tab')
driver.get('https://www.orangehrm.com/')