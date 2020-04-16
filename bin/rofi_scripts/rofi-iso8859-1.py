#!/usr/bin/env python3
# Alvie Rahman 2018 - Most code ripped from rofimoji:
#
# MIT License
#
# Copyright (c) 2017 Fabian Winter
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from subprocess import Popen, PIPE
from time import sleep


characters = ''
chardict = [
  {
    "code": "\u00A1",
    "name": "INVERTED EXCLAMATION MARK"
  },
  {
    "code": "\u00A2",
    "name": "CENT SIGN"
  },
  {
    "code": "\u00A3",
    "name": "POUND SIGN"
  },
  {
    "code": "\u00A4",
    "name": "CURRENCY SIGN"
  },
  {
    "code": "\u00A5",
    "name": "YEN SIGN"
  },
  {
    "code": "\u00A6",
    "name": "BROKEN BAR"
  },
  {
    "code": "\u00A7",
    "name": "SECTION SIGN"
  },
  {
    "code": "\u00A8",
    "name": "DIAERESIS"
  },
  {
    "code": "\u00A9",
    "name": "COPYRIGHT SIGN"
  },
  {
    "code": "\u00AA",
    "name": "FEMININE ORDINAL INDICATOR"
  },
  {
    "code": "\u00AB",
    "name": "LEFT-POINTING DOUBLE ANGLE QUOTATION MARK"
  },
  {
    "code": "\u00AC",
    "name": "NOT SIGN"
  },
  {
    "code": "\u00AD",
    "name": "SOFT HYPHEN"
  },
  {
    "code": "\u00AE",
    "name": "REGISTERED SIGN"
  },
  {
    "code": "\u00AF",
    "name": "MACRON"
  },
  {
    "code": "\u00B0",
    "name": "DEGREE SIGN"
  },
  {
    "code": "\u00B1",
    "name": "PLUS-MINUS SIGN"
  },
  {
    "code": "\u00B2",
    "name": "SUPERSCRIPT TWO"
  },
  {
    "code": "\u00B3",
    "name": "SUPERSCRIPT THREE"
  },
  {
    "code": "\u00B4",
    "name": "ACUTE ACCENT"
  },
  {
    "code": "\u00B5",
    "name": "MICRO SIGN"
  },
  {
    "code": "\u00B6",
    "name": "PILCROW SIGN"
  },
  {
    "code": "\u00B7",
    "name": "MIDDLE DOT"
  },
  {
    "code": "\u00B8",
    "name": "CEDILLA"
  },
  {
    "code": "\u00B9",
    "name": "SUPERSCRIPT ONE"
  },
  {
    "code": "\u00BA",
    "name": "MASCULINE ORDINAL INDICATOR"
  },
  {
    "code": "\u00BB",
    "name": "RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK"
  },
  {
    "code": "\u00BC",
    "name": "VULGAR FRACTION ONE QUARTER"
  },
  {
    "code": "\u00BD",
    "name": "VULGAR FRACTION ONE HALF"
  },
  {
    "code": "\u00BE",
    "name": "VULGAR FRACTION THREE QUARTERS"
  },
  {
    "code": "\u00BF",
    "name": "INVERTED QUESTION MARK"
  },
  {
    "code": "\u00C0",
    "name": "A WITH GRAVE"
  },
  {
    "code": "\u00C1",
    "name": "A WITH ACUTE"
  },
  {
    "code": "\u00C2",
    "name": "A WITH CIRCUMFLEX"
  },
  {
    "code": "\u00C3",
    "name": "A WITH TILDE"
  },
  {
    "code": "\u00C4",
    "name": "A WITH DIAERESIS"
  },
  {
    "code": "\u00C5",
    "name": "A WITH RING ABOVE"
  },
  {
    "code": "\u00C6",
    "name": "AE"
  },
  {
    "code": "\u00C7",
    "name": "C WITH CEDILLA"
  },
  {
    "code": "\u00C8",
    "name": "E WITH GRAVE"
  },
  {
    "code": "\u00C9",
    "name": "E WITH ACUTE"
  },
  {
    "code": "\u00CA",
    "name": "E WITH CIRCUMFLEX"
  },
  {
    "code": "\u00CB",
    "name": "E WITH DIAERESIS"
  },
  {
    "code": "\u00CC",
    "name": "I WITH GRAVE"
  },
  {
    "code": "\u00CD",
    "name": "I WITH ACUTE"
  },
  {
    "code": "\u00CE",
    "name": "I WITH CIRCUMFLEX"
  },
  {
    "code": "\u00CF",
    "name": "I WITH DIAERESIS"
  },
  {
    "code": "\u00D0",
    "name": "ETH (Icelandic)"
  },
  {
    "code": "\u00D1",
    "name": "N WITH TILDE"
  },
  {
    "code": "\u00D2",
    "name": "O WITH GRAVE"
  },
  {
    "code": "\u00D3",
    "name": "O WITH ACUTE"
  },
  {
    "code": "\u00D4",
    "name": "O WITH CIRCUMFLEX"
  },
  {
    "code": "\u00D5",
    "name": "O WITH TILDE"
  },
  {
    "code": "\u00D6",
    "name": "O WITH DIAERESIS"
  },
  {
    "code": "\u00D7",
    "name": "MULTIPLICATION SIGN"
  },
  {
    "code": "\u00D8",
    "name": "O WITH STROKE"
  },
  {
    "code": "\u00D9",
    "name": "U WITH GRAVE"
  },
  {
    "code": "\u00DA",
    "name": "U WITH ACUTE"
  },
  {
    "code": "\u00DB",
    "name": "U WITH CIRCUMFLEX"
  },
  {
    "code": "\u00DC",
    "name": "U WITH DIAERESIS"
  },
  {
    "code": "\u00DD",
    "name": "Y WITH ACUTE"
  },
  {
    "code": "\u00DE",
    "name": "THORN (Icelandic)"
  },
  {
    "code": "\u00DF",
    "name": "SHARP S (German)"
  },
  {
    "code": "\u00E0",
    "name": "A WITH GRAVE"
  },
  {
    "code": "\u00E1",
    "name": "A WITH ACUTE"
  },
  {
    "code": "\u00E2",
    "name": "A WITH CIRCUMFLEX"
  },
  {
    "code": "\u00E3",
    "name": "A WITH TILDE"
  },
  {
    "code": "\u00E4",
    "name": "A WITH DIAERESIS"
  },
  {
    "code": "\u00E5",
    "name": "A WITH RING ABOVE"
  },
  {
    "code": "\u00E6",
    "name": "AE"
  },
  {
    "code": "\u00E7",
    "name": "C WITH CEDILLA"
  },
  {
    "code": "\u00E8",
    "name": "E WITH GRAVE"
  },
  {
    "code": "\u00E9",
    "name": "E WITH ACUTE"
  },
  {
    "code": "\u00EA",
    "name": "E WITH CIRCUMFLEX"
  },
  {
    "code": "\u00EB",
    "name": "E WITH DIAERESIS"
  },
  {
    "code": "\u00EC",
    "name": "I WITH GRAVE"
  },
  {
    "code": "\u00ED",
    "name": "I WITH ACUTE"
  },
  {
    "code": "\u00EE",
    "name": "I WITH CIRCUMFLEX"
  },
  {
    "code": "\u00EF",
    "name": "I WITH DIAERESIS"
  },
  {
    "code": "\u00F0",
    "name": "ETH (Icelandic)"
  },
  {
    "code": "\u00F1",
    "name": "N WITH TILDE"
  },
  {
    "code": "\u00F2",
    "name": "O WITH GRAVE"
  },
  {
    "code": "\u00F3",
    "name": "O WITH ACUTE"
  },
  {
    "code": "\u00F4",
    "name": "O WITH CIRCUMFLEX"
  },
  {
    "code": "\u00F5",
    "name": "O WITH TILDE"
  },
  {
    "code": "\u00F6",
    "name": "O WITH DIAERESIS"
  },
  {
    "code": "\u00F7",
    "name": "DIVISION SIGN"
  },
  {
    "code": "\u00F8",
    "name": "O WITH STROKE"
  },
  {
    "code": "\u00F9",
    "name": "U WITH GRAVE"
  },
  {
    "code": "\u00FA",
    "name": "U WITH ACUTE"
  },
  {
    "code": "\u00FB",
    "name": "U WITH CIRCUMFLEX"
  },
  {
    "code": "\u00FC",
    "name": "U WITH DIAERESIS"
  },
  {
    "code": "\u00FD",
    "name": "Y WITH ACUTE"
  },
  {
    "code": "\u00FE",
    "name": "THORN (Icelandic)"
  },
  {
    "code": "\u00FF",
    "name": "Y WITH DIAERESIS"
  },
  {
          "code": "Δ",
          "name": "Uppercase delta"
          },
  {
          "code": "π",
          "name": "pi"
          }
]

for i in chardict:
    characters += i['code'] + '\t' + i['name'] + '\n'


rofi = Popen(
      args=[
            'rofi-preconf',
            '-dmenu',
            '-i',
            '-p',
            'character',
            '-kb-custom-1',
            'Alt+c'
      ],
      stdin=PIPE,
      stdout=PIPE
)

(stdout, stderr) = rofi.communicate(input=characters.encode('utf-8'))
sleep(0.1)
if rofi.returncode == 1:
    exit()
else:
    character = stdout.split()[0]
    if rofi.returncode == 0:
        Popen(
            args=[
                'xdotool',
                'type',
                '--clearmodifiers',
                character.decode('utf-8')
            ]
        )
        xsel = Popen(
            args=[
                'xsel',
                '-i',
                '-b'
            ],
            stdin=PIPE
        )
        xsel.communicate(input=character)
