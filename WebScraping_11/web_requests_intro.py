# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:43:18 2022

@author: paskorn.c
"""
import requests
page = requests.get("https://raw.githack.com/paskorn/DS270-Git2022/master/simple.html")
print(page)
print(page.content)
