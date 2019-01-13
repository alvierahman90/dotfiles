#!/bin/bash

images_dir="./images"

# get filename

printf "Filename (./images/ already prefixed): "
read filename
echo $filename

# get screenshot mode

printf "Type (s or f or blank): "
read mode

if [ "$mode" == "s" ]
then
	options="$options --select"
	echo "Make selection now"
elif [ "$mode" == "f" ]
then
	options="$options --focused"
fi

# check if images directory exists

if [ ! -d "$images_dir" ]; then
	mkdir $images_dir
fi

# take screenshot

scrot $options "$images_dir/$filename"
xclip -selection clipboard -target image/png $filename

printf "Open picture? (y/n/blank) "
read open

if [ "$open" == "y" ]
then
	feh "$images_dir/$filename"
fi
