import urllib.request
import re
import os
import concurrent.futures

pages = [
    "https://fogu.com/hm4/farm/complete_list.htm",
    "https://fogu.com/hm4/farm/tools.htm",
    "https://fogu.com/hm4/farm/mine.htm",
    "https://fogu.com/hm4/farm/items.htm",
    "https://fogu.com/hm4/events/jewels.htm"
]

img_urls = set()
for page in pages:
    try:
        req = urllib.request.Request(page, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as res:
            html = res.read().decode('utf-8', errors='ignore')
            for match in re.findall(r'src=["\']?(\.\./img/[^"\'>\s]+)["\']?', html):
                img_urls.add("https://fogu.com/hm4/" + match.replace("../", ""))
    except Exception as e:
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

