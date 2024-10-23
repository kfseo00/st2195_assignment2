import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Comma-separated_values"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table', class_='wikitable')

if tables:
    df = pd.read_html(str(tables[0]))[0]
    print(df)
else:
    print("not found")
    
df.to_csv(r'C:/7 programming/csv_table.csv',index=False)

print("table saved to csv_table.csv")
