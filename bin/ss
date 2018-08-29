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

scrot $options "$filename"
xclip -selection clipboard -target image/png $filename
