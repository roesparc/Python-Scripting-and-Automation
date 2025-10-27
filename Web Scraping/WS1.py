import requests
import pandas as pd
from io import StringIO

url = "https://en.wikipedia.org/wiki/Premier_League"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
scraper = pd.read_html(StringIO(response.text))

for i, table in enumerate(scraper):
    print("---")
    print(i)
    print(table)
