#!/usr/bin/env python3

import subprocess

APPLICATION = 'cmus'


def player(commands):
    """
    Returns the output of a shell command
    Automatically adds the playerctl command and specifies music player to
    control - cmus
    """
    return subprocess.run(['playerctl', '-p', APPLICATION] + commands,
                          stdout=subprocess.PIPE).stdout.decode('utf-8')[:-1]

def is_player_active():
    """
    Returns True when music player is open, else returns False
    """
    return player(['status']) != 'Not available\n'


def playing():
    """
    Returns True when music is playing, else returns False
    """
    return player(['status']) == 'Playing'


def get_artist():
    """
    Returns the artist of the track as string
    """
    return player(['metadata', 'xesam:artist'])


def get_track():
    """
    Returns the track name as string
    """
    return player(['metadata', 'xesam:title'])


def get_album():
    """
    Returns the album name as string
    """
    return player(['metadata', 'xesam:album'])


def status_symbol():
    """
    Returns a symbol based on if music is playing
    """
    if playing():
        return '>'
    return '|'


def blink(text):
    """
    Flashes text given once a second
    """
    from time import time

    if int(time()) % 2 == 0:
        return text
    return ' ' * len(text)


def main():
    """
    Main function when script is run
    """
    if not is_player_active():
        print('cmus not running')
        return 0

    if get_track() == "":
        print("no music playing")
        return 0

    status_message = "{playing} {track} - {artist}".format(
        playing=status_symbol(),
        track=get_track(),
        artist=get_artist()
    )

    print(status_message)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main())
