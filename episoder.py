# Episoder by Ben Rothman
# Quick little tool to hit an API to see if the next episode of a given show has been released.
# python3 episoder.py
import requests
import sys
from time import sleep
import json

# define color printing variables
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
OKCYAN = '\033[36m'
YELLOW = '\033[33m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def normalize(s):
    s = s.replace(' ', '')
    s = s.replace('\'', '')
    return s.lower().strip()

def fuzzy_validate(raw):
    shows = ['bigbangtheory', 'thewalkingdead', 'gameofthrones', 'southpark', 'sharktank',
     'cleaninglady', 'community', '30rock','itsalwayssunny', 'arresteddevelopment',
     'that70sshow', 'rickandmorty', 'siliconvalley', 'mrrobot', 'house', 'eureka', 'scrubs',
     'kimsconvenience', 'schittscreek', 'sherlock']
    for show in shows:
        if raw == show or ('the ' + raw) == show or raw[3:] == show:
            return show
    print(FAIL + 'Not a valid show "' + raw + '"' + ENDC)
    quit()

# define 'my_print()
def my_print(words):
    """prints text with effect"""
    for char in words:
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write("\n")






##### PROGRAM #####
word = input('Input a Show: ')
title = normalize(word)
title = fuzzy_validate(title)
res = requests.get('https://epguides.frecar.no/show/' + title + '/next/')

if res.text == '{"error": "Episode not found"}':
    my_print(FAIL + 'Error for input "' + word + '"' + ENDC)
else:
    # parse json into dic:
    dic = json.loads(res.text)
    # Clear the Screen
    print(chr(27) + "[2J")
    my_print(HEADER + dic['episode']['show']['title'] + ENDC)
    print('==============')
    my_print(OKCYAN + 'Title: ' + dic['episode']['title'] + ENDC)
    my_print(OKBLUE + 'Season: ' + str(dic['episode']['season']) + ENDC)
    my_print(OKBLUE + 'Episode: ' + str(dic['episode']['number']) + ENDC)
    my_print(OKCYAN + 'Release Date: ' + dic['episode']['release_date'] + ENDC)