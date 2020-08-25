#!/usr/bin/env bash
# script to turn google photos zip download into pdf

rfilename=./"$(basename $(pwd))"
filename=./"$(basename $(pwd))".md

echo "extracting photos..."
unzip Photos.zip
echo "removing metadata..."
exiftool -all="" *.jpg
echo "combining into pdf in name order..."
convert *.jpg "$rfilename".pdf
echo "opening using zathura..."
zathura "$rfilename".pdf
