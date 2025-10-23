from openpyxl import Workbook
from win32com.client import Dispatch
import os

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Testing"
sheet["B1"] = "Automation"

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "excel_automation.xlsx")

workbook.save(filename=file_path)

xl = Dispatch("Excel.Application")
xl.Visible = True

wb = xl.WorkBooks.Open(file_path)

sheet1 = wb.Sheets(1)
a1_cell = sheet1.Cells(1, 1)
a1_cell.Value = "Update"

wb.Save()
wb.Close()
xl.Quit()
