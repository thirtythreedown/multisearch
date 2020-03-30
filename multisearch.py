#! python3

##Command line tool to open several search engines in web browser with the same keywords
##Usage example: multisearch.py "baby yoda" stl

import webbrowser, sys

def keywords_extractor(raw_keywords):
    keywords_list = []
    keywords_list = raw_keywords.split(' ')
    return keywords_list

def plus_string(keywords):
    """crafts search URL for search engines using + as a joining element"""
    plus_string_local = '+'.join(keywords)
    return plus_string_local

def twenty_string(keywords):
    """crafts search URL for search engines using %20 as a joining element"""
    twenty_string_local = '%20'.join(keywords)
    return twenty_string_local

def space_string(keywords):
    """crafts search URL for search engines using space as a joining element"""
    space_string_local = ' '.join(keywords)
    return space_string_local

def core_url(core_string):
    """crafts search URL for Core77"""
    core_url_local = ('https://www.core77.com//home/search?search=' + core_string)
    return core_url_local

def dez_url(dez_string):
    """crafts search URL for Dezeen"""
    dez_url_local = ('https://www.dezeen.com/?s=' + dez_string)
    return dez_url_local

def duck_url(duck_string):
    """crafts search URL for Duckduckgo"""
    duck_url_local = ('https://duckduckgo.com/?q=' + duck_string)
    return duck_url_local

def goog_url(goog_string):
    """crafts search URL for Google search engine"""
    goog_url_local = ('https://www.google.com/search?q=' + goog_string)
    return goog_url_local

def googi_url(googi_string):
    """crafts search URL for Google Images search engine"""
    googi_url_local = ('https://www.google.com/search?tbm=isch&q=' + googi_string + '&oq=' + googi_string)
    return googi_url_local

def mmf_url(stl_string):
    """crafts search URL for MyMiniFactory"""
    mmf_url_local = ('https://www.myminifactory.com/search/?query=' + stl_string)
    return mmf_url_local

def redd_url(redd_string):
    """crafts search URL for Reddit"""
    redd_url_local = ('https://www.reddit.com/search/?q=' + redd_string)
    return redd_url_local

def thingiverse_url(stl_string):
    """crafts search URL for Thingiverse"""
    thingiverse_url_local = ('https://www.thingiverse.com/search?q=' + stl_string + '&type=things')
    return thingiverse_url_local

def yahoo_url(yahoo_string):
    """crafts search URL for Yahoo search engine"""
    yahoo_url_local = ('https://search.yahoo.com/search?p=' + yahoo_string + '&ei=UTF-8')
    return yahoo_url_local

def youmagine_url(stl_string):
    """crafts search URL for Youmagine"""
    youmagine_url_local = ('https://www.youmagine.com/search/designs?search=' + stl_string)
    return youmagine_url_local

##Bringing up help notes if requested
if sys.argv[1] == "-h":
    print("Welcome to the Multisearch engine!")
    print("Use several search engines in one shot from your terminal.")
    print('Example: multisearch.py "baby yoda" -stl')
    print("Complete instructions at https://github.com/thirtythreedown/multisearch - enjoy!")

else:
    ##Extracting list of keywords from command line arguments
    raw_keywords = sys.argv[1]
    keywords = []
    keywords = keywords_extractor(raw_keywords)

    ##Iterating through command line arguments
    arguments = len(sys.argv) - 1    
    position = 2
    while arguments >= position:
        ##Composing and opening URLs based on command line arguments
        if sys.argv[position] == "-c":
            core_string = plus_string(keywords)
            core_url = core_url(core_string)
            webbrowser.open(core_url)

        elif sys.argv[position] == "-d":
            duck_string = plus_string(keywords)
            duck_url = duck_url(duck_string)
            webbrowser.open(duck_url)

        elif sys.argv[position] == "-dz":
            dez_string = space_string(keywords)
            dez_url = dez_url(dez_string)
            webbrowser.open(dez_url)

        elif sys.argv[position] == "-g":
            goog_string = plus_string(keywords)
            goog_url = goog_url(goog_string)
            webbrowser.open(goog_url)

        elif sys.argv[position] == "-gi":
            googi_string = plus_string(keywords)
            googi_url = googi_url(googi_string)
            webbrowser.open(googi_url)

        elif sys.argv[position] == "-r":
            reddit_string = twenty_string(keywords)
            reddit_url = redd_url(reddit_string)
            webbrowser.open(reddit_url)

        elif sys.argv[position] == "-stl":
            stl_string = plus_string(keywords)
            mmf_url = mmf_url(stl_string)
            thingiverse_url = thingiverse_url(stl_string)
            youmagine_url = youmagine_url(stl_string)
            webbrowser.open(thingiverse_url)
            webbrowser.open(youmagine_url)
            webbrowser.open(mmf_url)

        elif sys.argv[position] == "-y":
            yahoo_string = plus_string(keywords)
            yahoo_url = yahoo_url(yahoo_string)
            webbrowser.open(yahoo_url)

        else:
            ##Error message in case of exception
            print("%s doesn't do anything yet, sorry! Did you mistype?" % (sys.argv[position]))
        
        position = position+1

    print("All done!")
