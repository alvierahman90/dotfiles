#!/usr/bin/env python3

import time
import json

SPEED=5
TWEETERS=['billwurtz','deiuge']
MAX_LENGTH=100

def auth_twitter():
    import twitter
    with open('/home/alvie/.twitter_auth') as f:
        creds = json.loads(f.read())

    t = twitter.Twitter(auth=twitter.OAuth(
        creds['token'],
        creds['token_secret'],
        creds['consumer_key'],
        creds['consumer_secret']
        ))
    return t

def add_quotes_from_twitter(t,user):
    tweets = t.statuses.user_timeline(screen_name=user,include_rts=False)
    quotes = get_quotes()
    
    for i in tweets:
        write_quote(i)

def get_quotes():
    output = []
    with open('/home/alvie/.config/polybar/quotes') as f:
        output = json.loads(f.read())
    return output

def shuffle_quotes():
    # TODO write this function
    pass

def write_quote(quote):
    quotes = get_quotes()
    quotes[quote['id']] = quote
    with open('/home/alvie/.config/polybar/quotes', 'w') as f:
        f.write(json.dumps(quotes))

def get_offset(string):
    return (int(time.time()*SPEED) % len(string))

def main(debug=False):
    preoutput = ''
    quotes = get_quotes()
    for i in quotes.keys():
        preoutput += quotes[i]['text'] + '   -   '
    output="..."
    for i in range(len(preoutput)):
        if i < MAX_LENGTH:
            offset=(get_offset(preoutput))
            if debug:
                print(i+offset-1)
                print(len(preoutput))
                print(preoutput)
            output += preoutput[(i+offset - 1) % (len(preoutput) - 1)]

    output+='...'


    if int(time.time()) % 14400 == 0:
        t = auth_twitter()
        for i in TWEETERS:
            add_quotes_from_twitter(t,i)

    if int(time.time()) % 3600 == 0:
        shuffle_quotes()

    print(output.lower())

if __name__ == "__main__":
    import sys
    if len(sys.argv)== 2:
        if sys.argv[1] == "debug":
            while True:
                main(debug=True)
    main()
