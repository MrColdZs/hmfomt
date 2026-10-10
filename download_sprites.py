import urllib.request
import re
import os

pages = [
    "https://fogu.com/hm4/farm/complete_list.htm",
    "https://fogu.com/hm4/farm/tools.htm",
    "https://fogu.com/hm4/farm/mine.htm",
    "https://fogu.com/hm4/moo/index.htm",
    "https://fogu.com/hm4/moo/chicken.htm",
    "https://fogu.com/hm4/moo/cows.htm",
    "https://fogu.com/hm4/moo/sheep.htm",
    "https://fogu.com/hm4/moo/dog_horse.htm",
    "https://fogu.com/hm4/farm/houses.htm"
]

img_urls = set()

for page in pages:
    try:
        req = urllib.request.Request(page, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8', errors='ignore')
            matches = re.findall(r'src="\.\./(img/[^"]+)"', html)
            for m in matches:
                img_urls.add("https://fogu.com/hm4/" + m)
    except Exception as e:
        print(f"Error fetching {page}: {e}")

if not os.path.exists('items'):
    os.makedirs('items')

for url in img_urls:
    filename = url.split('/')[-1]
    save_path = os.path.join('items', filename)
    if not os.path.exists(save_path):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as response:
                with open(save_path, 'wb') as out_file:
                    out_file.write(response.read())
            print(f"Downloaded {filename}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")
    else:
        print(f"Already have {filename}")

