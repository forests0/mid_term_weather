import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

url = 'https://www.weather.go.kr/w/weather/forecast/mid-term.do'
response = requests.get(url)
region = []
weathers = []

if response.status_code == 200:
  html = response.text
else:
  print('Failed to retrieve the web page')

soup = BeautifulSoup(html, 'html.parser')
title = soup.title.text

elements = soup.select('table > tbody > tr > td')

for index, element in enumerate(elements, 1) :
  weathers.append(element.text)
  #print("{} 지역 날씨: {}".format(index, element.text))

tmin = []
el = soup.select('table > tbody > tr > td > span.tmn')
for index, element in enumerate(el, 1) :
  tmin.append(element.text)
  #print('{} : {}'.format(index, element.text))

elr = soup.select('table > tbody > tr > td.midterm-city > span.sticky')
for index, element in enumerate(elr, 1) :
  region.append(element.text)

tmax = []
els = soup.select('table > tbody > tr > td > span.tmx')
for index, element in enumerate(els, 1) :
  tmin.append(element.text)
  #print('{} : {}'.format(index, element.text))

tmin = np.reshape(tmin, (-1,8))
tmax = np.reshape(tmax, (-1,8))

row = ['Fri','Sat','Sun','Mon','Tue','Wed','Thu','Fri'] # 04.25 기준
col = region
tmin_df = pd.DataFrame(tmin, index = col, columns = row)
tmax_df = pd.DataFrame(tmax, index = col, columns = row)
tmin_df = tmin_df.transpose()
tmax_df = tmax_df.transpose()

tmin_df = tmin_df.astype({'Fri':'int', 'Sat':'int', 'Sun':'int', 'Mon':'int', 'Tue':'int', 'Wed':'int', 'Thu':'int', 'sFri' : 'int' })
tmax_df = tmax_df.astype({'Fri':'int', 'Sat':'int', 'Sun':'int', 'Mon':'int', 'Tue':'int', 'Wed':'int', 'Thu':'int', 'sFri' : 'int' })

temp_all = []
temp_all = pd.concat([tmin_df, tmax_df], ignore_index = True, axis = 1)

fig = plt.figure()
fig.set_facecolor('white')
for _, label in enumerate(region):
    x = range(10)
    y = [random.randint(1,10) for _ in range(10)]
    sns.lineplot(x=x, y=y, label=label) # label 범례 라벨
    plt.legend()