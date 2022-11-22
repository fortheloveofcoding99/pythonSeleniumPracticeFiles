from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import xlrd

workbook = xlrd.open_workbook_xls('Book1.xls')
sheet = workbook.sheet_by_name('Sheet1')


rowCt = sheet.nrows
print('No of rows:',rowCt)