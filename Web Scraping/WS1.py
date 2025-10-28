import requests
import pandas as pd
from io import StringIO
import os

url = "https://en.wikipedia.org/wiki/Premier_League"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
scraper = pd.read_html(StringIO(response.text))

# for i, table in enumerate(scraper):
#     print("---")
#     print(i)
#     print(table)

df = scraper[1]

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "WS1.csv")

df.to_csv(file_path, index=False)
