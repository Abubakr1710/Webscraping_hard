from re import X
import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://weather.com/weather/tenday/l/San+Francisco+CA?canonicalCityId=dfdaba8cbe3a4d12a8796e1f7b1ccc7174b4b0a2d5ddb1c8566ae9f154fa638c")
soup =BeautifulSoup(page.content, 'html.parser')

list_day = []
list_desc_d = []
list_desc_n = []
list_min_temp = []
list_max_temp = []
list_c_min = []
list_c_max = []

#Getting Days
#--------------------------------------------------------

days = soup.find_all('h2', class_ = "DetailsSummary--daypartName--2FBp2")[0:10:1]
for d in days:
    day_get = d.text
    list_day.append(day_get)
#--------------------------------------------------------
#Getting Description
#--------------------------------------------------------
description_d = soup.find_all('p', class_='DailyContent--narrative--hplRl')[0:20:2]
for desc in description_d:
    desc_get = desc.text
    #desc_get_d = desc_get_d.split('.')[0]
    list_desc_d.append(desc_get)
#print(len(list_desc_d))
#print(list_desc_d)
#---------------------------------------------------------
description_n = soup.find_all('p', class_='DailyContent--narrative--hplRl')[1:20:2]
for desc_n in description_n:
    desc_get_n = desc_n.text
    #desc_get_n = desc_get_n.split('.')[0]
    list_desc_n.append(desc_get_n)
#print(len(list_desc_n))
#print(list_desc_n)


#--------------------------------------------------------

#Getting max Temperature
max_Temperature = soup.find_all('span',class_="DetailsSummary--highTempValue--3Oteu")[1:11:1]
for max_t in max_Temperature:
    tempMax = max_t.text.split('°')[0]
    tempMax = int(tempMax)
    list_max_temp.append(tempMax)
#--------------------------------------------------------

#Getting min Temperature
min_Temperature = soup.find_all('span',class_="DetailsSummary--lowTempValue--3H-7I")[1:11:1]
for min_t in min_Temperature:
    tempMin = min_t.text.split('°')[0]
    tempMin = int(tempMin)
    list_min_temp.append(tempMin)
#--------------------------------------------------------

#Convert farenheit to Celcius

#Convert min
def Convert_min():
    for i in  list_min_temp:
        new_min_temp = round((i-32)*(5/9))
        list_c_min.append(new_min_temp)


#--------------------------------------------------------

#Convert max
def Convert_max():
    for i in  list_max_temp:
        new_max_temp = round((i-32)*(5/9))
        list_c_max.append(new_max_temp)
Convert_max()
# -----------------------------------------------------
# Create Dates

dates_from_08 = pd.date_range('2022-02-08',periods=10,freq='D')

# -----------------------------------------------------
# CREATING DATAFRAME
#--------------------------------------------------------

data = { 'Days': list_day,'Description for day': list_desc_d, 'Temp (MAX)': list_c_max,'Description for night': list_desc_n ,  'Temp (MIN)': list_c_min }

days = list_day
table = pd.DataFrame(data, index=dates_from_08 )


index = []


print(table)
#print(list_day)
#print(len(list_day))
#print(list_desc)
#print(len(list_desc))
#print(list_max_temp)
#print(len(list_max_temp))
#print(len(list_min_temp))
#print(list_min_temp)
#print(len(list_c_min))
#print(list_c_min)
#print(list_c_max)
#print(len(list_c_max))
