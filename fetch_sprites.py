import urllib.request
import json
import re

url = "https://html.duckduckgo.com/html/?q=harvest+moon+friends+of+mineral+town+items+spriters+resource"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    links = re.findall(r'href="([^"]+spriters-resource[^"]+)"', html)
    for link in links:
        print(link)
except Exception as e:
    print(e)
