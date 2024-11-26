#!/usr/bin/python3.12

import requests, urllib, os

if 'PREFIX' in os.environ:
    print("Termux detected")
    bin = str(os.environ['PREFIX'] + "/bin/")
    os.chdir(bin)
    pwd = os.getcwd()
    print(pwd)
    if 'WINDIR' not in os.environ:
        print('no bimbos')
    else:
        print("how bimbos??")
else:
    print("This doesnt work")
