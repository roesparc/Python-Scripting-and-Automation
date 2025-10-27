import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from win32com.client import Dispatch
import os
from datetime import datetime
import random

workbook = Workbook()
sheet = workbook.active
sheet.title = "Assets Report"

assets = ["Asset 1", "Asset 2", "Asset 3"]
months = [f"Month {i}" for i in range(1, 7)]  # dynamically generate 6 months

data = {"Asset Name": assets}

for month in months:
    data[month] = [random.randint(0, 50) for _ in assets]

df = pd.DataFrame(data)

# Add a total column
df["Total"] = df[months].sum(axis=1)

# Add an average row
totals = df.select_dtypes(include="number").mean(axis=0)
totals["Asset Name"] = "Average"
df = pd.concat([df, pd.DataFrame([totals])], ignore_index=True)

for row in dataframe_to_rows(df, index=False, header=True):
    sheet.append(row)

script_dir = os.path.dirname(os.path.abspath(__file__))
timestamp = datetime.now().strftime("%Y-%m-%d_timestamp")
file_path = os.path.join(script_dir, f"EA2_{timestamp}.xlsx")

workbook.save(filename=file_path)

xl = Dispatch("Excel.Application")
xl.Visible = True
xl.WorkBooks.Open(file_path)
