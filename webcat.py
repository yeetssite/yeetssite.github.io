from urllib import request
import traceback
from sys import argv
from sys import stdout
from sys import exit
try:
    url=argv[1]
except:
    print('webcat: No file URL specified')
    exit(1)

DISP_CONT = False

try:
    with request.urlopen(url) as file:
        if file.getcode() == 404:
            print('webcat: '+url+': (404) The requested file could not be found.')
            print('[1;30m([37mi[30m): Try checking your spelling. If the error persists, the file may have been moved or deleted.[0m')
            exit(1)
        else:
            file_contents = file.read().decode('UTF-8')
            DISP_CONT = True
except Exception as err:
    print('An exception occured while opening the URL:')
    print(traceback.format_exc())
    print('webcat: '+url+': There was an unknown issue opening this URL. Please check your internet connection and try again.')
    exit(2)

if DISP_CONT:
    for line in file_contents:
        stdout.write(line)
        stdout.flush()
else:
    exit(0)
