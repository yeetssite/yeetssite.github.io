#!/data/data/com.termux/files/usr/bin/python3.12

import requests
from bs4 import BeautifulSoup 
import urllib.request
import sys

# Big importante variables

version = "v1.1-alpha"
versionFloat = 1.1
help = "asciiFarter: help\n" + \
        "    -v, --version:     show version info\n" + \
        "    -u, --update:      check for updates\n" + \
        "    -h, --help:        show this text"

# Get arguments and do stuff with them

args = sys.argv[1:]

if '-v' in args or '--version' in args:

    if str(versionFloat) not in version:
        print("[33mWarning: versionFloat(" + str(versionFloat) + ") is different from version(" + version + ").[0m")
    print("asciiFarter.py " + version)
    print("use -u or --update to check for a newer version")

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
        if str(versionFloat) not in version:
            print("[33mWarning: versionFloat(" + str(versionFloat) + ") is different from version(" + version + ").[0m")
    elif fartVerFloat == versionFloat:
        print("Up to date. (" + fartVer + " same as " + version + ")")
        if str(versionFloat) not in version:
            print("[33mWarning: versionFloat(" + str(versionFloat) + ") is different from version(" + version + ").[0m")
    elif fartVerFloat < versionFloat:
        print("Developing, are we? (" + fartVer + " under " + version + ")")

elif '-h' in args or '--help' in args:

    print(help)


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
else:
    print("[31masciiFarter.py: \"" + args[0] + "\" is not a valid argument.\n")
    exit(1)



