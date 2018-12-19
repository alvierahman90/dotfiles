#!/usr/bin/env python3

import sys
import subprocess


def get_volume():
    response = subprocess.run("cmus-remote -Q".split(' '), stdout=subprocess.PIPE)
    response = response.stdout.decode('utf-8')
    response = response.split("\n")
    volumes = []
    for property in response:
        property = property.split(' ')
        if len(property) < 3:
            continue
        if "vol_" in property[1]:
            volumes.append(int(property[2]))

    return volumes


def main():
    """ Entry point for script """
    volume = get_volume()
    volume = sum(volume)/len(volume)
    print(str(int(volume)) + "%")
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(0)
