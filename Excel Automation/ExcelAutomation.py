from openpyxl import Workbook
from win32com.client import Dispatch

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Testing"
sheet["B1"] = "Automation"

workbook.save(filename="testing_automation.xlsx")
