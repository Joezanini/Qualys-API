#an example of Session Based Authentication 

# Load the packages
import requests
from bs4 import BeautifulSoup
import re
import os

#function for testing output
def soupmaker(r) :
	# get the HTML content from the webpage
	html = r.content

	# Create the soup
	soup = BeautifulSoup(html, 'xml')

	# Create the soup
	soup = BeautifulSoup(html, 'xml')

	print(soup.prettify())
	return


# Defining the url of the site
base_site = "https://qualysapi.qg3.apps.qualys.com:443"

# Using Session Based Authentication

headers = {
    'X-Requested-With': 'Python Sample',
}

data = {
  'action': 'login',
  'username': 'quays3te86',
  'password': 'B0j@ckson'
}

s = requests.Session()
response = s.post(base_site + '/api/2.0/fo/session/', headers=headers, data=data)

#print(response.cookies['QualysSession'])

c = response.cookies['QualysSession']

soupmaker(response)

# Make resource requests

cookies = {
    'QualysSession': c,
    'path': '/api',
}

headers = {
    'X-Requested-With': 'Python Sample',
}

data = {
  'action': 'list'
}

response = requests.post(base_site + '/api/2.0/fo/report/', headers=headers, cookies=cookies, data=data)

# get the HTML content from the webpage
html = response.content
# Create the soup
soup = BeautifulSoup(html, 'xml')
# Create the soup
soup = BeautifulSoup(html, 'xml')
# get all report IDs
ids = [row.contents[0] for row in soup.find_all("ID")]

#loop through IDs and download report
for i in ids :
    response = requests.post(base_site + '/api/2.0/fo/report/?action=fetch&id=' + i, headers=headers, cookies=cookies)
    d = response.headers['content-disposition']
    fname = re.findall("filename=(.+)", d)[0]
    #print(fname)
    f = open(fname, 'wb')
    f.write(response.content)

# Make session logout request
data = {
  'action': 'logout'
}

response = requests.post(base_site + '/api/2.0/fo/session/', headers=headers, cookies=cookies, data=data)
soupmaker(response)

