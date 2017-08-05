#!/usr/bin/env python3

import webbrowser, sys
searchfor = ''
if len(sys.argv) > 1:
    searchfor = '+'.join(sys.argv[1:])

url_string = "https://www.google.com/search?q=" + searchfor

webbrowser.open(url_string)