from os import name
import requests
from bs4 import BeautifulSoup
import json
import sys
from colorama import init
init(convert=True)

print(r"""
 ______ __    __ __ ______ ______  ____ ____       ___ __  __  ____   ___ __ __  ____ ____ 
 | || | ||    || || | || | | || | ||    || \\     //   ||  || ||     //   || // ||    || \\
   ||   \\ /\ // ||   ||     ||   ||==  ||_//    ((    ||==|| ||==  ((    ||<<  ||==  ||_//
   ||    \V/\V/  ||   ||     ||   ||___ || \\     \\__ ||  || ||___  \\__ || \\ ||___ || \\

Made by Dom Is Offline#0001                                                                                     
""")

names = []
available = []
with open("usernames.txt", "r", encoding="utf8") as f:
    for line in f:
        names.append(line.strip())
        
for i in names:
    url = "https://api.twitter.com/graphql/P8ph10GzBbdMqWZxulqCfA/UserByScreenName?variables=%7B%22screen_name%22%3A%22" + i + "%22%2C%22withHighlightedLabel%22%3Atrue%7D"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,bn;q=0.8",
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        "content-type": "application/json",
        "dnt": "1",
        'origin': 'https://twitter.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36',
        'x-twitter-active-user': 'yes',
        'x-twitter-client-language': 'en'
        }
    resp  = json.loads(requests.get(url, headers=headers).text)
    try:
        print(f"\u001b[31m{i} unavailable since " + resp["data"]["user"]["legacy"]["created_at"] + '\u001b[0m')
    except:
        try:
            err = resp["errors"][0]["message"]
            if f"User '{i}' not found" == err:
                print(f"\u001b[32m{i} is available\u001b[0m")
                available.append(i)
            else:
                pass
        except:
            print(f"\u001b[32m{i} is available\u001b[0m")
            available.append(i)
with open('available.txt', 'w+', encoding="utf8") as f:
    for i in available:
        f.write(i+'\n')
        # this block of code(finally) can be removed if you dont need server response