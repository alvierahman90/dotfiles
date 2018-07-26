#!/usr/bin/env python3

import json
import sys
import time

SPEED = 5
TWEETERS = ['billwurtz', 'deiuge']
MAX_LENGTH = 100


def auth_twitter():
    """
    Imports twitter api and returns authorized twitter object
    """
    import twitter
    with open('/home/alvie/.twitter_auth') as file:
        creds = json.loads(file.read())

    twitter = twitter.Twitter(auth=twitter.OAuth(
        creds['token'],
        creds['token_secret'],
        creds['consumer_key'],
        creds['consumer_secret']
        ))
    return twitter


def add_quotes_from_twitter():
    """
    Appends latest quotes from followed tweeters
    """
    twitter = auth_twitter()
    for i in TWEETERS:
        tweets = twitter.statuses.user_timeline(screen_name=i, include_rts=False)

    for i in tweets:
        i['text'] = i['text'].replace('\n', '    ')
        write_quote(i)


def get_quotes():
    """
    Returns all the quotes stored
    """
    output = []
    with open('/home/alvie/.config/polybar/quotes') as file:
        output = json.loads(file.read())
    return output


def write_quotes(quotes):
    """
    Saves `quotes` in json format to file
    """
    with open('/home/alvie/.config/polybar/quotes', 'w') as file:
        file.write(json.dumps(quotes))


def write_quote(quote):
    """
    Adds a single quote
    required object format
    "UNIQUEID" : { "text" : "TEXT" }
    """

    # lazy and hacky way to prevent tweets with URLs making it into my list
    if "http" in quote['text']:
        return
    quotes = get_quotes()
    quotes[quote['id']] = quote
    write_quotes(quotes)


def remove_quote(quote_id):
    """
    Deletes a quote by id
    Returns deleted message on success, return None if quote isn't found
    """
    quotes = get_quotes()
    deleted = quotes.pop(quote_id, None)
    write_quotes(quotes)
    return deleted


# this could probably be implemented by making a list from get_quotes then
# shuffling that in the main() function in the one place it's needed
def shuffle_quotes():
    """
    Shuffles quotes
    TODO write this function
    """
    pass


def get_offset(string):
    """
    Returns the amount the string should be offset to simulate scrolling
    """
    return int(time.time()*SPEED) % len(string)

def add_user_quote(quotes_list, text, custom_id=False):
    """
    Add a custom quote, given text and optional custom id
    """
    quote_object = {}
    quote_object['text'] = text
    if custom_id:
        quote_object['id'] = custom_id
    else:
        id_int = 0
        while True:
            quote_id = "user_" + str(id_int)
            if quote_id not in quotes_list.keys():
                break
            else:
                id_int += 1
        quote_object['id'] = quote_id
    write_quote(quote_object)
    print("Written quote with ID {0}".format(quote_id))
    return 0

def quotes_as_string(quotes):
    """
    Returns all quotes one per line
    """
    string = ''
    for i in quotes.keys():
        string += str(quotes[i]['id']) + "\t" + quotes[i]['text'] + '\n'


def main(debug=False):
    """
    Entry point when script is run
    """
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--add', type=str, help="Add a quote.")
    parser.add_argument('-i', '--custom-id', type=str,
                        default=False,
                        help="A custom id for the quote command. Can be used "
                        "to overwrite quote.")
    parser.add_argument('-l', '--list-quotes', action='store_true',
                        default=False, help="List the quotes.")
    parser.add_argument('-u', '--update-quotes', action='store_true',
                        default=False, help="Grab quotes from twitter.")
    parser.add_argument('-r', '--remove', type=str,
                        help="Remove a quote by id. Prints the quote with "
                        "full details if mistake. ")
    args = parser.parse_args()

    if args.add and args.remove:
        print("You probably shouldn't add and remove a quote at the same "
              + "time.")
        return 0

    quotes = get_quotes()

    if args.add:
        add_user_quote(quotes, args.add, custom_id=args.custom_id)
        return 0

    if args.list_quotes:
        print(quotes_as_string(quotes))
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
        add_quotes_from_twitter()

    if int(time.time()) % 3600 == 0:
        shuffle_quotes()

    preoutput = ""
    for i in quotes.keys():
        preoutput += quotes[i]['text'] + "   -   "
        output = "..."
    for i in range(len(preoutput)):
        if i < MAX_LENGTH:
            offset = (get_offset(preoutput))
            if debug:
                print(i+offset-1)
                print(len(preoutput))
                print(preoutput)
            output += preoutput[(i+offset - 1) % (len(preoutput) - 1)]

    output += '...'

    print(output.lower())
    return 0


if __name__ == "__main__":
    sys.exit(main())
