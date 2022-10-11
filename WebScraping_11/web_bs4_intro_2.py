import requests
from bs4 import BeautifulSoup
#import csv

page = requests.get("https://raw.githack.com/paskorn/DS270-Git2022/master/Simple_Head.html")
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.select('p a'))





