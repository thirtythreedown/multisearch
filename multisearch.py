#! python3

import webbrowser, sys, pyperclip
##Importing modules. webbrowser to open webbrowser, sys to access command line and arguments, pyperclip for clipboard

def duck_url(arguments):
    """crafts search URL to Duckduckgo"""
    duck_url_local = ('https://duckduckgo.com/?q=' + arguments)
    ##Putting the DuckDuckGo search URL together
    return duck_url_local
    ##Returning the completed DuckDuckGo search URL

def goog_url(arguments):
    """crafts search URL for Google search engine"""
    goog_url_local = ('https://www.google.com/search?q=' + arguments)
    ##Putting the Google search URL together
    return goog_url_local
    ##Returning the completed Google search URL

def redd_url(arguments):
    """crafts search URL for Google search engine"""
    redd_url_local = ('https://www.reddit.com/search/?q=' + arguments.replace('+', '%20'))
    ##Putting the reddit search URL together and replacing space characters with %20 in one shot
    return redd_url_local
    ##Returning the completed Reddit search URL

if len(sys.argv) > 1:
    ##If the length of command line arguments is longer than 1...
    arguments = '+'.join(sys.argv[1:])
    ##Collecting command line input into arguments variable by slicing the sys.argv
    
else:
##If the command line is empty...
    clipboard = pyperclip.paste()
    arguments = clipboard.replace(' ', '+')
    ##We use the paste() method from pyperclip to paste the clipboard contents into the address

print("The search arguments stored are " + arguments)
duck_search = duck_url(arguments)
goog_search = goog_url(arguments)
redd_search = redd_url(arguments)
##Feeding arguments variable to the search URL functions

webbrowser.open(duck_search)
webbrowser.open(goog_search)
webbrowser.open(redd_search)
##Feeding variables to webbrowser.open()
