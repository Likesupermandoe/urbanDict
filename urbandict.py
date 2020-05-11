#!/usr/bin/env python3
import sys
import requests
from bs4 import BeautifulSoup

url = "http://urbandictionary.com"
word = sys.argv[1]
#TODO
#only taking 1 word searches right now
searchurl = url + "/define.php?term=" + word
response = requests.get(searchurl)
data = response.text

soup = BeautifulSoup(response.text, 'html.parser')
meaning = soup.find('div', {'class' :'meaning'}).text

print(meaning)

#TODO
#print examples
#print multiple definitions
