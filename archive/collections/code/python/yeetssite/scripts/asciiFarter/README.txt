** AsciiFarter README v1.0 **

Revision 11.29.2024
Author: itsyeetsup(aka "mangolover1899")
Licensed under YSSL 1.1. See <https://yeetssite.github.io/yssl-1.1> for more info.

AsciiFarter is an internet based application. If it spits out a bunch of random stuff, you're probably not connected 
to the interwebs, especially if that random stuff is red.

————————————————————————————————————————————————————————————————————————————————————————————————

Installation:

You don't necessarily need to install asciiFarter, as it is a python 3.12 script. simply download it, go to whichever
folder you downloaded it in(in this example, we'll pretend it was downloaded to "~/Download/"), and run the following 
command:

(Note: "[bash]:" at the beginning of a line just means that said line is a terminal example. DO NOT INCLUDE "[bash]:",
or anything that comes before the "$", including the "$", because what comes after is the command. If a line doesn't 
have a "$" it is not a command at all.)

[bash]: ~/Download/ $ py asciiLover.py

If you receive the following error(or something like it):

[bash]: bash: command "py" not found

Then try the following:

[bash]: ~/Download/ $ python asciiLover.py

If you still get the same error, you probably don't have python 3 installed.

To install it:

Windows: get it from <https://www.python.org/downloads/windows/> or the Microsoft store.

MacOS: get it from <https://www.python.org/downloads/macos/>

Linux:

   Ubuntu/Debian: 
   [bash]: ~ $ sudo apt install -y python3

   Arch, btw:
   [bash]: ~ $ $ sudo pacman -Sy python3

   Termux:
   [bash]: pkg install python3

   Other(no, I am not listing every possible Linux distro, stfu Fedora/Red hat users):
   Compile the source from <https://www.python.org/downloads/source/> or Google it, idk.

————————————————————————————————————————————————————————————————————————————————————————————————

The other version:

If you use an Arm-based CPU, or if you use Termux, there's a good chance you can simply download the binary(like a 
windows .exe) and run it, no Python install required. To do so:

1. Grab the latest version from <https://github.com/yeetssite/yeetssite.github.io/releases/>

2. In the folder you downloaded it, run:
   [bash]: ~/Downloads/ $ ./asciiFarter

3. If you get an error saying something along the lines of the file not being executable, try:
   [bash]: ~/Downloads/ $ chmod u+r+x ./asciiFarter
   
   Then try step 2 again. If you still have problems, open an issue at <https://github.com/yeetssite.github.io/issues>

————————————————————————————————————————————————————————————————————————————————————————————————

==whatsnew.start==
11.19.2023

What's new in asciiFarter v1.3-alpha:

1. Introduced "whatsnew"
   Run asciiFarter with the "--whatsnew" or "-w" option, and you should receive this message

2. Introduced "textpasta"
   Get a short(or long) story, ramble, or some other stupit bullshit by running asciiFarter
   with the "--textpasta" or "-t" option.

3. First README revision
   See it at <https://github.com/yeetssite/yeetssite.github.io/tree/main/Python/scripts/asciiFarter#readme>
   That's where this whatsnew message is pulled from.

4. Added stats
   Run the thing with "--stats" or "-s" option to get stats on asciiFarter's database.
   Was supposed to be added in v1.2, but was removed due to issues during development.
   If more issues occur, please open an issue at:
   <https://github.com/yeetssite/yeetssite.github.io/issues>

5. Minor performance improvements/Bug fixes

6. Your mom

(i): Run the program with the "--help" option to see all available options and usage.
==whatsnew.end==
