#!/usr/bin/env bash
# script to turn google photos zip download into pdf

rfilename=./"$(basename $(pwd))"
filename=./"$(basename $(pwd))".md

unzip Photos.zip

echo '
---
title: 
author: Alvie Rahman
date: \today
---' > $filename

exiftran -ai $(ls *jpg*)

for file in $(ls *.jpg)
do
	echo "![]($file)" >> $filename
done

render $filename
convert *.jpg "$rfilename".pdf
zathura "$rfilename".pdf
