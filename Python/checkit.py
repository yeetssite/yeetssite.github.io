import requests
from bs4 import BeautifulSoup 


# Making a GET request
r = requests.get('https://yeetssite.github.io/')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# finding element by class
s = soup.find('p', class_= 'rdrTextNormal')

for line in s:
    print(line)
