from urllib import request
import traceback
from sys import argv
from sys import stdout
from sys import exit
version = 1.00
try:
    url=argv[1]
    if url == '--help' or url == '-h':
        print('WEBCAT HELP')
        print('USAGE: webcat [ URL ]')
        print('       webcat --help')
        print('       webcat --version\a')
        print('Webcat is like cat but for files hosted over the internet.')
        print('Webcat doesnt feature all the features that cat does, its')
        print('just a simple tool to get plain text files from a URL and')
        print('print it in your terminal.\n')
        print('webcat is not an actively developed project, use it at your')
        print("own risk. It was developed because I'm sick of Firefox and")
        print("Chrome's tendency to make it really annoying to properly")
        print("view and download plain .TXT files and isn't one of my main")
        print("projects, thus it will only be updated if needed and if I still")
        print("feel like it. ~itsyeetsup(A.K.A. mangolover1899)\n")
        print("Licensed under YSSL-1.0 as a part of my website. see")
        print("< https://yeetssite.github.io/yssl-1.0/ >.")
        exit(0)
    elif url == '--version' or url == '-v':
        print('webcat version '+str(version))
        exit(0)
    elif 'https://' not in url:
        if 'http://' not in url:
            if 'ftp://' not in url:
                url = str('https://'+url)
except IndexError:
    print('[1;37;41mwebcat: No file URL specified[0m')
    exit(1)

DISP_CONT = False

try:
    with request.urlopen(url) as file:
        if file.getcode() == 404:
            print('webcat: "'+url+'": (404) The requested file could not be found.')
            print('[1;30m([37mi[30m): Try checking your spelling. If the error persists, the file may have been moved or deleted.[0m')
            exit(1)
        else:
            file_contents = file.read().decode('UTF-8')
            DISP_CONT = True
except Exception as err:
    print('[1;41;37mAn exception occured while opening the URL:[49;31m\n')
    print(traceback.format_exc())
    if "unknown url type" in str(err):
        print('[41;37mwebcat: "'+url+'": Not a valid URL.[0m')
    elif "404: Not Found" in str(err):
        print('[41;37mwebcat: "'+url+'": (404) The requested file could not be found.[0m')
    else:
        stdout.write('\r\n[41;37mwebcat: "'+url+'": There was an unknown issue opening this URL.\r\nwebcat: Please check your internet connection and try again,[49;0m\r[49m\n')
    exit(2)

if DISP_CONT:
    for line in file_contents:
        stdout.write(line)
        stdout.flush()
else:
    exit(0)
