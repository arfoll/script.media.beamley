#import xbmcaddon
#
#Addon = xbmcaddon.Addon(id='script.media.beamly')

import requests
import pprint
import json
import os

#zeedictus = {"zeebox-app-id":"03c9eeb1", "zeebox-app-key":"bff5ff48a94ddc4be49c0504c886b411"}
zeedictuk = {"zeebox-app-id":"28a8577d", "zeebox-app-key":"ad9b49c4bc3006daa1520e0ee8574b72"}
zeedict = zeedictuk

# proper api url
beamly = "https://api-uk.zeebox.com/"
# fake api url
#beamly ="https://zgateway-i.zeebox.com/"

#def makeReq():

search = "search/2/blended-search"
reqparam = {"q":"archer", "tvc":"uk"}

print(reqparam)

r = requests.get(beamly+search, headers=zeedict, params=reqparam)

print(r.status_code)

parsed = json.loads(r.text)
feedid=parsed['sections'][0]['docs'][0]['entity']['id']
print(feedid)

zeedict = {"content-type":"application/json"}
beamly="https://zgateway-i.zeebox.com/"
login = "auth/1/login"
payload = open(os.getenv("HOME") + "/login.json").read()
r = requests.post(beamly+login, data=payload, headers=zeedict)
print(r.text)

#userid = r.text[0]["access_token"]
token = json.loads(r.text)['access_token']
userid={}
userid["access_token"] = token

follow = "connector/2/me/feed/"
beamly="https://zconnect-i.zeebox.com/"
r = requests.put(beamly + follow + feedid, params=userid)

