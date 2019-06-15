from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl

book = openpyxl.load_workbook('challenge.xlsx')
sheet = book.active

# create a new Firefox session
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("http://rpachallenge.com/")

javascript_exec = ""

# first click on go button

for i in range(1,11):
	for col in sheet.iter_cols(max_col=7, max_row=11, values_only=True):
		print(col[0], col[i])
		# javascript_exec += "$(\"label:contains(\"" + str(col[0]).strip() + "\")\").parentElement.lastElementChild.value = " + str(col[i]).strip() + ";"
		
		# javascript_exec = "console.log($(\"label:contains(\"First Name\")\"));";

	# print(javascript_exec)
	# driver.execute_script(javascript_exec);	

# javascript_exec = "ele=$(\"label:contains(\\\"First Name\\\")\");console.log(ele);"
# print(javascript_exec)
javascript_exec += "$(\"label:contains(\\\"" + "First Name" + "\\\")\")[0].parentElement.lastElementChild.value = " + "\"John\"" + ";"
print(javascript_exec)
driver.execute_script(javascript_exec)

# javaScript = "console.log(789);"
# driver.execute_script(javaScript)

# Use var element = $("label:contains('SuperSweetCheckbox')"); to find label whose inner HTML value is SuperSweetCheckbox
# $("label:contains('col_val')").parent.children -> input = row['col_val']
