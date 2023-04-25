import requests
import numpy as np
from bs4 import BeautifulSoup

url = 'https://www.weather.go.kr/w/weather/forecast/mid-term.do'
response = requests.get(url)
region = []
weathers = []

if response.status_code == 200:
  html = response.text
  #print(html)
else:
  print('Failed to retrieve the web page')

soup = BeautifulSoup(html, 'html.parser')
title = soup.title.text

elements = soup.select('table > tbody > tr > td')

for index, element in enumerate(elements, 1) :
  weathers.append(element.text)
  print("{} 지역 날씨: {}".format(index, element.text))

tmin = []
el = soup.select('table > tbody > tr > td > span.tmn')
for index, element in enumerate(el, 1) :
  tmin.append(element.text)
  print('{} : {}'.format(index, element.text))

tmax = []
els = soup.select('table > tbody > tr > td > span.tmx')
for index, element in enumerate(els, 1) :
  tmin.append(element.text)
  print('{} : {}'.format(index, element.text))

we = weathers[140 : -1]
we.remove('그래프')

tmin = np.reshape(tmin, (-1,8))
tmax = np.reshape(tmax, (-1,8))