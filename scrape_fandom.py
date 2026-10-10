import urllib.request
import re
import os
import json

url = "https://harvestmoon.fandom.com/api.php?action=query&list=categorymembers&cmtitle=Category:Friends_of_Mineral_Town_items&cmlimit=100&format=json"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    response = urllib.request.urlopen(req).read()
    data = json.loads(response)
    print(data)
except Exception as e:
    print(e)
