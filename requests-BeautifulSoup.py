# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 20:18:33 2021

@author: harishs
"""

import requests
import bs4


res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')

print(type(res))

soup = bs4.BeautifulSoup(res.text,'lxml')
#print(type(soup))

#print((res.text))

#print('Title of the Page  -->' + soup.title.text)

for article in soup.find_all('script', type='application/ld+json'):
    print(article)

