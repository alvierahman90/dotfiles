#!/bin/bash
options=""
filename="/home/alvie/Pictures/Screenshot-$(date --iso-8601=ns).png"

if [ "$1" == "select" ]
then
	options="$options --select"
elif [ "$1" == "focused" ]
then
	options="$options --focused"
fi

sleep 0.1
scrot $options "$filename"
convert "$filename" \( +clone -background black -shadow 57x15+0+13 \) +swap -background transparent -layers merge +repage "$filename"
xclip -selection clipboard -target image/png $filename
