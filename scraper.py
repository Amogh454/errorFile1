from typing import List
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import csv
import requests
import pandas as pd

regurl = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
page = requests.get(regurl)

Name=[]
LightYearsFromEarth=[]
PlanetMass=[]
StellarMagnitude=[]

print(page)

soup = bs(page.text,'html.parser')

star_table = soup.find('table')


temp_list= []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

for i in range(1,len(temp_list)):
    Name.append(temp_list[i][1]) 
    LightYearsFromEarth.append(temp_list[i][3])
    PlanetMass.append(temp_list[i][5])
    StellarMagnitude.append(temp_list[i][6])

headers=['NAME','LIGHT-YEARS FROM EARTH','PLANET MASS','STELLAR MAGNITUDE']
planetdata=pd.DataFrame(list(zip(Name,LightYearsFromEarth,PlanetMass,StellarMagnitude)),columns=["NAME','LIGHT-YEARS FROM EARTH','PLANET MASS','STELLAR MAGNITUDE"])
planetdata.to_csv("planetdata.csv")

