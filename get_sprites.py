import urllib.request
import json

sprites = ["Staid", "Nappy", "Bold", "Chef", "Aqua", "Hoggy", "Timid"]
urls = []

for s in sprites:
    # Fandom API image query
    api_url = f"https://harvestmoon.fandom.com/api.php?action=query&titles=File:{s}_(FoMT).png&prop=imageinfo&iiprop=url&format=json"
    req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        resp = urllib.request.urlopen(req).read()
        data = json.loads(resp)
        pages = data['query']['pages']
        for page_id in pages:
            if 'imageinfo' in pages[page_id]:
                url = pages[page_id]['imageinfo'][0]['url']
                urls.append((s, url))
            else:
                print(f"Image info missing for {s}")
    except Exception as e:
        print(f"Failed for {s}: {e}")

for name, url in urls:
    print(f"Downloading {name}...")
    import subprocess
    subprocess.run(["curl", "-s", "-o", f"items_clean/sprite_{name.lower()}.webp", url])

print("Done")
