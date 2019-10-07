from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl

book = openpyxl.load_workbook('challenge.xlsx')
sheet = book.active

# create a new Firefox session
driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://rpachallenge.com/")

javascript_exec = "function getElementsByText(str, tag = 'a') {  return Array.prototype.slice.call(document.getElementsByTagName(tag)).filter(el => el.textContent.trim() === str.trim());}getElementsByText('Start', 'button')[0].click();"

for i in range(1,11):
	for col in sheet.iter_cols(max_col=7, max_row=11, values_only=True):
		javascript_exec += "$(\"label:contains(\\\"" + str(col[0]).strip() + "\\\")\")[0].parentElement.lastElementChild.value=\"" + str(col[i]).strip() + "\";"		

	javascript_exec += "$('input.btn').click();"

driver.execute_script(javascript_exec)