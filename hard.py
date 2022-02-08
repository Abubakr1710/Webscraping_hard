import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://weather.com/weather/tenday/l/San+Francisco+CA?canonicalCityId=dfdaba8cbe3a4d12a8796e1f7b1ccc7174b4b0a2d5ddb1c8566ae9f154fa638c")
soup =BeautifulSoup(page.content, 'html.parser')

list_day = []
list_desc = []
list_min_temp = []
list_max_temp = []

#Getting Days
#--------------------------------------------------------

days = soup.find_all('h2', class_ = "DetailsSummary--daypartName--2FBp2")[1:11:1]
for d in days:
    day_get = d.text
    list_day.append(day_get)

print(list_day)
