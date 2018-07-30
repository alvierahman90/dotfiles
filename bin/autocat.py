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
import datetime
import argparse
import subprocess
import requests

BASE = os.path.expanduser("~/Downloads/Torrents/")


def main():
    """
    Entry point for script
    """
    args = parse_args()
    print("main: starting at " + iso_time())
    print("main: args.file: " + args.file)
    if args.dry_run:
        print("main: DRY RUN: No linking will happen")

    if args.file[-1] == '/':
        file_name = os.path.split(args.file[:-1])[1]
    else:
        file_name = os.path.split(args.file)[1]

    if file_name == "":
        file_name = os.path.split(file_name)[1]
    print("main: file_name" + file_name)
    show_name = get_show_name(file_name)

    if args.category == "TV FS":
        path = generate_path(show_name, args.category)
        if not os.path.isdir(path):
            subprocess.run(['mkdir', path])
        return link(args.file,
                    generate_path(show_name, args.category) + file_name, dry_run=args.dry_run)
    elif args.category in ["Movie", "Documentary"]:
        return link(args.file,
                    generate_path(file_name, args.category), dry_run=args.dry_run)
    elif args.category == "TV Ep":
        # TODO implement automagic linking of single episodes
        print("main: single episodes not implemented yet")
        return 1
    else:
        print("main: this category has not been implemented yet")
        return 1


def parse_args():
    """
    Parse command line arguments for script
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("category")
    parser.add_argument("-d", "--dry-run", action='store_true')
    return parser.parse_args()


def get_show_name(file_name):
    """
    Get name of a movie to tv show from imdb
    """

    # clean file name before using it in the api request
    file_name = file_name.replace('.', ' ')
    print("get_show_name: file_name.replace('.', ' '): " + file_name)
    file_name = re.split("S[0-9][0-9]", file_name)[0]
    print("get_show_name: re.split(\"S[0-9][0-9]\", file_name)[0]: " + file_name)

    # send and process the request
    url = "https://sg.media-imdb.com/suggests/"
    url += file_name[0].lower() + "/"
    url += file_name
    url += ".json"
    response = requests.get(url)
    print("get_show_name: =====IMDB RESPONSE START=====")
    print(response.text)
    print("=====IMDB RESPONSE END=====")
    data_json = response.text.split("(")[1].split(")")[0]

    return json.loads(data_json)['d'][0]['l']


def link(original, new, dry_run=False):
    """
    Create soft relative link
    """
    command = ['ln', '-rs', original, new]
    log_text = '[' + iso_time() + '] ' + " ".join(command)
    print("link: " + log_text)

    if dry_run:
        return 0
    return subprocess.run(command).returncode


def generate_path(show_name, category):
    """
    Returns the possibly base path
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
    Returns time in iso8601 string
    """
    return datetime.datetime.now().isoformat()


if __name__ == "__main__":
    sys.exit(main())
