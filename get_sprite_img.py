import urllib.request
import urllib.parse
import json

title = urllib.parse.quote("Staid (FoMT)")
api_url = f"https://harvestmoon.fandom.com/api.php?action=query&titles={title}&prop=images&format=json"
req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req).read()
data = json.loads(resp)
pages = data['query']['pages']
for page_id in pages:
    for img in pages[page_id].get('images', []):
        print(img['title'])
