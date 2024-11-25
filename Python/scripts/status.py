import requests
from bs4 import BeautifulSoup 


# Make a GET request and store it ti the variable "r"
r = requests.get('https://yeetssite.github.io/Python/status.html')

# Parse some HTML with souo
soup = BeautifulSoup(r.content, 'html.parser')

# Find paragraphs("p") using their IDs
asciiFarts = soup.find('p', id= 'asciiArts')

crawlIDs = soup.find('p', id= 'crawlIDs')

textPastas = soup.find('p', id= 'textPastas')

newestAscii = soup.find('p', id= 'newestAscii')

# Print the IDs value
print("Total Ascii arts:")
for line in asciiFarts:
    print(line)
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

