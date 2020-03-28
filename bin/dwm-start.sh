#!/usr/bin/env zsh

xrandr --output HDMI-A-1 --mode 1920x1080&
xset s off&
xset -dpms&
mpd&
compton&
qbittorrent&
dwm-bar.sh&
wallpaper_set reset&
sleep 5 && mpdas&
rclone mount sa-onedrive: ~/Documents/sa-onedrive --vfs-cache-mode full&
