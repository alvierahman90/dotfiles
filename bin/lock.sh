#!/usr/bin/env bash

tmpbg='/tmp/screen.png'
[ "$1" != "nopause" ] && music pause
scrot "$tmpbg"
convert "$tmpbg" -scale 20% -scale 500% "$tmpbg"
i3lock -i "$tmpbg" 
