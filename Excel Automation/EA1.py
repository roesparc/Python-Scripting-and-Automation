from openpyxl import Workbook
from win32com.client import Dispatch
import os

# Create a new Excel workbook using openpyxl

workbook = Workbook()
sheet = workbook.active


# Add some initial data

sheet["A1"] = "Testing"
sheet["B1"] = "Automation"


# Build the path to save the file in the same folder as this script

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "EA1.xlsx")


# Save the workbook

workbook.save(filename=file_path)


# Open the saved workbook in Excel using pywin32

xl = Dispatch("Excel.Application")  # Start Excel application
xl.Visible = True  # Make Excel window visible

wb = xl.WorkBooks.Open(file_path)


# Update a specific cell in Excel

sheet1 = wb.Sheets(1)
a1_cell = sheet1.Cells(1, 1)
a1_cell.Value = "Update"


# Save changes and close Excel
wb.Save()
wb.Close()
xl.Quit()
