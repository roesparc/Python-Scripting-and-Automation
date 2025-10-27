import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/Premier_League"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
scraper = pd.read_html(response.text)

print(scraper)
