#!/usr/bin/env python3

import json
import subprocess

def player(commands):
    return subprocess.run(['playerctl'] + commands
            , stdout=subprocess.PIPE).stdout.decode('utf-8')

def get_status():
    if player(['status']) == 'Playing\n':
        return "'re"
    elif player(['status']) == 'Paused\n':
        return " were"

def get_artist():
    return player(['metadata','xesam:artist'])

def get_track():
    return player(['metadata','xesam:title'])

def get_album():
    return player(['metadata','xesam:album'])

def get_album_artist():
    song_artist = get_artist()
    album_artist = player(['metadata','xesam:albumArtist'])
    if song_artist == album_artist:
        return 'their'
    else:
        return "{}'s".format(album_artist)


# status_message = "You{status} listening to {artist}'s \"{track}\" from "
    # "{album_artist} album \"{album}\".".format(
        # status = get_status()
        # , artist = get_artist()
        # , track = get_track()
        # , album = get_album()
        # , album_artist = get_album_artist()
        # )

if get_track() == "":
    print("No is music currently playing")
    exit(0)

status_message = "{track} - {artist}".format(
        track = get_track()
        , artist = get_artist()
        )

print(status_message)
