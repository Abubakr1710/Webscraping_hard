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
#--------------------------------------------------------
#Getting Description
#--------------------------------------------------------
description = soup.find_all('p', class_='DailyContent--narrative--hplRl')[1:11:1]
for desc in description:
    desc_get = desc.text
    list_desc.append(desc_get)
#--------------------------------------------------------

#Getting max Temperature
max_Temperature = soup.find_all('span',class_="DetailsSummary--highTempValue--3Oteu")[1:11:1]
for max_t in max_Temperature:
    tempMax = max_t.text
    list_max_temp.append(tempMax)
#--------------------------------------------------------

#Getting min Temperature
min_Temperature = soup.find_all('span',class_="DetailsSummary--lowTempValue--3H-7I")[1:11:1]
for min_t in min_Temperature:
    tempMin = min_t.text
    list_min_temp.append(tempMin)
#--------------------------------------------------------




#print(list_day)
#print(len(list_day))
#print(list_desc)
#print(len(list_desc))
#print(list_max_temp)
#print(len(list_max_temp))

#print(len(list_min_temp))
#print(list_min_temp)