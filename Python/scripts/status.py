import requests
from bs4 import BeautifulSoup 
import random


# Make a GET request and store it ti the variable "r"
r = requests.get('https://yeetssite.github.io/Python/status.html')

# Parse some HTML with souo
soup = BeautifulSoup(r.content, 'html.parser')

# Find paragraphs("p") using their IDs
asciiFarts = soup.find('p', id= 'asciiArts')

asciiFartsNames = soup.find('p', id='asciiArtsNames')

crawlIDs = soup.find('p', id= 'crawlIDs')

textPastas = soup.find('p', id= 'textPastas')

newestAscii = soup.find('p', id= 'newestAscii')

fartVer = soup.find('p', id= 'fartVer')

fartVerFloat = soup.find('p', id= 'fartVerFloat')

# Print the IDs value
print("Total Ascii arts:")
for line in asciiFarts:
    print(line)
    global pp
    pp = list(line)
    pp = pp.append(line)
print("\nAll Ascii Art Filenames:")
for line in asciiFartsNames:
    print(line)
liss = " ".join(line.strip() for line in str(asciiFartsNames).splitlines())
liss = liss.split()
liss.remove("<p")
liss = [word.replace('id="asciiArtsNames">','') for word in liss]
liss = [word.replace('</p>','') for word in liss]
print("random pick: " + random.choice(liss))


print("\nCrawl IDs:")
for line in crawlIDs:
    print(line)
print("\nTotal Text Copypastas:")
for line in textPastas:
    print(line)

print("\nNewest ASCII art:")
for line in newestAscii: 
    print("https://yeetssite.github.io/" + line) # This IDs value is always a filename of a file in the root of the site.
                                                 # This can be used to generate a url. This is used in asciiFarter. 

print("\nLatest asciiFarter version:")
for line in fartVer:
    print(line)
for line in fartVerFloat:
    print("Reported version float: " + line)
