import urllib.request
import re
import os
import concurrent.futures

pages = [
    "https://fogu.com/hm4/farm/cooking.htm",
    "https://fogu.com/hm4/farm/cooking2.htm",
    "https://fogu.com/hm4/moo/animal_items.htm",
    "https://fogu.com/hm4/farm/shopping.htm",
    "https://fogu.com/hm4/farm/misc.htm"
]

img_urls = set()
for page in pages:
    try:
        req = urllib.request.Request(page, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as res:
            html = res.read().decode('utf-8', errors='ignore')
            for match in re.findall(r'src=["\']?(\.\./img/[^"\'>\s]+)["\']?', html):
                img_urls.add("https://fogu.com/hm4/" + match.replace("../", ""))
    except:
        pass

def download(url):
    filename = url.split('/')[-1]
    save_path = os.path.join('items', filename)
    if not os.path.exists(save_path):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as res:
                with open(save_path, 'wb') as f:
                    f.write(res.read())
        except:
            pass

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(download, img_urls)

