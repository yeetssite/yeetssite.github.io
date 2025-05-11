#!/data/data/com.termux/files/usr/bin/python3.12

import requests
from bs4 import BeautifulSoup 
import urllib.request
import sys
import time
import random
import warnings

# check le interndet connection

timeout = 1 
try: 
    requests.head("https://yeetssite.github.io", timeout=timeout)
except requests.ConnectionError:
    sys.stdout.write("[31m")
    raise ConnectionError("Cannot verify connection to yeetssite(https://yeetssite.github.io)\nCheck your internet connection, dipshit.")
    sys.stdout.write("[0m")
    sys.stdout.flush()

# Big importante variables

version = "v1.2-alpha"
versionFloat = 1.2
help = "asciiFarter: help\n\n" + \
        "Usage: asciiFarter.py [ OPTIONS ]\n" + \
        "Running without options shows the latest Ascii Art\n\n" + \
        "    -v, --version:     show version info\n" + \
        "    -u, --update:      check for updates\n" + \
        "    -h, --help:        show this text\n" + \
        "    -r, --random:      show a random Ascii Art."

# Get arguments and do stuff with them

def verWarning():
    if str(versionFloat) not in version:
        print("[33mWarning: Version float(" + str(versionFloat) + ") differs from version(" + version + ").[0m")

args = sys.argv[1:]

if '-v' in args or '--version' in args:    
    print("asciiFarter.py " + version)
    print("use -u or --update to check for a newer version")
    verWarning() 
elif '-u' in args or '--update' in args:

    print("Checking https://yeetssite.github.io for a new version...")
    r = requests.get('https://yeetssite.github.io/Python/status.html')
    site = BeautifulSoup(r.content, 'html.parser')
    fartVerFloat = site.find('p', id='fartVerFloat')
    fartVer = site.find('p', id='fartVer')
    fartVerFloat = float(fartVerFloat.get_text())
    fartVer = fartVer.get_text()
    if fartVerFloat > versionFloat:
        print("There is a new update available: " + fartVer + " over " + version)
        verWarning()
    elif fartVerFloat == versionFloat:
        print("Up to date. (" + fartVer + " same as " + version + ")")
        verWarning()
    elif fartVerFloat < versionFloat:
        print("Developing, are we? (" + fartVer + " under " + version + ")")
        verWarning

elif '-h' in args or '--help' in args:

    print(help)

elif '-r' in args or '--random' in args:

    r = requests.get('https://yeetssite.github.io/Python/status.html')

    soup = BeautifulSoup(r.content, 'html.parser')

    asciiFartsNames = soup.find('p', id='asciiArtsNames')

    print("Random ascii art:")
    liss = " ".join(line.strip() for line in str(asciiFartsNames).splitlines())
    liss = liss.split()
    liss.remove("<p")                      
    liss = [word.replace('id="asciiArtsNames">','') for word in liss]                 
    liss = [word.replace('</p>','') for word in liss]
    
    randomUrl = "https://yeetssite.github.io/" + random.choice(liss)

    for line in urllib.request.urlopen(randomUrl):
        sys.stdout.write(line.decode('utf-8'))
        sys.stdout.flush()
        time.sleep(0.005)

elif not args:
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
    print("Newest ASCII art:")

    for line in newestAscii:
        newestArtUrl = "https://yeetssite.github.io/" + line # add the filename to the end of the url to make a new url
        for line in openUrl(newestArtUrl):                   # open the file located at the new url
            stdoutW(line.decode('utf-8'))                    # use stdoutW instead of print because print adds extra lines which
                                                             # mess up the art.
            stdoutF()                                        # Flush stdout
            time.sleep(0.005)
else:
    class ArgError(ValueError):
        pass
    raise ArgError("[31m\"" + args[0] + "\" is not a valid argument.")
    exit(1)



