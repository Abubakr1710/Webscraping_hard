import imp
from lib2to3.pgen2 import driver
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

url = "https://weather.com/weather/tenday/l/San+Francisco+CA?canonicalCityId=dfdaba8cbe3a4d12a8796e1f7b1ccc7174b4b0a2d5ddb1c8566ae9f154fa638c"
pth = "chromedriver.exe"

driver = webdriver.Chrome("C:/Users/Abu/Downloads/chromedriver_win32/chromedriver.exe")

driver.get(url)
