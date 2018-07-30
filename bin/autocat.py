#!/usr/bin/env python3

# A program to automatically action on certain categories of torrents
# 1. Change BASE
# 2. Set up torrent client
#     - The arguments are: ./script CONTENT-PATH CATEGORY
#     qBittorrent setup:
#         Downloads > Run external script:
#         LOCATION_OF_SCRIPT/autocat.py %F %L

import re
import os
import sys
import json
import time
import argparse
import subprocess
import requests

LOG_FILE = os.path.expanduser("~/.autcat.py.log")
BASE = os.path.expanduser("~/Downloads/Torrents/")


def main():
    args = parse_args()
    file_name = os.path.split(args.file)[1]
    show_name = get_show_name(file_name)

    if args.category == "TV FS":
        print(args.file)
        print(file_name)
        path = generate_path(show_name, args.category) 
        if not os.path.isdir(path):
            subprocess.run(['mkdir',path])
        return link(args.file,
                    generate_path(show_name, args.category) + file_name)
    elif args.category in ["Movie", "Documentary"]:
        return link(args.file,
                    generate_path(file_name, args.category))
    elif args.category == "TV Ep":
        return 1


def parse_args():
    """
    parse command line arguments for script
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("category")
    parser.add_argument("-d", "--dry-run", action='store_true')
    return parser.parse_args()


def get_show_name(file_name):
    """
    get name of a movie to tv show from imdb
    """

    # clean file name before using it in the api request
    file_name = file_name.replace('.', ' ')
    print(file_name)
    file_name = re.split("S[0-9][0-9]", file_name)[0]
    print(file_name)

    # send and process the request
    url = "https://sg.media-imdb.com/suggests/"
    url += file_name[0].lower() + "/"
    url += file_name
    url += ".json"
    response = requests.get(url)
    print(response.text)
    data_json = response.text.split("(")[1].split(")")[0]

    return json.loads(data_json)['d'][0]['l']


def link(original, new, dry_run=False):
    """
    create soft relative link
    """
    command = ['ln', '-rs', original, new]
    log_text = '[' + iso_time() + '] ' + " ".join(command)
    with open(LOG_FILE, "a+") as file:
        file.write(log_text)
        file.write('\n')
    print(log_text)

    if dry_run:
        print(log_text)
        return 0
    return subprocess.run(command).returncode


def generate_path(show_name, category):
    """
    returns the possibly base path
    """

    show_name = '.'.join(show_name.split(' '))

    base = BASE
    if category == "TV FS":
        base += "TV Shows/"
        base += show_name + "/"
    elif category in ['Movie', 'Documentary']:
        base += "Movies/"
        base += show_name

    return base


def iso_time():
    """
    returns time in iso8601 string
    """
    def pad(var, padding=2):
        """
        returns string with padding
        """
        return str(var).zfill(padding)
    t = time.gmtime()
    iso = pad(t.tm_year, padding=4) + \
        '-'+pad(t.tm_mon) + \
        '-'+pad(t.tm_mday) + \
        'T' + \
        pad(t.tm_hour) + \
        ':' + \
        pad(t.tm_min) + \
        ':' + \
        pad(t.tm_sec)

    return iso


if __name__ == "__main__":
    sys.exit(main())
