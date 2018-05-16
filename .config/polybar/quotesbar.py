#!/usr/bin/env python3

import json
import sys
import time

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
        i['text'] = i['text'].replace('\n','    ')
        write_quote(i)

def get_quotes():
    output = []
    with open('/home/alvie/.config/polybar/quotes') as f:
        output = json.loads(f.read())
    return output

# overwrite the whole thing as opposed to adding one
def write_quotes(quotes):
    with open('/home/alvie/.config/polybar/quotes', 'w') as f:
        f.write(json.dumps(quotes))


# required object format
# "UNIQUEID" : { "text" : "TEXT" }

# add a quote as opposed to overwriting the whole thing
def write_quote(quote):
    # lazy and hacky way to prevent tweets with URLs making it into my list
    if "http" in quote['text']:
        return 1
    quotes = get_quotes()
    quotes[quote['id']] = quote
    write_quotes(quotes)

# returns deleted message on success, return None if quote isn't found
def remove_quote(quote_id):
    quotes = get_quotes()
    deleted = quotes.pop(quote_id, None)
    write_quotes(quotes)
    return deleted

# this could probably be implemented by making a list from get_quotes then
# shuffling that in the main() function in the one place it's needed
def shuffle_quotes():
    # TODO write this function
    pass

def get_offset(string):
    return (int(time.time()*SPEED) % len(string))

def main(debug=False):
    import argparse


    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--add', type=str, help="Add a quote.")
    parser.add_argument('-i', '--custom-id', type=str, 
     default=False,
     help="A custom id for the quote command. Can be used to overwrite quote.")
    parser.add_argument('-l', '--list-quotes', action='store_true', 
     default=False, help="List the quotes.")
    parser.add_argument('-u', '--update_quotes', action='store_true', 
     default=False, help="Grab quotes from twitter.")
    parser.add_argument('-r', '--remove', type=str, 
     help="Remove a quote by id. Prints the quote with full details if mistake. ")
    args = parser.parse_args()

    if args.add and args.remove:
        print("You probably shouldn't add and remove a quote at the same time.")
        print("Exiting...")
        return 0

    quotes = get_quotes()

    if args.add:
        quote_object = {}
        quote_object['text'] = args.add
        if args.custom_id:
            quote_object['id'] = args.custom_id
        else:
            id_int = 0
            while True:
                quote_id = "user_" + str(id_int)
                if quote_id not in quotes.keys():
                    break
                else:
                    id_int += 1
            quote_object['id'] = quote_id
        write_quote(quote_object)
        print("Written quote with ID {0}".format(quote_id))
        return 0

    if args.list_quotes:
        for i in quotes.keys():
            print(str(quotes[i]['id']) + "\t" + quotes[i]['text'])
        return 0

    if args.remove:
        print("Deleting entry with ID {0}".format(args.remove))
        deleted = remove_quote(args.remove)
        if deleted is None:
            print("ID not found.")
            return 1
        print(str(deleted))
        return 0

    if int(time.time()) % 14400 == 0 or args.update_quotes:
        t = auth_twitter()
        for i in TWEETERS:
            add_quotes_from_twitter(t,i)

    if int(time.time()) % 3600 == 0:
        shuffle_quotes()

    preoutput = ""
    for i in quotes.keys():
        preoutput += quotes[i]['text'] + "   -   "
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



    print(output.lower())

if __name__ == "__main__":
    sys.exit(main())
