---
permalink: /about-scripts/
title: scripts
layout: default
---
# scripts  
My bash and other assorted scripts

# use  
This repo is actually a github pages site at https://yeetssite.github.io/scripts/, but it has no content as it's specifically made to host files only.

It's meant to be used with bash, but can contain other script types, too.

### These are the current bash scripts availible:  

`yeetsmemes v1.4-alpha`   
`qls v1.2-alpha`  
`yeetsinstaller v1.3-alpha`  

# Installing

### You can install my scripts using these methods:

#### The installer (The recommended way)

The installer is the recommended way to get my scripts because you don't have to specify the path to scripts you want to run if you use this method.  
To use the installer, enter or copypasta these commands: 

    $ curl -O https://yeetssite.github.io/scripts/yeetsinstaller
    $ chmod u+r+x ./yeetsinstaller 
    $ # ^^^Downloads the installer and marks it executable
    $ ./yeetsinstaller 
    $ # ^^^runs the installer
    

The installer will download scripts to your `BIN/` directory so they can be executed as normal commands.

You can also use `wget` to download the installer:

    $ wget https://yeetssite.github.io/scripts/yeetsinstaller && chmod u+r+x ./yeetsinstaller
    $ ./yeetsinstaller

#### Clone Via Git:

    $ git clone https://github.com/yeetssite/scripts

But using this method to install will require you to specify the path to your scripts every time you want to run them, e.g.:

    someone@localhost: ~ $ ./scripts/yeetsmemes

Using the installer will download scripts to your BIN and mark them executable, letting them be run like this:

    $ yeetsmemes


