#!/usr/bin/env python3
# Modified from https://github.com/indeedwatson/polybar_twitch

import requests
import time


username = 'alvierahman90'


def getID(client, user):
    '''
    Get the user id from the twitch login username
    '''
    r = requests.get('https://api.twitch.tv/helix/users?login=' + user,
                     headers=client)
    data = r.json()
    reqID = data['data'][0]['id']
    return reqID


def getFollowedChans(client, user):
    '''
    return a list of all the user id's followed by the given user id
    '''
    r = requests.get('https://api.twitch.tv/helix/users/follows?from_id=' +
                     user, headers=client)
    data = r.json()
    # look into this with mpas
    followedChans = list()
    for i in data['data']:
        followedChans.append(i['to_id'])
    return followedChans


def getOnlineChans(channels, headers):
    '''
    Check followed channels to see which are streaming, make a dict with the
    channel name, containing the game name
    '''
    onlineChans = {}
    for stream in channels:
        r = requests.get('https://api.twitch.tv/kraken/streams/' + stream,
                         headers=headers)
        online = r.json()
        if online['stream'] is not None:
            onlineChans[stream] = {'name':
                                   online['stream']['channel']['display_name'],
                                   'game': online['stream']['game']}
            printStreams(onlineChans.items())
            time.sleep(10)


def printStreams(dic):
    streamers_string = ""
    for chan, info in dic:
        streamers_string += info.get('name') + "   "
    print(streamers_string)


headers = {'Client-ID': 'l62zpdkfreec6bbsoffjw0lyjtiwkc',
           'Accept': 'application/vnd.twitchtv.v5+json'}

if __name__ == "__main__":
    userID = getID(headers, username)
    onlineChans = getOnlineChans(getFollowedChans(headers, userID), headers)
    print(' ')
