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


characters = ''
chardict = [{
    "code": "\u0000",
    "name": "NULL"
  },
  {
    "code": "\u0001",
    "name": "START OF HEADING"
  },
  {
    "code": "\u0002",
    "name": "START OF TEXT"
  },
  {
    "code": "\u0003",
    "name": "END OF TEXT"
  },
  {
    "code": "\u0004",
    "name": "END OF TRANSMISSION"
  },
  {
    "code": "\u0005",
    "name": "ENQUIRY"
  },
  {
    "code": "\u0006",
    "name": "ACKNOWLEDGE"
  },
  {
    "code": "\u0007",
    "name": "BELL"
  },
  {
    "code": "\u0008",
    "name": "BACKSPACE"
  },
  {
    "code": "\u0009",
    "name": "HORIZONTAL TABULATION"
  },
  {
    "code": "\u000A",
    "name": "LINE FEED"
  },
  {
    "code": "\u000B",
    "name": "VERTICAL TABULATION"
  },
  {
    "code": "\u000C",
    "name": "FORM FEED"
  },
  {
    "code": "\u000D",
    "name": "CARRIAGE RETURN"
  },
  {
    "code": "\u000E",
    "name": "SHIFT OUT"
  },
  {
    "code": "\u000F",
    "name": "SHIFT IN"
  },
  {
    "code": "\u0010",
    "name": "DATA LINK ESCAPE"
  },
  {
    "code": "\u0011",
    "name": "DEVICE CONTROL ONE"
  },
  {
    "code": "\u0012",
    "name": "DEVICE CONTROL TWO"
  },
  {
    "code": "\u0013",
    "name": "DEVICE CONTROL THREE"
  },
  {
    "code": "\u0014",
    "name": "DEVICE CONTROL FOUR"
  },
  {
    "code": "\u0015",
    "name": "NEGATIVE ACKNOWLEDGE"
  },
  {
    "code": "\u0016",
    "name": "SYNCHRONOUS IDLE"
  },
  {
    "code": "\u0017",
    "name": "END OF TRANSMISSION BLOCK"
  },
  {
    "code": "\u0018",
    "name": "CANCEL"
  },
  {
    "code": "\u0019",
    "name": "END OF MEDIUM"
  },
  {
    "code": "\u001A",
    "name": "SUBSTITUTE"
  },
  {
    "code": "\u001B",
    "name": "ESCAPE"
  },
  {
    "code": "\u001C",
    "name": "FILE SEPARATOR"
  },
  {
    "code": "\u001D",
    "name": "GROUP SEPARATOR"
  },
  {
    "code": "\u001E",
    "name": "RECORD SEPARATOR"
  },
  {
    "code": "\u001F",
    "name": "UNIT SEPARATOR"
  },
  {
    "code": "\u0020",
    "name": "SPACE"
  },
  {
    "code": "\u0021",
    "name": "EXCLAMATION MARK"
  },
  {
    "code": "\u0022",
    "name": "QUOTATION MARK"
  },
  {
    "code": "\u0023",
    "name": "NUMBER SIGN"
  },
  {
    "code": "\u0024",
    "name": "DOLLAR SIGN"
  },
  {
    "code": "\u0025",
    "name": "PERCENT SIGN"
  },
  {
    "code": "\u0026",
    "name": "AMPERSAND"
  },
  {
    "code": "\u0027",
    "name": "APOSTROPHE"
  },
  {
    "code": "\u0028",
    "name": "LEFT PARENTHESIS"
  },
  {
    "code": "\u0029",
    "name": "RIGHT PARENTHESIS"
  },
  {
    "code": "\u002A",
    "name": "ASTERISK"
  },
  {
    "code": "\u002B",
    "name": "PLUS SIGN"
  },
  {
    "code": "\u002C",
    "name": "COMMA"
  },
  {
    "code": "\u002D",
    "name": "HYPHEN-MINUS"
  },
  {
    "code": "\u002E",
    "name": "FULL STOP"
  },
  {
    "code": "\u002F",
    "name": "SOLIDUS"
  },
  {
    "code": "\u0030",
    "name": "DIGIT ZERO"
  },
  {
    "code": "\u0031",
    "name": "DIGIT ONE"
  },
  {
    "code": "\u0032",
    "name": "DIGIT TWO"
  },
  {
    "code": "\u0033",
    "name": "DIGIT THREE"
  },
  {
    "code": "\u0034",
    "name": "DIGIT FOUR"
  },
  {
    "code": "\u0035",
    "name": "DIGIT FIVE"
  },
  {
    "code": "\u0036",
    "name": "DIGIT SIX"
  },
  {
    "code": "\u0037",
    "name": "DIGIT SEVEN"
  },
  {
    "code": "\u0038",
    "name": "DIGIT EIGHT"
  },
  {
    "code": "\u0039",
    "name": "DIGIT NINE"
  },
  {
    "code": "\u003A",
    "name": "COLON"
  },
  {
    "code": "\u003B",
    "name": "SEMICOLON"
  },
  {
    "code": "\u003C",
    "name": "LESS-THAN SIGN"
  },
  {
    "code": "\u003D",
    "name": "EQUALS SIGN"
  },
  {
    "code": "\u003E",
    "name": "GREATER-THAN SIGN"
  },
  {
    "code": "\u003F",
    "name": "QUESTION MARK"
  },
  {
    "code": "\u0040",
    "name": "COMMERCIAL AT"
  },
  {
    "code": "\u0041",
    "name": "LATIN CAPITAL LETTER A"
  },
  {
    "code": "\u0042",
    "name": "LATIN CAPITAL LETTER B"
  },
  {
    "code": "\u0043",
    "name": "LATIN CAPITAL LETTER C"
  },
  {
    "code": "\u0044",
    "name": "LATIN CAPITAL LETTER D"
  },
  {
    "code": "\u0045",
    "name": "LATIN CAPITAL LETTER E"
  },
  {
    "code": "\u0046",
    "name": "LATIN CAPITAL LETTER F"
  },
  {
    "code": "\u0047",
    "name": "LATIN CAPITAL LETTER G"
  },
  {
    "code": "\u0048",
    "name": "LATIN CAPITAL LETTER H"
  },
  {
    "code": "\u0049",
    "name": "LATIN CAPITAL LETTER I"
  },
  {
    "code": "\u004A",
    "name": "LATIN CAPITAL LETTER J"
  },
  {
    "code": "\u004B",
    "name": "LATIN CAPITAL LETTER K"
  },
  {
    "code": "\u004C",
    "name": "LATIN CAPITAL LETTER L"
  },
  {
    "code": "\u004D",
    "name": "LATIN CAPITAL LETTER M"
  },
  {
    "code": "\u004E",
    "name": "LATIN CAPITAL LETTER N"
  },
  {
    "code": "\u004F",
    "name": "LATIN CAPITAL LETTER O"
  },
  {
    "code": "\u0050",
    "name": "LATIN CAPITAL LETTER P"
  },
  {
    "code": "\u0051",
    "name": "LATIN CAPITAL LETTER Q"
  },
  {
    "code": "\u0052",
    "name": "LATIN CAPITAL LETTER R"
  },
  {
    "code": "\u0053",
    "name": "LATIN CAPITAL LETTER S"
  },
  {
    "code": "\u0054",
    "name": "LATIN CAPITAL LETTER T"
  },
  {
    "code": "\u0055",
    "name": "LATIN CAPITAL LETTER U"
  },
  {
    "code": "\u0056",
    "name": "LATIN CAPITAL LETTER V"
  },
  {
    "code": "\u0057",
    "name": "LATIN CAPITAL LETTER W"
  },
  {
    "code": "\u0058",
    "name": "LATIN CAPITAL LETTER X"
  },
  {
    "code": "\u0059",
    "name": "LATIN CAPITAL LETTER Y"
  },
  {
    "code": "\u005A",
    "name": "LATIN CAPITAL LETTER Z"
  },
  {
    "code": "\u005B",
    "name": "LEFT SQUARE BRACKET"
  },
  {
    "code": "\u005C",
    "name": "REVERSE SOLIDUS"
  },
  {
    "code": "\u005D",
    "name": "RIGHT SQUARE BRACKET"
  },
  {
    "code": "\u005E",
    "name": "CIRCUMFLEX ACCENT"
  },
  {
    "code": "\u005F",
    "name": "LOW LINE"
  },
  {
    "code": "\u0060",
    "name": "GRAVE ACCENT"
  },
  {
    "code": "\u0061",
    "name": "LATIN SMALL LETTER A"
  },
  {
    "code": "\u0062",
    "name": "LATIN SMALL LETTER B"
  },
  {
    "code": "\u0063",
    "name": "LATIN SMALL LETTER C"
  },
  {
    "code": "\u0064",
    "name": "LATIN SMALL LETTER D"
  },
  {
    "code": "\u0065",
    "name": "LATIN SMALL LETTER E"
  },
  {
    "code": "\u0066",
    "name": "LATIN SMALL LETTER F"
  },
  {
    "code": "\u0067",
    "name": "LATIN SMALL LETTER G"
  },
  {
    "code": "\u0068",
    "name": "LATIN SMALL LETTER H"
  },
  {
    "code": "\u0069",
    "name": "LATIN SMALL LETTER I"
  },
  {
    "code": "\u006A",
    "name": "LATIN SMALL LETTER J"
  },
  {
    "code": "\u006B",
    "name": "LATIN SMALL LETTER K"
  },
  {
    "code": "\u006C",
    "name": "LATIN SMALL LETTER L"
  },
  {
    "code": "\u006D",
    "name": "LATIN SMALL LETTER M"
  },
  {
    "code": "\u006E",
    "name": "LATIN SMALL LETTER N"
  },
  {
    "code": "\u006F",
    "name": "LATIN SMALL LETTER O"
  },
  {
    "code": "\u0070",
    "name": "LATIN SMALL LETTER P"
  },
  {
    "code": "\u0071",
    "name": "LATIN SMALL LETTER Q"
  },
  {
    "code": "\u0072",
    "name": "LATIN SMALL LETTER R"
  },
  {
    "code": "\u0073",
    "name": "LATIN SMALL LETTER S"
  },
  {
    "code": "\u0074",
    "name": "LATIN SMALL LETTER T"
  },
  {
    "code": "\u0075",
    "name": "LATIN SMALL LETTER U"
  },
  {
    "code": "\u0076",
    "name": "LATIN SMALL LETTER V"
  },
  {
    "code": "\u0077",
    "name": "LATIN SMALL LETTER W"
  },
  {
    "code": "\u0078",
    "name": "LATIN SMALL LETTER X"
  },
  {
    "code": "\u0079",
    "name": "LATIN SMALL LETTER Y"
  },
  {
    "code": "\u007A",
    "name": "LATIN SMALL LETTER Z"
  },
  {
    "code": "\u007B",
    "name": "LEFT CURLY BRACKET"
  },
  {
    "code": "\u007C",
    "name": "VERTICAL LINE"
  },
  {
    "code": "\u007D",
    "name": "RIGHT CURLY BRACKET"
  },
  {
    "code": "\u007E",
    "name": "TILDE"
  },
  {
    "code": "\u007F",
    "name": "DELETE"
  },
  {
    "code": "\u0080",
    "name": "<control>"
  },
  {
    "code": "\u0081",
    "name": "<control>"
  },
  {
    "code": "\u0082",
    "name": "<control>"
  },
  {
    "code": "\u0083",
    "name": "<control>"
  },
  {
    "code": "\u0084",
    "name": "<control>"
  },
  {
    "code": "\u0085",
    "name": "<control>"
  },
  {
    "code": "\u0086",
    "name": "<control>"
  },
  {
    "code": "\u0087",
    "name": "<control>"
  },
  {
    "code": "\u0088",
    "name": "<control>"
  },
  {
    "code": "\u0089",
    "name": "<control>"
  },
  {
    "code": "\u008A",
    "name": "<control>"
  },
  {
    "code": "\u008B",
    "name": "<control>"
  },
  {
    "code": "\u008C",
    "name": "<control>"
  },
  {
    "code": "\u008D",
    "name": "<control>"
  },
  {
    "code": "\u008E",
    "name": "<control>"
  },
  {
    "code": "\u008F",
    "name": "<control>"
  },
  {
    "code": "\u0090",
    "name": "<control>"
  },
  {
    "code": "\u0091",
    "name": "<control>"
  },
  {
    "code": "\u0092",
    "name": "<control>"
  },
  {
    "code": "\u0093",
    "name": "<control>"
  },
  {
    "code": "\u0094",
    "name": "<control>"
  },
  {
    "code": "\u0095",
    "name": "<control>"
  },
  {
    "code": "\u0096",
    "name": "<control>"
  },
  {
    "code": "\u0097",
    "name": "<control>"
  },
  {
    "code": "\u0098",
    "name": "<control>"
  },
  {
    "code": "\u0099",
    "name": "<control>"
  },
  {
    "code": "\u009A",
    "name": "<control>"
  },
  {
    "code": "\u009B",
    "name": "<control>"
  },
  {
    "code": "\u009C",
    "name": "<control>"
  },
  {
    "code": "\u009D",
    "name": "<control>"
  },
  {
    "code": "\u009E",
    "name": "<control>"
  },
  {
    "code": "\u009F",
    "name": "<control>"
  },
  {
    "code": "\u00A0",
    "name": "NO-BREAK SPACE"
  },
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
    "name": "LATIN CAPITAL LETTER A WITH GRAVE"
  },
  {
    "code": "\u00C1",
    "name": "LATIN CAPITAL LETTER A WITH ACUTE"
  },
  {
    "code": "\u00C2",
    "name": "LATIN CAPITAL LETTER A WITH CIRCUMFLEX"
  },
  {
    "code": "\u00C3",
    "name": "LATIN CAPITAL LETTER A WITH TILDE"
  },
  {
    "code": "\u00C4",
    "name": "LATIN CAPITAL LETTER A WITH DIAERESIS"
  },
  {
    "code": "\u00C5",
    "name": "LATIN CAPITAL LETTER A WITH RING ABOVE"
  },
  {
    "code": "\u00C6",
    "name": "LATIN CAPITAL LETTER AE"
  },
  {
    "code": "\u00C7",
    "name": "LATIN CAPITAL LETTER C WITH CEDILLA"
  },
  {
    "code": "\u00C8",
    "name": "LATIN CAPITAL LETTER E WITH GRAVE"
  },
  {
    "code": "\u00C9",
    "name": "LATIN CAPITAL LETTER E WITH ACUTE"
  },
  {
    "code": "\u00CA",
    "name": "LATIN CAPITAL LETTER E WITH CIRCUMFLEX"
  },
  {
    "code": "\u00CB",
    "name": "LATIN CAPITAL LETTER E WITH DIAERESIS"
  },
  {
    "code": "\u00CC",
    "name": "LATIN CAPITAL LETTER I WITH GRAVE"
  },
  {
    "code": "\u00CD",
    "name": "LATIN CAPITAL LETTER I WITH ACUTE"
  },
  {
    "code": "\u00CE",
    "name": "LATIN CAPITAL LETTER I WITH CIRCUMFLEX"
  },
  {
    "code": "\u00CF",
    "name": "LATIN CAPITAL LETTER I WITH DIAERESIS"
  },
  {
    "code": "\u00D0",
    "name": "LATIN CAPITAL LETTER ETH (Icelandic)"
  },
  {
    "code": "\u00D1",
    "name": "LATIN CAPITAL LETTER N WITH TILDE"
  },
  {
    "code": "\u00D2",
    "name": "LATIN CAPITAL LETTER O WITH GRAVE"
  },
  {
    "code": "\u00D3",
    "name": "LATIN CAPITAL LETTER O WITH ACUTE"
  },
  {
    "code": "\u00D4",
    "name": "LATIN CAPITAL LETTER O WITH CIRCUMFLEX"
  },
  {
    "code": "\u00D5",
    "name": "LATIN CAPITAL LETTER O WITH TILDE"
  },
  {
    "code": "\u00D6",
    "name": "LATIN CAPITAL LETTER O WITH DIAERESIS"
  },
  {
    "code": "\u00D7",
    "name": "MULTIPLICATION SIGN"
  },
  {
    "code": "\u00D8",
    "name": "LATIN CAPITAL LETTER O WITH STROKE"
  },
  {
    "code": "\u00D9",
    "name": "LATIN CAPITAL LETTER U WITH GRAVE"
  },
  {
    "code": "\u00DA",
    "name": "LATIN CAPITAL LETTER U WITH ACUTE"
  },
  {
    "code": "\u00DB",
    "name": "LATIN CAPITAL LETTER U WITH CIRCUMFLEX"
  },
  {
    "code": "\u00DC",
    "name": "LATIN CAPITAL LETTER U WITH DIAERESIS"
  },
  {
    "code": "\u00DD",
    "name": "LATIN CAPITAL LETTER Y WITH ACUTE"
  },
  {
    "code": "\u00DE",
    "name": "LATIN CAPITAL LETTER THORN (Icelandic)"
  },
  {
    "code": "\u00DF",
    "name": "LATIN SMALL LETTER SHARP S (German)"
  },
  {
    "code": "\u00E0",
    "name": "LATIN SMALL LETTER A WITH GRAVE"
  },
  {
    "code": "\u00E1",
    "name": "LATIN SMALL LETTER A WITH ACUTE"
  },
  {
    "code": "\u00E2",
    "name": "LATIN SMALL LETTER A WITH CIRCUMFLEX"
  },
  {
    "code": "\u00E3",
    "name": "LATIN SMALL LETTER A WITH TILDE"
  },
  {
    "code": "\u00E4",
    "name": "LATIN SMALL LETTER A WITH DIAERESIS"
  },
  {
    "code": "\u00E5",
    "name": "LATIN SMALL LETTER A WITH RING ABOVE"
  },
  {
    "code": "\u00E6",
    "name": "LATIN SMALL LETTER AE"
  },
  {
    "code": "\u00E7",
    "name": "LATIN SMALL LETTER C WITH CEDILLA"
  },
  {
    "code": "\u00E8",
    "name": "LATIN SMALL LETTER E WITH GRAVE"
  },
  {
    "code": "\u00E9",
    "name": "LATIN SMALL LETTER E WITH ACUTE"
  },
  {
    "code": "\u00EA",
    "name": "LATIN SMALL LETTER E WITH CIRCUMFLEX"
  },
  {
    "code": "\u00EB",
    "name": "LATIN SMALL LETTER E WITH DIAERESIS"
  },
  {
    "code": "\u00EC",
    "name": "LATIN SMALL LETTER I WITH GRAVE"
  },
  {
    "code": "\u00ED",
    "name": "LATIN SMALL LETTER I WITH ACUTE"
  },
  {
    "code": "\u00EE",
    "name": "LATIN SMALL LETTER I WITH CIRCUMFLEX"
  },
  {
    "code": "\u00EF",
    "name": "LATIN SMALL LETTER I WITH DIAERESIS"
  },
  {
    "code": "\u00F0",
    "name": "LATIN SMALL LETTER ETH (Icelandic)"
  },
  {
    "code": "\u00F1",
    "name": "LATIN SMALL LETTER N WITH TILDE"
  },
  {
    "code": "\u00F2",
    "name": "LATIN SMALL LETTER O WITH GRAVE"
  },
  {
    "code": "\u00F3",
    "name": "LATIN SMALL LETTER O WITH ACUTE"
  },
  {
    "code": "\u00F4",
    "name": "LATIN SMALL LETTER O WITH CIRCUMFLEX"
  },
  {
    "code": "\u00F5",
    "name": "LATIN SMALL LETTER O WITH TILDE"
  },
  {
    "code": "\u00F6",
    "name": "LATIN SMALL LETTER O WITH DIAERESIS"
  },
  {
    "code": "\u00F7",
    "name": "DIVISION SIGN"
  },
  {
    "code": "\u00F8",
    "name": "LATIN SMALL LETTER O WITH STROKE"
  },
  {
    "code": "\u00F9",
    "name": "LATIN SMALL LETTER U WITH GRAVE"
  },
  {
    "code": "\u00FA",
    "name": "LATIN SMALL LETTER U WITH ACUTE"
  },
  {
    "code": "\u00FB",
    "name": "LATIN SMALL LETTER U WITH CIRCUMFLEX"
  },
  {
    "code": "\u00FC",
    "name": "LATIN SMALL LETTER U WITH DIAERESIS"
  },
  {
    "code": "\u00FD",
    "name": "LATIN SMALL LETTER Y WITH ACUTE"
  },
  {
    "code": "\u00FE",
    "name": "LATIN SMALL LETTER THORN (Icelandic)"
  },
  {
    "code": "\u00FF",
    "name": "LATIN SMALL LETTER Y WITH DIAERESIS"
  }
]

for i in chardict:
    characters += i['code'] + '\t' + i['name'] + '\n'


rofi = Popen(
      args=[
            'rofi',
            '-theme',
            'solarized',
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
    elif rofi.returncode == 10:
        xsel = Popen(
            args=[
                'xsel',
                '-i',
                '-b'
            ],
            stdin=PIPE
        )
        xsel.communicate(input=character)
