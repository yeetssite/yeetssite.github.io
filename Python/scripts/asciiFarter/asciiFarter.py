#!/usr/bin/python3.12

# Copyright(c) 2024 itsyeetsup(aka "mangolover1899"
# Licensed under some shitty software license idk <https://yeetssite.github.io/yssl-1.1>

# I need ALL of these
import requests
from bs4 import BeautifulSoup 
import urllib.request
import sys
import time
import random

# check le interndet connection
timeout = 1 
try: 
    requests.head("https://yeetssite.github.io", timeout=timeout)
    # Connect to https://yeetssite.github.io, do nothing if successful.

except requests.ConnectionError:
    # Throw an error if a connection cannot be made
    sys.stdout.write("[31m")
    raise ConnectionError("Cannot verify connection to yeetssite(https://yeetssite.github.io)\nCheck your internet connection, dipshit.")
    sys.stdout.write("[0m")
    sys.stdout.flush()

# Big importante variables

# The current version with the development stage(e.g. alpha)
# Should generally be named something like "v1.3-alpha".
version = "v1.3-alphadev"

# The current version as a floating point(number only)
versionFloat = 1.3

# Prints when --help or -h option is passed
help = "asciiFarter: help\n\n" + \
        "Usage: asciiFarter.py [ OPTIONS ]\n" + \
        "Running without options shows the latest Ascii Art\n\n" + \
        "    -v, --version:     show version info\n" + \
        "    -u, --update:      check for updates\n" + \
        "    -h, --help:        show this text\n" + \
        "    -r, --random:      show a random Ascii Art."

# Warn if versionFloat variable says a different version than the version variable, because it will lead to
# catastrophic misinformation spreading if I fuck up and release a version with a different version float.
def verWarning():
    if str(versionFloat) not in version:
        print("[33mWarning: Version float(" + str(versionFloat) + ") differs from version(" + version + ").[0m")

# Get arguments
args = sys.argv[1:]

# Do stuff(main code below)
if not args: # Runs when there aren't any arguments
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
        newestArtUrl = "https://yeetssite.github.io/" + line 
        # add the filename to the end of the url to make a new url

        for line in openUrl(newestArtUrl): 
            # open the file located at the new url

            stdoutW(line.decode('utf-8'))                    
            # use stdoutW instead of print because print adds extra lines which mess up the art.
            stdoutF()
            # Flush stdout(so it doesnt got clogged with big taco bell shits)
            time.sleep(0.005)
            # sleep for a teeny tiny bit after every line to look smoother

# Print version

elif '-v' in args or '--version' in args:
    print("asciiFarter.py " + version)
    print("use -u or --update to check for a newer version")
    verWarning()

# Update check

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
        verWarning()

# Help 

elif '-h' in args or '--help' in args:
    print(help)

# Random art 

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

# get newest text pasta

elif "-t" in args or "--textpasta" in args:
    r = requests.get('https://yeetssite.github.io/Python/status.html')
    soup = BeautifulSoup(r.content, 'html.parser')
    textPasta = soup.find('p', id='newestText')

    for line in textPasta:
        pastaUrl = "https://yeetssite.github.io/textPasta/" + line

        for line in urllib.request.urlopen(pastaUrl):
            sys.stdout.write(line.decode('utf-8'))
            sys.stdout.flush()
            time.sleep(0.005)

# Get whatsnew message

elif "-w" in args or "--whatsnew" in args:
    lineCount = 0
    whatsnewMsg = urllib.request.openurl('https://yeetssite.github.io/Python/scripts/asciiFarter/README.txt')
    printWhatsnew = False
    for line in whatsnewMsg:
        line = line.decode('utf-8')
        lineCount += 1
        if "==whatsnew.start==" in line:
            printWhatsnew = True
        elif "==whatsnew.end==" in line:
            printWhatsnew = False
        if printWhatsnew:
            sys.stdout.write(line)
            sys.stdout.flush()
        else:
            pass


# Statistics

elif "-s" in args or "--stats" in args:
    r = requests.get("https://yeetssite.github.io/Python/status.html")
    soup = BeautifulSoup(r.content, 'html.parser')
    asciiArtsCount = soup.find('p', id='asciiArts')
    asciiArtsNames = soup.find( 'p', id='asciiArtsNames')
    newestAscii = soup.find('p', id='newestAscii')
    textPastaCount = soup.find('p', id='textPastas')
    textPastaNames = soup.find('p', id='textPastasNames')
    latestText = soup.find('p', id='latestText')
    latestPubRelease = soup.find('P', id='fartVer')
    pubVerFloat = soup.find('p', id='fartVerFloat')

    print("[1masciiFarter Stats:[0m")
    for line in asciiArtsCount:
        print("\n   [1mAscii art count:[m " + line)
    for line in latestText:
        print("\n   [1mNewest Ascii art:[m " + line)
    print("\n   [1mAll Ascii arts:[0m\n")
    for line in asciiArtsNames:
        print("     " + line)
    for line in textPastaCount:
        print("\nMy brain hurts.")

# Spew out an error when bad argument passed

else:
    class ArgError(ValueError):
        pass
    raise ArgError("^[[31m\"" + args[0] + "\" is not a valid argument.\a")
    exit(1)
