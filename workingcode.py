import requests 
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

#url = StringIO("https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table")
url = "https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
tables = soup.find_all("table")
i=0

df = pd.read_html(StringIO(str(tables[1])))
print(df)
#print(type(df))
#print(len(df))
#print(type(df[0]))
#df1 = df[0]
#print(type(df1))
