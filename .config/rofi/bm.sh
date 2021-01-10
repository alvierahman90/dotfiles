#!/usr/bin/env bash

case "$1" in
	"")
		# start making file list by putting user-added bookmarks at the top
		#cp $HOME/.bookmarks $HOME/.bmlisttmp

		# add commonly accessed and changing directories
		find "$HOME" -maxdepth 1 -type f -not -path "$HOME/Pictures/*" >> ~/.bmlisttmp
		find "$HOME/Documents/school" -type f >> ~/.bmlisttmp
		find "$HOME/Pictures" -type f -mtime 1 >> ~/.bmlisttmp

		# add pre-scanned directories (generated by bmgen)
		cat ~/.bmlist >> ~/.bmlisttmp

		cat ~/.bmlisttmp
		rm ~/.bmlisttmp
		;;
	*)
		# open the ~/Pictures directory with feh if selected
		[ "$1" == "$HOME/Pictures" ] && coproc (nohup feh "$1" > /dev/null 2) && exec 1>&- && exit
		# otherwise open selected file
		coproc (open "$1" > /dev/null 2>&1) && exec 1>&- && exit
		;;
esac
