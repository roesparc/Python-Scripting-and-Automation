import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from win32com.client import Dispatch

data = {"Asset Name": ["Asset 1", "Asset 2"], "Month 1": [15, 30], "Month 2": [5, 35]}

df = pd.DataFrame(data)
