import urllib.request
import urllib.parse
import json

q = urllib.parse.quote("Staid")
api_url = f"https://harvestmoon.fandom.com/api.php?action=query&list=search&srsearch={q}&format=json"
req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req).read()
data = json.loads(resp)
for res in data['query']['search']:
    print(res['title'])
