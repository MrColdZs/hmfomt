import urllib.request
import urllib.parse
import json
import subprocess
import os
import re

with open('index.html') as f:
    html = f.read()

# Find all lines in ICONS_MAPPING that use 'items/'
mapping_block = re.search(r'const ICONS_MAPPING = \{([\s\S]*?)\n\};', html).group(1)
lines = mapping_block.split('\n')

to_download = []
for line in lines:
    if "'items/" in line and "'items_clean/" not in line:
        match = re.search(r"'([^']+)': 'items/([^']+)'", line)
        if match:
            key, old_file = match.groups()
            to_download.append((key, old_file))

def search_fandom_image(query):
    # Fandom search for images
    q = urllib.parse.quote(query)
    api_url = f"https://harvestmoon.fandom.com/api.php?action=query&list=allimages&aiprop=url&aiprefix={q}&format=json"
    req = urllib.request.Request(api_url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        resp = urllib.request.urlopen(req).read()
        data = json.loads(resp)
        if data["query"]["allimages"]:
            return data["query"]["allimages"][0]["url"]
    except:
        pass
    return None

def fetch_specific(title):
    t = urllib.parse.quote(title)
    api_url = f"https://harvestmoon.fandom.com/api.php?action=query&titles=File:{t}&prop=imageinfo&iiprop=url&format=json"
    req = urllib.request.Request(api_url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        resp = urllib.request.urlopen(req).read()
        data = json.loads(resp)
        pages = data["query"]["pages"]
        for p in pages:
            if 'imageinfo' in pages[p]:
                return pages[p]['imageinfo'][0]['url']
    except:
        pass
    return None

new_mappings = {}

print(f"Found {len(to_download)} items to fix.")

for key, old_file in to_download:
    # Try to guess Fandom image name
    search_query = key.title()
    
    # Custom mappings for better results
    custom = {
        'horse wins the festival': 'Horse',
        'horse affection maxed': 'Horse',
        'horse fully grown': 'Horse',
        '8 chicken slots': 'Chicken',
        '8 cows & 8 sheep': 'Cow',
        'house at maximum level': 'House',
        'barn fully upgraded': 'Barn',
        'coop fully upgraded': 'Chicken Coop',
        'villa, beach house, and mountain cabin': 'Town Villa',
        'all power berries': 'Power Berry',
        'stop the clock': 'Clock',
        'sweet potato': 'Sweet Potato',
        'green pepper': 'Green Pepper',
        'stone': 'Stone',
        'branch': 'Branch',
        'gem': 'Ruby',
        'fossil': 'Fossil of Ancient Fish',
        'level': 'Pink Diamond',
        'max': 'Pink Diamond',
        'infinite': 'Pink Diamond',
        'master': 'Pink Diamond',
        'recipe': 'Cookbook',
        'upgrade': 'Lumber',
        'stamina': 'Power Berry',
        'medicine': 'Bodigizer',
        'potion': 'Turbojolt',
        'day': 'Calendar',
        'year': 'Calendar',
        'bell': 'Bell',
        'brush': 'Brush',
        'milker': 'Milker',
        'shears': 'Clippers',
        'book': 'Book',
        'ore': 'Copper Ore',
        'fry': 'French Fries',
        'fries': 'French Fries',
        'noodle': 'Noodles',
        'flower': 'Toy Flower'
    }
    
    if key in custom:
        search_query = custom[key]
        
    url = fetch_specific(search_query + " (FoMT).png")
    if not url:
        url = fetch_specific(search_query + ".png")
    if not url:
        url = search_fandom_image(search_query.replace(' ', '_'))
        
    if url:
        safe_name = re.sub(r'[^a-z0-9]', '_', key.lower())
        filename = f"item_{safe_name}.webp"
        filepath = os.path.join("items_clean", filename)
        if not os.path.exists(filepath):
            subprocess.run(["curl", "-s", "-o", filepath, url])
        new_mappings[old_file] = f"items_clean/{filename}"
        print(f"Fixed {key} -> {url}")
    else:
        print(f"Could not find image for {key}")

with open('new_mappings.json', 'w') as f:
    json.dump(new_mappings, f, indent=2)

