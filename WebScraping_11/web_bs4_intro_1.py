# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 11:43:02 2022

@author: paskorn.c
"""
import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())
#print( list(soup.children))
#print([type(item) for item in list(soup.children)])
html = list(soup.children)[2]
#print(list(html.children))

body = list(html.children)[3]
#print(list(body.children))

p = list(body.children)[1]
#print(p.get_text())