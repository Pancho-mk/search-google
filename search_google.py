#! python3
'''Extracting links from google, searching with requests and Beautiful Soup'''

import requests, sys, webbrowser
from bs4 import BeautifulSoup
from collections import OrderedDict

print('Googling...') # display text while downloading the Google page

term = 'tesla'        #term for searhing

headers = {"Accept-Language": "en-US,en;q=0.5", 'Accept-Encoding': 'gzip, deflate'}
r = requests.get('https://www.google.com/search?q=' + term, headers=headers)

# Retrieve top search result links.
soup = BeautifulSoup(r.text, 'lxml')

links = soup.find_all('div', class_='ZINbbc xpd O9g5cc uUPGi')

#clean up the links
links_list = []
for link in links:
	try:
		url_plus = link.a.get('href')
		url_lstrip = url_plus.lstrip('/url?q=')
		url = url_lstrip.split('&')
	except Exception as a:               #some of the divs has other links which are not of interest
		pass

	if url[0]!='search?ie=UTF-8':             #some of the divs has links which needs to be clean up
			links_list.append(url[0])

links_unique_list = list(OrderedDict.fromkeys(links_list))     #removing duplicates from the list

#some of the links are for google.maps which are not of interest
links_finaly = [element for element in links_unique_list if 'google.com' not in element]
print(links_finaly)





