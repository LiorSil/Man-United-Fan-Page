#!/usr/bin/env python
# coding: utf-8

# In[214]:


import bs4
from bs4 import BeautifulSoup  
import pandas as pd
import scipy as sc
import numpy as np
import requests
import numpy as np
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
r = requests.get("https://www.premierleague.com/tables", headers=headers)
data = r.text
preimer_league_soup = BeautifulSoup(data)
#Prepare empty lists
clubs_long=[]
clubs_short=[]
pl=[]
wins=[]
draws=[]
loses=[]
gd=[]
points=[]
table = preimer_league_soup.find("table")

#create fullname list orderd by pos
long_table =  table.find_all('span',attrs = {"class":"long"})
for row in long_table:
    clubs_long.append(row.get_text())

#create short name list orderd by pos
short_table =  table.find_all('span',attrs = {"class":"short"})
for row_s in short_table:
    clubs_short.append(row_s.get_text())
    

temp_table = table.find("tbody")
#pl = played games => create pl list

index = 3
pl.append(temp_table.find_all('td')[index].get_text())
while (index+14 < 280):
    t=temp_table.find_all('td')[index+14].get_text()
    pl.append(t)
    index += 14
    
#wins list    
index =4
wins.append(temp_table.find_all('td')[index].get_text())
while (index+14 < 280):
    t=temp_table.find_all('td')[index+14].get_text()
    wins.append(t)
    index += 14
    
#draws list    
index = 5
draws.append(temp_table.find_all('td')[index].get_text())
while (index+14 < 280):
    t=temp_table.find_all('td')[index+14].get_text()
    draws.append(t)
    index += 14

#loses list    
index =6
loses.append(temp_table.find_all('td')[index].get_text())
while (index+14 < 280):
    t=temp_table.find_all('td')[index+14].get_text()
    loses.append(t)
    index += 14
    
#gd = goals differs list    
index =7
gd.append(temp_table.find_all('td')[index].get_text())
while (index+14 < 280):
    t=temp_table.find_all('td')[index+14].get_text()
    gd.append(t)
    index += 14
    
#points list
#points.append(temp_table.find_all('td')[index].get_text())
for row in temp_table.find_all('td',attrs ={'class':'points'}):
    points.append(row.get_text())

# print("full =" +str(len(clubs_long)))
# print("sh= "+str(len(clubs_short)))
# print("pl= " +str(len(pl)))
# print("wins= " +str(len(wins)))
# print("D= " +str(len(draws)))
# print("L= " +str(len(loses)))
# print("gd= " +str(len(gd)))
# print("points= " +str(len(points)))


df = pd.DataFrame({'Fullname':clubs_long,"club":clubs_short, "played":pl,"wins":wins,"draws":draws,"loses":loses,"gd":gd, "points":points})

html = df.to_html()

# write html to file
text_file = open("index.html", "w")
text_file.write(html)
text_file.close()