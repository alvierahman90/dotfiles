#!/usr/bin/env bash

sep="   "

print_mpd_info(){
	playing="playing"
	[[ -z "$(mpc status | grep -o --color=never 'playing')" ]] && playing=""
	echo -n "$sep$playing $(mpc current)"

}

print_date(){
	echo -n "$sep$(date "+%A %Y-%m-%d %H:%M:%S (%Z)")"
}

print_active_window_time(){
	pid="$(xdotool getactivewindow getwindowpid)"
	echo "$sep$(ps -o etime= -p $pid | sed -s 's/  *//')"
}

while true
do
	val="$(print_mpd_info)$(print_active_window_time)$(print_date)$sep$(echo dwm-ar90)"
	xsetroot -name "$val"
	sleep 1
done
