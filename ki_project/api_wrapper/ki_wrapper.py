"""
Lib that will act as a wrapper around the API:

http://www.clashapi.xyz/api/

For now, ki_wrapper provides 01 function:

get_random_deck --> queries the API and returns a list containing an aleatory deck

"""

# Importing python libraries for data manipulation
from urllib.request import urlopen
import json

def get_random_deck():
    # queries the API and returns a list containing an aleatory deck
    randomic_deck = urlopen('http://www.clashapi.xyz/api/random-deck')
    randomic_deck = json.loads(randomic_deck.read())
    return randomic_deck
