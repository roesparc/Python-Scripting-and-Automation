import requests
import pandas as pd
from io import StringIO
import os

# List of URLs to scrape
urls = [
    "https://en.wikipedia.org/wiki/Premier_League",
    "https://en.wikipedia.org/wiki/List_of_Premier_League_seasons",
]

headers = {"User-Agent": "Mozilla/5.0"}
all_data = []

for url in urls:
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to load {url}")
        continue

    # Extract all tables from the page
    tables = pd.read_html(StringIO(response.text))

    # You can pick a specific table by index or filter by columns
    for table in tables:
        # Example: only keep tables with a 'Season' column
        if "Season" in table.columns:
            all_data.append(table)

# Combine all tables into one DataFrame
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
else:
    raise Exception("No suitable tables found.")

# Save combined data
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "WS1.csv")
combined_df.to_csv(file_path, index=False)
