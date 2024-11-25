import requests
from bs4 import BeautifulSoup 
import urllib.request
import sys

# Simplify some function names
stdoutW = sys.stdout.write
stdoutF = sys.stdout.flush
openUrl = urllib.request.urlopen

# Make a GET request and store it to "r"
r = requests.get('https://yeetssite.github.io/Python/status.html')

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')

# Get the newest ascii filename <from https://yeetssite.github.io/Python/status.html>
newestAscii = soup.find('p', id= 'newestAscii')
print("\nNewest ASCII art:")

for line in newestAscii:
    newestArtUrl = "https://yeetssite.github.io/" + line # add the filename to the end of the url to make a new url
    for line in openUrl(newestArtUrl):                   # open the file located at the new url
        stdoutW(line.decode('utf-8'))                    # use stdoutW instead of print because print adds extra lines which
                                                         # mess up the art.

