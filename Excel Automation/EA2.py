import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from win32com.client import Dispatch
import os

data = {"Asset Name": ["Asset 1", "Asset 2"], "Month 1": [15, 30], "Month 2": [5, 35]}

df = pd.DataFrame(data)

workbook = Workbook()
sheet = workbook.active

for row in dataframe_to_rows(df, index=False, header=True):
    sheet.append(row)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "EA2.xlsx")

workbook.save(filename=file_path)

xl = Dispatch("Excel.Application")
xl.Visible = True
xl.WorkBooks.Open(file_path)
