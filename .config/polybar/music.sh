#!/usr/bin/env bash

PLAYING_CHAR=">"
NOT_PLAYING_CHAR="|"
NEXT_SONG_MESSAGE=">>"

NO_MUSIC_MESSAGE=""
NO_MUSIC_EXIT_CODE=0

CURRENT_SONG="$(mpc current)"
if [ "$CURRENT_SONG" == "" ]
then
	echo "$NO_MUSIC_MESSAGE"
	exit $NO_MUSIC_EXIT_CODE
fi 

PLAYING=$(mpc status | grep '\[playing\]' -c | sed -e "s/1/$PLAYING_CHAR/" | sed -e "s/0/$NOT_PLAYING_CHAR/")
NEXT_SONG="$(mpc playlist | grep "$CURRENT_SONG" -A 1 | tail -1)"

echo $PLAYING $CURRENT_SONG $NEXT_SONG_MESSAGE $NEXT_SONG
