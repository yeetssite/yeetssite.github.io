#!/usr/bin/bash
if [ "$2" == "" ]; then
	IN="$PWD/index.html"
elif [ "$2" == " " ]; then
	IN="$PWD/index.html"
else
	IN="$2"
fi

if [ -f "$IN" ]; then
read -p "$(dirname $(basename $IN))/$(basename $IN): This file already exists, overwrite? [y/n] " CONFIRM1
if [ "${CONFIRM1,,}" == "y" ]; then
	echo -e "[A[2K\r$(dirname $(basename $IN))/$(basename $IN): 0verwritten."
else
	echo -e "[A[2K\r$(dirname $(basename $IN))/$(basename $IN): Unchanged."
	exit 0
fi
fi
tree $1 -H "$3" -L 1 -I index.html --dirsfirst --houtro "" --noreport --hintro "" > $IN
