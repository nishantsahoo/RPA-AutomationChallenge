from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl

book = openpyxl.load_workbook('challenge.xlsx')
sheet = book.active

# create a new Firefox session
# driver = webdriver.Firefox()
# driver.implicitly_wait(30)
# driver.maximize_window()

# # Navigate to the application home page
# driver.get("http://rpachallenge.com/")

for row in sheet.iter_rows(max_col=7, max_row=11, values_only=True):
	print(row)

# javaScript = "console.log(789);"
# driver.execute_script(javaScript)