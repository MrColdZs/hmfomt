import urllib.request
import urllib.parse
import json
import subprocess

girls = ["Popuri", "Mary", "Karen", "Elli", "Ann", "Harvest Goddess"]

for s in girls:
    title = urllib.parse.quote(f"File:Th {s}.png")
    api_url = f"https://harvestmoon.fandom.com/api.php?action=query&titles={title}&prop=imageinfo&iiprop=url&format=json"
    req = urllib.request.Request(api_url, headers={"User-Agent": "Mozilla/5.0"})
    resp = urllib.request.urlopen(req).read()
    data = json.loads(resp)
    pages = data["query"]["pages"]
    found = False
    for page_id in pages:
        if 'imageinfo' in pages[page_id]:
            url = pages[page_id]['imageinfo'][0]['url']
            print(f"Downloading {s} from {url}")
            subprocess.run(["curl", "-s", "-o", f"items_clean/face_{s.lower().replace(' ', '_')}.webp", url])
            found = True
    if not found:
        print(f"No image info for {s}")
