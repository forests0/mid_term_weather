# !pip install requests
# !pip install bs4
# !pip install requests

import requests
from bs4 import BeautifulSoup

url = 'https://www.weather.go.kr/w/weather/forecast/mid-term.do'
response = requests.get(url)
region = []

if response.status_code == 200:
  html = response.text
  #print(html)
else:
  print('Failed to retrieve the web page')

soup = BeautifulSoup(html, 'html.parser')
title = soup.title.text

elements = soup.select('tbody > tr > td.midterm-city > span.sticky')

for index, element in enumerate(elements, 1) :
  # region.append(element.text)
	print("{} 지역 날씨: {}".format(index, element.text))
