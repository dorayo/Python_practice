#!/usr/local/bin/python3

import json
from urllib.request import urlopen

def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")+' - '+responseJson.get('country_name')

print(getCountry("61.135.165.224"))
