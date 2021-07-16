#an example of Session Based Authentication 

# Load the packages
import requests
from bs4 import BeautifulSoup

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
  'username': 'username',
  'password': 'password '
}

s = requests.Session()
response = s.post(base_site + '/api/2.0/fo/session/', headers=headers, data=data)

#print(response.cookies['QualysSession'])

c = response.cookies['QualysSession']

print(c)

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

soupmaker(response)

# Make session logout request
data = {
  'action': 'logout'
}

response = requests.post(base_site + '/api/2.0/fo/session/', headers=headers, cookies=cookies, data=data)
soupmaker(response)

