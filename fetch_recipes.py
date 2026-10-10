import urllib.request
import json
import re
from bs4 import BeautifulSoup
import os

url = "https://harvestmoon.fandom.com/wiki/Cooking_Recipes_(FoMT)"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

req = urllib.request.Request(url, headers=headers)
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    with open('fandom_recipes.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Downloaded HTML")
except Exception as e:
    print(f"Failed to download HTML: {e}")
