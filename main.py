#import xbmcaddon
#
#Addon = xbmcaddon.Addon(id='script.media.beamley')

import requests
import pprint
import json

#zeedictus = {"zeebox-app-id":"03c9eeb1", "zeebox-app-key":"bff5ff48a94ddc4be49c0504c886b411"}
#zeedictuk = {"zeebox-app-id":"28a8577d", "zeebox-app-key":"ad9b49c4bc3006daa1520e0ee8574b72"}
#zeedict = zeedictuk

reqparam = {"episode":"42535", "tvc":"us", "view":"web"}

# proper api url
#beamley = "https://api-uk.zeebox.com/"
# fake api url
beamley ="https://zgateway-i.zeebox.com/"

#def makeReq():

search = "search/2/blended-search"
reqparam = {"q":"archer", "tvc":"uk"}

zeedict = {}
print(reqparam)

#r = requests.get('https://api.zeebox.com/tee/topics/downloads', headers=zeedict, params=reqparam)
r = requests.get(beamley+search, headers=zeedict, params=reqparam)
print(r.status_code)

parsed = json.loads(r.text)
print(parsed['sections']['docs'][0]['brands']['title'])
print(feedid=parsed['sections'][0]['docs'][0]['entity']['id'])
#print json.dumps(parsed, indent=4, sort_keys=True)

zeedict = {"content-type":"application/json"}
login = "auth/1/login"
payload = open("/home/brendan/login.json").read()
r = requests.post(beamley+login, data=payload, headers=zeedict)



connector = "connector/1/me/follows/"
r = requests.post(beamley+connector+feedid)

