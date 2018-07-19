#!/usr/bin/env python3

import subprocess

application = 'cmus'


def player(commands):
    return subprocess.run(['playerctl', '-p', application] + commands,
                          stdout=subprocess.PIPE).stdout.decode('utf-8')


def is_player_active():
    return player(['status']) != 'Not available\n'


def playing():
    if player(['status']) == 'Playing\n':
        return True
    return False


def get_artist():
    return player(['metadata', 'xesam:artist'])


def get_track():
    return player(['metadata', 'xesam:title'])


def get_album():
    return player(['metadata', 'xesam:album'])


def get_album_artist():
    song_artist = get_artist()
    album_artist = player(['metadata', 'xesam:albumArtist'])
    if song_artist == album_artist:
        return 'their'
    return "{}'s".format(album_artist)


def status_symbol():
    if playing():
        return '>'
    return '|'


def blinker(text):
    from time import time

    if int(time()) % 2 == 0:
        return text
    return ' ' * len(text)


def main():
    if not is_player_active():
        print('cmus not running')
        return 0

    if get_track() == "":
        print("no music playing")
        return 0

    if playing():
        status_message = "{playing} {track} - {artist}".format(
            playing=status_symbol(),
            track=get_track(),
            artist=get_artist())
    else:
        status_message = "{playing} {track}".format(
            playing=status_symbol(),
            track=get_track())
    print(status_message)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
