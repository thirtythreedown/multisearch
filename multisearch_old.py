#! python3

##Command line tool to open several search engines in web browser with the same keywords
##Usage example: multisearch.py baby yoda stl

import webbrowser, sys, pyperclip

def duck_url(arguments):
    """crafts search URL to Duckduckgo"""
    duck_url_local = ('https://duckduckgo.com/?q=' + arguments)
    return duck_url_local

def goog_url(arguments):
    """crafts search URL for Google search engine"""
    goog_url_local = ('https://www.google.com/search?q=' + arguments)
    return goog_url_local

def redd_url(arguments):
    """crafts search URL for Reddit search engine"""
    redd_url_local = ('https://www.reddit.com/search/?q=' + arguments.replace('+', '%20'))
    return redd_url_local

if len(sys.argv) > 1:
    arguments = '+'.join(sys.argv[1:])
    ##Collecting command line input into arguments variable by slicing the sys.argv, connecting everything with + character
    
else:
    clipboard = pyperclip.paste()
    arguments = clipboard.replace(' ', '+')
    ##If no command line arguments, use pyperclip to paste from the clipboard contents as arguments

print("The search arguments stored are " + arguments)
duck_search = duck_url(arguments)
goog_search = goog_url(arguments)
redd_search = redd_url(arguments)
##Feeding arguments variable to the search URL functions

webbrowser.open(duck_search)
webbrowser.open(goog_search)
webbrowser.open(redd_search)
##Feeding variables to webbrowser.open()
