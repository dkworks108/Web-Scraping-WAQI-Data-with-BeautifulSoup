import pandas as pd
from bs4 import BeautifulSoup
import requests

response = requests.get("https://waqi.info/")
soup = BeautifulSoup(response.text, "lxml")

# Step 1: collect data in list
locations = []

for div in soup.find_all("div", class_="local"):
    locations.append(div.get_text(strip=True))

# Step 2: convert list to DataFrame
df = pd.DataFrame(locations, columns=["Location"])

print(df.head())
print("success")
