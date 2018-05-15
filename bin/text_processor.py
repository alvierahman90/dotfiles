#!/usr/bin/env python3

import os
import sys
import time

def parse_arguments():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, default="input"
            , help="Input file, default is 'input'")
    parser.add_argument("-o", "--output-file", type=str, default="outputs"
            , help="Output file, default is 'outputs'")
    return parser.parse_args()

def iso_time():
    def ztr(var, padding=2):
        return str(var).zfill(padding)

    t = time.gmtime()
    iso = ztr(t.tm_year, padding=4) 
    iso += '-'
    iso +=  ztr(t.tm_mon)
    iso += '-'
    iso += ztr(t.tm_mday)
    iso += 'T'
    iso += ztr(t.tm_hour)
    iso += ':'
    iso += ztr(t.tm_min)
    iso += ':'
    iso += ztr(t.tm_sec)
    return iso

# An example of defining a function to process the text.
# This makes it easy to modify the application.
# All functions take the input and this one takes the argument 'startfrom',
# the number at which the numbered list starts
# 
def numbered_lines(input, startfrom=1, padding="auto", splitter=":: "):
    output = ""
    lines = input.split('\n')
    if padding == "auto" or not isinstance(padding, int): 
        padding = len(str(len(lines)))

    for i in range(len(lines)):
        output +=  str(i+startfrom).zfill(padding) + splitter + lines[i] + "\n"
    
    return output

def wordcount(input):
    return str(len(input.split(' ')))

def main():
    args = parse_arguments()
    with open(args.input) as file:
        input = file.read()

    # Set the function and change arguments
    #
    processor = wordcount
    output = processor(input)

    print(output)

    filepath = os.path.abspath(args.input)
    with open(args.output_file, "a+") as file:
        def pw(key, value):
            return "{0}: {1}\n".format(key,value)

        file.write("----- BEGIN INFO -----\n")
        file.write(pw("Date", iso_time()))
        file.write(pw("File path", filepath))
        file.write("----- BEGIN OUTPUT -----\n")
        file.write(output)
        file.write("\n----- END OUTPUT -----\n")

if __name__ == "__main__":
    sys.exit(main())
