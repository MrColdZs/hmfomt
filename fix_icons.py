import urllib.request
import urllib.parse
import json
import subprocess
import os
import re

with open('index.html') as f:
    html = f.read()

mapping_block = re.search(r'const ICONS_MAPPING = \{([\s\S]*?)\n\};', html).group(1)
lines = mapping_block.split('\n')

to_download = []
for line in lines:
    if "'items/" in line:
        match = re.search(r"'([^']+)': 'items/([^']+)'", line)
        if match:
            key, old_file = match.groups()
            to_download.append((key, old_file))

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

print(f"Found {len(to_download)} items to fix.")

new_mappings = {}

for key, old_file in to_download:
    search_query = key.title()
    
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
        'flower': 'Toy Flower',
        'turnip': 'Turnip',
        'potato': 'Potato',
        'cucumber': 'Cucumber',
        'strawberry': 'Strawberry',
        'cabbage': 'Cabbage',
        'tomato': 'Tomato',
        'onion': 'Onion',
        'pumpkin': 'Pumpkin',
        'pineapple': 'Pineapple',
        'eggplant': 'Eggplant',
        'carrot': 'Carrot',
        'spinach': 'Spinach',
        'apple': 'Apple',
        'honey': 'Honey',
        'bamboo': 'Bamboo Shoot',
        'mushroom': 'Mushroom',
        'truffle': 'Truffle',
        'grape': 'Wild Grape',
        'fish': 'Medium Fish',
        'egg': 'Regular Quality Egg',
        'mayonnaise': 'Mayonnaise (S)',
        'milk': 'Milk (S)',
        'cheese': 'Cheese (S)',
        'wool': 'Wool (S)',
        'yarn': 'Yarn (S)',
        'bracelet': 'Bracelet',
        'necklace': 'Necklace',
        'earrings': 'Earrings',
        'brooch': 'Brooch',
        'horse': 'Horse',
        'chicken': 'Chicken',
        'cow': 'Cow',
        'sheep': 'Sheep',
        'tool': 'Hammer',
        'sickle': 'Sickle',
        'hoe': 'Hoe',
        'ax': 'Axe',
        'hammer': 'Hammer',
        'watering can': 'Watering Can',
        'fishing rod': 'Fishing Rod',
        'house': 'House',
        'wine': 'Wine',
        'chocolate': 'Chocolate',
        'cake': 'Cake',
        'cookie': 'Cookies',
        'ice cream': 'Ice Cream',
        'bread': 'Bread',
        'pizza': 'Pizza',
        'sushi': 'Sushi'
    }
    
    if key in custom:
        search_query = custom[key]
        
    # Strict searching
    url = fetch_specific(search_query + " (FoMT).png")
    if not url:
        url = fetch_specific(search_query + ".png")
        
    if url:
        safe_name = re.sub(r'[^a-z0-9]', '_', key.lower())
        filename = f"item_{safe_name}.webp"
        filepath = os.path.join("items_clean", filename)
        if not os.path.exists(filepath):
            subprocess.run(["curl", "-s", "-o", filepath, url])
        new_mappings[f"'items/{old_file}'"] = f"'items_clean/{filename}'"
        print(f"Fixed {key}")
    else:
        print(f"Missing {key} ({search_query})")

for old, new in new_mappings.items():
    html = html.replace(old, new)

with open('index.html', 'w') as f:
    f.write(html)
    
print("index.html patched!")
