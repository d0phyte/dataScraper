#launch vscode from anaconda to have access to the libraries

from bs4 import BeautifulSoup #import beautifulsoup for web scraping
import requests #send http requests
import time 
import datetime 
import smtplib #send emails

# Website connection

URL = 'https://www.amazon.es/-/pt/dp/B00W50HYXO/ref=sr_1_5?crid=ML8GTTYU9SL9&keywords=british+tea+box&qid=1704472543&sprefix=british+tea+box%2Caps%2C88&sr=8-5'



headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productTitle').get_text()

price = soup2.find(id='corePrice_feature_div').get_text()


print(title)
print(price)


